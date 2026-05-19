"""Stage 1: Extract and split mock-interview submissions into per-problem folders.

Input:  mock_raw_unzipped/  (Brightspace file-upload download, unzipped)
Output: per-problem folders with raw/ (full doc) and code/ (extracted code),
        inputs/students.csv, manifest per problem, reports/missing_mandatory.csv

Pipeline:
  1. Parse folder names -> student ID, name, timestamp
  2. Pick latest submission per student
  3. Read file content (txt/py direct; docx/pdf/rtf via libraries; images -> manual)
  4. Detect which LeetCode problem the student solved
  5. Extract candidate code section (strip interviewer form / prose)
  6. Repair indentation (tabs vs spaces, flat indent detection)
  7. Write raw/ (full doc), code/ (extracted code), manifest.csv
"""
import csv
import json
import os
import re
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UNZIPPED = ROOT / "mock_raw_unzipped"
INPUTS = ROOT / "inputs"
REPORTS = ROOT / "reports"

FOLDER_RE = re.compile(
    r"^(\d+)-\d+\s*-\s*(.+?)\s*-\s*"
    r"((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2},\s*\d{4}\s+\d{1,2}\d{2}\s*[AP]M)$"
)

PROBLEM_SIGNATURES = {
    "guess_number": {
        "functions": [r"\bguess\s*[Nn]umber\b", r"\bguess\s*\(\s*mid\b", r"\bguess\s*\(\s*\w+\s*\)\s*[!=<>]"],
        "titles": [r"[Gg]uess\s+[Nn]umber", r"[Gg]uess\s+[Gg]ame", r"[Hh]igher\s+or\s+[Ll]ower"],
    },
    "longest_substring": {
        "functions": [r"\blengthOfLongestSubstring\b", r"\blength_of_longest_substring\b",
                      r"\blongest[Ss]ubstring\b", r"\blengthofLongestSubstring\b",
                      r"s\.charAt\("],
        "titles": [r"[Ll]ongest\s+[Ss]ubstring", r"[Ww]ithout\s+[Rr]epeating"],
    },
    "contains_nearby_duplicate": {
        "functions": [r"\bcontainsNearbyDuplicate\b", r"\bcontains_nearby_duplicate\b",
                      r"\bnearby[Dd]uplicate\b"],
        "titles": [r"[Cc]ontains\s+[Nn]earby\s+[Dd]uplicate"],
    },
    "merge_two_sorted_lists": {
        "functions": [r"\bmergeTwoLists?\b", r"\bmerge_two_lists\b",
                      r"\bmergeTwoSortedLists\b"],
        "titles": [r"[Mm]erge\s+[Tt]wo\s+[Ss]orted\s+[Ll]ists?"],
    },
    "eval_rpn": {
        "functions": [r"\bevalRPN\b", r"\beval_rpn\b", r"\bevalPRN\b", r"\bexalRPN\b",
                      r"\breversepolishnotation\b", r"\breverse_polish\b"],
        "titles": [r"[Rr]everse\s+[Pp]olish", r"\bRPN\b"],
    },
}

PROBLEM_FN_INFO = {
    "guess_number":                {"fn_name": "guessNumber",               "params": ["n"]},
    "longest_substring":           {"fn_name": "lengthOfLongestSubstring",  "params": ["s"]},
    "contains_nearby_duplicate":   {"fn_name": "containsNearbyDuplicate",   "params": ["nums", "k"]},
    "merge_two_sorted_lists":      {"fn_name": "mergeTwoLists",             "params": ["list1", "list2"]},
    "eval_rpn":                    {"fn_name": "evalRPN",                   "params": ["tokens"]},
}


def parse_folder_name(name: str):
    m = FOLDER_RE.match(name)
    if not m:
        return None
    bid = m.group(1)
    name_part = m.group(2).strip()
    date_str = m.group(3).strip()
    parts = name_part.split(",", 1)
    if len(parts) == 2:
        last_name = parts[0].strip()
        first_name = parts[1].strip()
    else:
        last_name = name_part
        first_name = ""
    for fmt in ("%b %d, %Y %I%M %p", "%b %d, %Y %H%M %p"):
        try:
            dt = datetime.strptime(date_str, fmt)
            return bid, first_name, last_name, dt
        except ValueError:
            continue
    return bid, first_name, last_name, datetime.min


def read_text_file(path: Path) -> str:
    for enc in ("utf-8", "utf-8-sig", "latin-1", "cp1252"):
        try:
            return path.read_text(encoding=enc)
        except (UnicodeDecodeError, ValueError):
            continue
    return ""


def read_docx(path: Path) -> str:
    try:
        from docx import Document
        doc = Document(str(path))
        return "\n".join(p.text for p in doc.paragraphs)
    except Exception as e:
        return f"[DOCX extraction failed: {e}]"


def read_doc(path: Path) -> str:
    # .doc (legacy format) - try antiword or fallback to raw text extraction
    try:
        import subprocess
        result = subprocess.run(["antiword", str(path)], capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            return result.stdout
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass
    # Fallback: try reading as raw bytes and extracting ASCII text
    try:
        data = path.read_bytes()
        text_parts = []
        current = []
        for b in data:
            if 32 <= b < 127 or b in (9, 10, 13):
                current.append(chr(b))
            else:
                if len(current) > 3:
                    text_parts.append("".join(current))
                current = []
        if current and len(current) > 3:
            text_parts.append("".join(current))
        raw = "\n".join(text_parts)
        if len(raw) > 50:
            return raw
    except Exception:
        pass
    return "[DOC extraction failed: antiword not available, raw extraction insufficient]"


def read_pdf(path: Path) -> str:
    try:
        from PyPDF2 import PdfReader
        reader = PdfReader(str(path))
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text
    except Exception as e:
        return f"[PDF extraction failed: {e}]"


def read_rtf(path: Path) -> str:
    try:
        from striprtf.striprtf import rtf_to_text
        raw = path.read_text(encoding="utf-8", errors="replace")
        return rtf_to_text(raw)
    except Exception as e:
        return f"[RTF extraction failed: {e}]"


def read_ipynb(path: Path) -> str:
    try:
        import nbformat
        nb = nbformat.read(str(path), as_version=4)
        code_cells = []
        for cell in nb.cells:
            if cell.cell_type == "code":
                code_cells.append(cell.source)
            elif cell.cell_type == "markdown":
                code_cells.append(f"# {cell.source}")
        return "\n\n".join(code_cells)
    except Exception as e:
        return f"[IPYNB extraction failed: {e}]"


def read_any_file(path: Path) -> tuple[str, str]:
    """Returns (text_content, extraction_method)."""
    ext = path.suffix.lower()
    if ext in (".txt", ".py"):
        return read_text_file(path), "direct"
    if ext == ".docx":
        return read_docx(path), "docx"
    if ext == ".doc":
        return read_doc(path), "doc"
    if ext == ".pdf":
        return read_pdf(path), "pdf"
    if ext == ".rtf":
        return read_rtf(path), "rtf"
    if ext == ".ipynb":
        return read_ipynb(path), "ipynb"
    if ext in (".jpeg", ".jpg", ".png", ".heic"):
        return "", "image"
    if ext == "":
        return read_text_file(path), "no-ext"
    return "", f"unsupported-{ext}"


def detect_problem(text: str) -> str:
    scores = {}
    for problem, sigs in PROBLEM_SIGNATURES.items():
        score = 0
        for pat in sigs["functions"]:
            if re.search(pat, text):
                score += 3
        for pat in sigs["titles"]:
            if re.search(pat, text):
                score += 2
        scores[problem] = score
    best = max(scores, key=scores.get)
    if scores[best] == 0:
        return "unknown"
    return best


def detect_language(text: str) -> str:
    if not text or not text.strip():
        return "empty"
    has_def = bool(re.search(r"\bdef\s+\w+\s*\(", text))
    has_java_sig = bool(re.search(r"(?:public|private|protected)\s+(?:static\s+)?\w+\s+\w+\s*\(", text))
    has_braces = "{" in text and "}" in text
    has_semi = ";" in text
    if has_def:
        return "python"
    if has_java_sig or (has_braces and has_semi and not has_def):
        return "java"
    # Check for pseudocode-like content
    low = text.lower()
    code_kws = ["for ", "while ", "if ", "return ", "def ", "class ", "print("]
    if any(kw in low for kw in code_kws):
        return "pseudocode"
    return "pseudocode"


# ---- Code extraction ----

CANDIDATE_MARKERS = [
    r"^Candidate\s+Form\s*:?\s*$",
    r"\[Insert\s+Submitted\s+Code\]",
    r"^Candidate\s+Code\s*:?\s*$",
    r"^Implement\s*:",
    r"^My\s+Solution\s*:?\s*$",
    r"^(?:My\s+)?Code\s*:\s*$",
]

INTERVIEWER_MARKERS = [
    r"Interviewer\s+Form",
    r"Problem\s+Understanding",
    r"Communication\s+&\s+Collaboration",
    r"Implementation\s+&\s+Technical",
    r"Team\s+Fit",
    r"Final\s+Evaluation",
    r"Final\s+Decision",
]

TEMPLATE_HEADER_LINES = {
    "CS102 PAIRED TECHNICAL INTERVIEW",
    "This is the template for what you are expected to submit",
    "Please make sure you have your items in this order",
    "Refer back to the Paired Technical Interview",
    "We encourage you to comment your code",
}


def is_code_line(line: str) -> bool:
    """Check if a line looks like code rather than prose."""
    s = line.strip()
    if not s:
        return False
    if s.startswith("#") or s.startswith("//"):
        return True
    code_starters = (
        "def ", "class ", "for ", "if ", "elif ", "else:", "else ",
        "while ", "return", "import ", "from ", "try:", "except",
        "finally:", "with ", "raise ", "break", "continue", "pass",
        "print(", "print (", "@", "self.", "int ", "public ", "private ",
        "static ", "void ", "String ", "boolean ",
    )
    if any(s.startswith(kw) for kw in code_starters):
        return True
    # Assignment or function call patterns
    if re.match(r"^\s*\w+\s*[=\[({]", s):
        return True
    if re.match(r"^\s*\w+\.\w+", s):
        return True
    # Indented content (likely inside a code block)
    if line.startswith(("\t", "    ")):
        return True
    # Operators / brackets — but exclude rubric-like lines (e.g., "2) Communication & Collaboration")
    code_chars = set("=(){}[]<>+-*/%!&|^;:")
    char_count = sum(1 for c in s if c in code_chars)
    if char_count >= 3 and len(s) < 120:
        return True
    # 2 code chars is only code if most chars aren't alphabetic words
    if char_count == 2 and len(s) < 80:
        words = s.split()
        alpha_words = sum(1 for w in words if w.isalpha())
        if alpha_words <= len(words) * 0.5:
            return True
    return False


LEADING_PROSE_PATTERNS = [
    r"^(My\s+name|Partner'?s?\s+name|Name|Student)\s*:?\s+\w",
    r"^(Problem|Question)\s*:?\s+",
    r"^(Candidate|Interviewer)\s+(Form|Code)",
    r"^(Technical\s+Interview|Mock\s+Interview)",
    r"^\d+/\d+\s+CS\d+",
    r"^CS\s*102\s+(PAIRED\s+)?",
    r"^(Submitted|Written)\s+by",
    r"^(Solution|Code)\s*:?\s*$",
    r"^\[Insert\s+",
    r"^(Guess|Merge|Contains|Evaluate|Longest)\s+",
    r"^(Implement|Review|Plan|Match)\s*:",
    r"^Python\s+Mock",
]


def _strip_leading_prose_lines(text: str) -> str:
    """Remove leading non-code lines (student names, problem titles, etc.)."""
    lines = text.split("\n")
    start = 0
    for i, line in enumerate(lines):
        s = line.strip()
        if not s:
            start = i + 1
            continue
        # Check if it's a prose/header line
        is_prose = False
        for pat in LEADING_PROSE_PATTERNS:
            if re.match(pat, s, re.IGNORECASE):
                is_prose = True
                break
        # Short non-code line without code characters (a name, title, etc.)
        if not is_prose and not is_code_line(line) and len(s.split()) <= 8:
            is_prose = True
        if is_prose:
            start = i + 1
            continue
        break

    result = "\n".join(lines[start:]).strip()

    # Also strip leading triple-quoted docstrings that contain problem descriptions
    result = _strip_leading_docstring(result)

    return result


def _strip_leading_docstring(code: str) -> str:
    """Strip leading triple-quoted docstrings (problem descriptions pasted as docstrings).

    Loops to handle multiple consecutive docstrings.
    Also handles the case where extracted text contains a stray closing `\"\"\"`
    followed by actual code — takes the code after the last docstring boundary.
    """
    # First: loop-strip leading docstrings
    changed = True
    while changed:
        changed = False
        stripped = code.lstrip()
        for delim in ('"""', "'''"):
            if stripped.startswith(delim):
                end = stripped.find(delim, len(delim))
                if end != -1:
                    after = stripped[end + len(delim):].lstrip("\n")
                    if after.strip():
                        code = after
                        changed = True
                        break

    # Second: if there's a stray `"""` in the text with a def after it,
    # the extraction accidentally captured content inside a docstring.
    # Take the code after the last `"""`.
    for delim in ('"""', "'''"):
        last_pos = code.rfind(delim)
        if last_pos > 0:
            after = code[last_pos + len(delim):].lstrip("\n")
            if after.strip() and re.search(r"\bdef\s+\w+\s*\(", after):
                code = after

    return code


def _trim_code_block(code_lines: list[str]) -> list[str]:
    """Trim trailing prose/explanation from a code block."""
    code_end = len(code_lines)
    consecutive_prose = 0
    for i, line in enumerate(code_lines):
        s = line.strip()
        if not s:
            continue
        if not is_code_line(line) and len(s.split()) > 6:
            consecutive_prose += 1
            if consecutive_prose >= 2:
                code_end = i - consecutive_prose + 1
                break
        else:
            consecutive_prose = 0

    result = code_lines[:code_end]

    # Also trim a single trailing prose line (long explanation at end of code)
    while result:
        last = result[-1].strip()
        if not last:
            result.pop()
            continue
        if not is_code_line(result[-1]) and len(last.split()) > 10:
            result.pop()
            continue
        break

    return result


def extract_code_section(text: str) -> str:
    """Extract the candidate code from a full interview document.

    Strategy:
    1. Look for Candidate Form / code markers
    2. If found, take everything after the marker
    3. Strip trailing prose / explanation
    4. If no marker found, look for code blocks directly
    """
    lines = text.split("\n")

    # Strategy 1: Find a candidate code marker
    marker_line = None
    for i, line in enumerate(lines):
        for pat in CANDIDATE_MARKERS:
            if re.search(pat, line, re.IGNORECASE):
                marker_line = i
                break
        if marker_line is not None:
            break

    if marker_line is not None:
        after = lines[marker_line + 1:]
        # Skip blank lines and non-code lines right after marker
        code_start = None
        for i, line in enumerate(after):
            if is_code_line(line):
                code_start = i
                break
        if code_start is not None:
            code_lines = after[code_start:]
            code_lines = _trim_code_block(code_lines)
            extracted = "\n".join(code_lines).strip()
            extracted = _strip_leading_prose_lines(extracted)
            return extracted

    # Strategy 2: No marker found.
    # If the file looks like pure code (>60% code lines), use it as-is.
    non_blank = [l for l in lines if l.strip()]
    if non_blank:
        code_count = sum(1 for l in non_blank if is_code_line(l))
        if code_count / len(non_blank) > 0.5:
            result = _strip_leading_prose_lines(text.strip())
            return result

    # Strategy 3: Find the first def/class/public and take from there
    for i, line in enumerate(lines):
        s = line.strip()
        if re.match(r"^(def |class |public |private |protected )", s):
            rest = lines[i:]
            rest = _trim_code_block(rest)
            return "\n".join(rest).strip()

    # Fallback: return everything
    return _strip_leading_prose_lines(text.strip())


# ---- Indentation repair ----

def normalize_indentation(code: str) -> str:
    """Fix common indentation issues from copy-paste into Brightspace.

    Handles:
    - Mixed tabs and spaces
    - Completely flat code that should be indented
    - Inconsistent indent levels
    """
    code = code.replace("\r\n", "\n").replace("\r", "\n")

    # Step 1: Normalize tabs to spaces, but be smart about it
    # If code uses tabs consistently, convert tab = 1 indent level
    lines = code.split("\n")
    has_tabs = any("\t" in line for line in lines)
    has_leading_spaces = any(line.startswith("    ") for line in lines if line.strip())

    if has_tabs:
        # Convert tabs to 4 spaces
        lines = [line.replace("\t", "    ") for line in lines]

    # Step 2: Detect flat code (everything at col 0 that should be indented)
    lines = _fix_flat_indentation(lines)

    # Step 3: Normalize inconsistent indent levels
    lines = _normalize_indent_levels(lines)

    return "\n".join(lines)


def _fix_flat_indentation(lines: list[str]) -> list[str]:
    """Detect and fix code where def/class bodies are at the same indent as headers.

    Handles two scenarios:
    A) def body at col 0 but inner blocks already have relative indentation
       (from tab→space conversion): shift all body lines by +4
    B) Completely flat code (everything at col 0 including inner blocks):
       rebuild from block headers
    """
    # Find def/class lines at col 0 whose body starts at col 0
    def_lines = []
    for i, line in enumerate(lines):
        s = line.strip()
        if not s:
            continue
        lead = len(line) - len(line.lstrip())
        if lead == 0 and re.match(r"^(def|class)\b", s) and s.endswith(":"):
            for j in range(i + 1, len(lines)):
                ns = lines[j].strip()
                if ns:
                    next_lead = len(lines[j]) - len(lines[j].lstrip())
                    if next_lead == 0:
                        def_lines.append(i)
                    break

    if not def_lines:
        return lines

    # Check if body lines have ANY existing indentation (scenario A vs B)
    body_has_indent = False
    for i, line in enumerate(lines):
        if i in def_lines:
            continue
        s = line.strip()
        if s:
            lead = len(line) - len(line.lstrip())
            if lead > 0:
                body_has_indent = True
                break

    if body_has_indent:
        # Scenario A: Preserve existing relative indentation, add +4 to body lines.
        # Find ranges of each def's body.
        result = list(lines)
        for di, def_idx in enumerate(def_lines):
            # Body runs from def_idx+1 to next def_line (or EOF)
            body_start = def_idx + 1
            body_end = def_lines[di + 1] if di + 1 < len(def_lines) else len(lines)
            for j in range(body_start, body_end):
                if result[j].strip():
                    result[j] = "    " + result[j]
        return result
    else:
        # Scenario B: Completely flat code — rebuild from block structure.
        result = []
        indent_stack = [0]
        DEDENT_KEYWORDS = {"else:", "elif", "except:", "except", "finally:"}

        for line in lines:
            stripped = line.strip()
            if not stripped:
                result.append("")
                continue

            should_dedent = any(stripped.startswith(kw) for kw in DEDENT_KEYWORDS)
            if should_dedent and len(indent_stack) > 1:
                indent_stack.pop()

            current_indent = indent_stack[-1]
            result.append(" " * current_indent + stripped)

            if stripped.endswith(":") and re.match(
                r"^(def|class|if|elif|else|for|while|try|except|finally|with)\b", stripped
            ):
                indent_stack.append(current_indent + 4)

        return result


def _normalize_indent_levels(lines: list[str]) -> list[str]:
    """Normalize indent levels to consistent 4-space multiples.

    Handles cases like:
    - 2-space indent mixed with 4-space
    - Odd indents (3, 5, 7 spaces)
    """
    indents = set()
    for line in lines:
        if line.strip():
            spaces = len(line) - len(line.lstrip())
            if spaces > 0:
                indents.add(spaces)

    if not indents:
        return lines

    # Find the base indent unit
    sorted_indents = sorted(indents)
    if len(sorted_indents) < 2:
        return lines

    # Check if already 4-space aligned
    if all(i % 4 == 0 for i in sorted_indents):
        return lines

    # Find GCD-like base unit
    diffs = []
    for i in range(1, len(sorted_indents)):
        d = sorted_indents[i] - sorted_indents[i-1]
        if d > 0:
            diffs.append(d)

    if not diffs:
        return lines

    base = min(diffs) if diffs else 4
    if base < 2:
        base = 2

    result = []
    for line in lines:
        if not line.strip():
            result.append("")
            continue
        spaces = len(line) - len(line.lstrip())
        level = round(spaces / base)
        result.append(" " * (level * 4) + line.lstrip())

    return result


def strip_html_entities(text: str) -> str:
    """Remove common HTML entities from Brightspace exports."""
    text = text.replace("&nbsp;", " ")
    text = text.replace("&amp;", "&")
    text = text.replace("&lt;", "<")
    text = text.replace("&gt;", ">")
    text = text.replace("&quot;", '"')
    text = re.sub(r"&#\d+;", "", text)
    return text


# ---- Main ----

def main():
    if not UNZIPPED.exists():
        print(f"ERROR: {UNZIPPED} not found. Unzip the submissions first.")
        return

    # Parse all folders
    students = {}
    for d in sorted(UNZIPPED.iterdir()):
        if not d.is_dir():
            continue
        info = parse_folder_name(d.name)
        if not info:
            continue
        bid, first, last, dt = info
        if bid not in students:
            students[bid] = {"first": first, "last": last, "folders": []}
        students[bid]["folders"].append((dt, d))

    # Pick latest submission per student
    for bid, s in students.items():
        s["folders"].sort(key=lambda x: x[0])
        s["latest_dt"], s["latest_dir"] = s["folders"][-1]

    # Write students.csv
    INPUTS.mkdir(exist_ok=True)
    REPORTS.mkdir(exist_ok=True)
    students_path = INPUTS / "students.csv"
    with open(students_path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["student_id", "FirstName", "LastName"])
        for bid in sorted(students):
            s = students[bid]
            w.writerow([bid, s["first"], s["last"]])
    print(f"Wrote {students_path} ({len(students)} students)")

    # Process each student
    results = []
    for bid in sorted(students):
        s = students[bid]
        latest_dir = s["latest_dir"]

        # Read all files in latest submission
        full_text = ""
        file_methods = []
        has_image_only = True

        for f in sorted(latest_dir.iterdir()):
            if not f.is_file():
                continue
            text, method = read_any_file(f)
            if method != "image" and text.strip():
                has_image_only = False
            if text:
                full_text += text + "\n"
            file_methods.append((f.name, method))

        full_text = strip_html_entities(full_text)

        # Detect language
        lang = detect_language(full_text)

        # Determine file type category
        file_types = [m for _, m in file_methods]
        if all(m == "image" for m in file_types):
            extraction = "image-only"
            status = "manual-review"
        elif any("failed" in (read_any_file(latest_dir / fn)[0]) for fn, _ in file_methods
                  if fn.endswith((".doc", ".pdf", ".docx", ".rtf"))):
            extraction = "partial"
            status = "extracted"
        else:
            extraction = "text"
            status = "extracted"

        # Extract code
        code = ""
        if full_text.strip() and lang != "empty":
            code = extract_code_section(full_text)
            if code:
                code = normalize_indentation(code)

        # Detect problem from extracted CODE first (avoids picking up
        # interviewer's problem), fall back to full text if code gives unknown
        problem = "unknown"
        if code.strip():
            problem = detect_problem(code)
        if problem == "unknown" and full_text.strip():
            problem = detect_problem(full_text)

        if not code.strip():
            if has_image_only:
                status = "manual-review"
            else:
                status = "empty"

        results.append({
            "student_id": bid,
            "first_name": s["first"],
            "last_name": s["last"],
            "problem": problem,
            "detected_language": lang,
            "status": status,
            "extraction": extraction,
            "files": "; ".join(f"{fn} ({m})" for fn, m in file_methods),
            "full_text": full_text,
            "code": code,
        })

    # Organize into problem folders
    problem_dirs = set()
    for r in results:
        p = r["problem"]
        if p == "unknown":
            p = "unknown_problem"
        problem_dirs.add(p)

    for pdir_name in problem_dirs:
        pdir = ROOT / pdir_name
        raw_dir = pdir / "raw"
        code_dir = pdir / "code"
        for d in (pdir, raw_dir, code_dir):
            d.mkdir(exist_ok=True)

    # Write files and manifests
    problem_manifests = defaultdict(list)

    for r in results:
        bid = r["student_id"]
        p = r["problem"] if r["problem"] != "unknown" else "unknown_problem"
        pdir = ROOT / p

        # Write raw (full document)
        if r["full_text"].strip():
            raw_path = pdir / "raw" / f"{bid}.txt"
            raw_path.write_text(r["full_text"], encoding="utf-8")

        # Write extracted code
        if r["code"].strip():
            ext = ".py" if r["detected_language"] in ("python", "pseudocode") else ".java" if r["detected_language"] == "java" else ".txt"
            code_path = pdir / "code" / f"{bid}{ext}"
            code_path.write_text(r["code"], encoding="utf-8")

        problem_manifests[p].append({
            "student_id": bid,
            "first_name": r["first_name"],
            "last_name": r["last_name"],
            "detected_language": r["detected_language"],
            "status": r["status"],
            "extraction": r["extraction"],
            "files": r["files"],
        })

    # Write per-problem manifests
    for p, rows in problem_manifests.items():
        pdir = ROOT / p
        manifest_path = pdir / "manifest.csv"
        with open(manifest_path, "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=[
                "student_id", "first_name", "last_name", "detected_language",
                "status", "extraction", "files"
            ])
            w.writeheader()
            for row in rows:
                w.writerow(row)
        print(f"Wrote {manifest_path} ({len(rows)} students)")

    # Write global manifest
    global_manifest = INPUTS / "manifest.csv"
    with open(global_manifest, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=[
            "student_id", "first_name", "last_name", "problem",
            "detected_language", "status", "extraction", "files"
        ])
        w.writeheader()
        for r in results:
            w.writerow({
                "student_id": r["student_id"],
                "first_name": r["first_name"],
                "last_name": r["last_name"],
                "problem": r["problem"],
                "detected_language": r["detected_language"],
                "status": r["status"],
                "extraction": r["extraction"],
                "files": r["files"],
            })
    print(f"Wrote {global_manifest} ({len(results)} students)")

    # Summary
    print("\n--- Stage 1 Summary ---")
    problem_counts = Counter(r["problem"] for r in results)
    print(f"\nProblem distribution:")
    for p, cnt in problem_counts.most_common():
        print(f"  {p:35s}: {cnt}")

    lang_counts = Counter(r["detected_language"] for r in results)
    print(f"\nLanguage distribution:")
    for l, cnt in lang_counts.most_common():
        print(f"  {l:20s}: {cnt}")

    status_counts = Counter(r["status"] for r in results)
    print(f"\nStatus distribution:")
    for s, cnt in status_counts.most_common():
        print(f"  {s:20s}: {cnt}")

    # Manual review students
    manual = [r for r in results if r["status"] == "manual-review"]
    if manual:
        print(f"\nStudents needing manual review ({len(manual)}):")
        for r in manual:
            print(f"  {r['student_id']} ({r['last_name']}, {r['first_name']}): {r['files']}")


if __name__ == "__main__":
    main()
