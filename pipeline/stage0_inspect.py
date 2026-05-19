"""Stage 0: Inspect unzipped mock-interview submissions and print stats.

Parses folder names for student info + timestamps, inventories file types,
detects which LeetCode problem each student solved, and prints distribution.
Does not modify anything.
"""
import os
import re
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UNZIPPED = ROOT / "mock_raw_unzipped"

FOLDER_RE = re.compile(
    r"^(\d+)-\d+\s*-\s*(.+?)\s*-\s*"
    r"((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2},\s*\d{4}\s+\d{1,2}\d{2}\s*[AP]M)$"
)

PROBLEM_SIGNATURES = {
    "guess_number": {
        "functions": [r"\bguess\s*[Nn]umber\b", r"\bguess\s*\(\s*mid"],
        "titles": [r"[Gg]uess\s+[Nn]umber", r"[Gg]uess\s+[Gg]ame"],
    },
    "longest_substring": {
        "functions": [r"\blengthOfLongestSubstring\b", r"\blength_of_longest_substring\b",
                      r"\blongest[Ss]ubstring\b"],
        "titles": [r"[Ll]ongest\s+[Ss]ubstring", r"[Ww]ithout\s+[Rr]epeating"],
    },
    "contains_nearby_duplicate": {
        "functions": [r"\bcontainsNearbyDuplicate\b", r"\bcontains_nearby_duplicate\b",
                      r"\bnearby[Dd]uplicate\b"],
        "titles": [r"[Cc]ontains\s+[Nn]earby\s+[Dd]uplicate"],
    },
    "merge_two_sorted_lists": {
        "functions": [r"\bmergeTwoLists\b", r"\bmerge_two_lists\b", r"\bmergeTwoList\b",
                      r"\bmergeTwoSortedLists\b"],
        "titles": [r"[Mm]erge\s+[Tt]wo\s+[Ss]orted\s+[Ll]ists?"],
    },
    "eval_rpn": {
        "functions": [r"\bevalRPN\b", r"\beval_rpn\b", r"\breversepolishnotation\b",
                      r"\breverse_polish\b", r"\bevalr?p?n?\b"],
        "titles": [r"[Rr]everse\s+[Pp]olish", r"\bRPN\b"],
    },
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


def read_text_file(path: Path) -> str:
    for enc in ("utf-8", "utf-8-sig", "latin-1", "cp1252"):
        try:
            return path.read_text(encoding=enc)
        except (UnicodeDecodeError, ValueError):
            continue
    return ""


def main():
    if not UNZIPPED.exists():
        print(f"ERROR: {UNZIPPED} not found. Unzip the submissions first.")
        return

    folders = sorted(UNZIPPED.iterdir())
    dirs = [f for f in folders if f.is_dir()]
    print(f"Total submission folders: {len(dirs)}")

    students = {}  # bid -> {first, last, folders: [(dt, path)]}
    unparsed = []
    for d in dirs:
        info = parse_folder_name(d.name)
        if not info:
            unparsed.append(d.name)
            continue
        bid, first, last, dt = info
        if bid not in students:
            students[bid] = {"first": first, "last": last, "folders": []}
        students[bid]["folders"].append((dt, d))

    print(f"Unique students (by Brightspace ID): {len(students)}")
    if unparsed:
        print(f"Unparsed folder names: {unparsed}")

    multi = {bid: s for bid, s in students.items() if len(s["folders"]) > 1}
    print(f"Students with multiple submissions: {len(multi)}")
    for bid, s in sorted(multi.items()):
        times = [dt.strftime("%m/%d %I:%M %p") for dt, _ in s["folders"]]
        print(f"  {bid} ({s['last']}, {s['first']}): {times}")

    # File type inventory
    ext_counter = Counter()
    all_files = []
    for d in dirs:
        for f in d.iterdir():
            if f.is_file():
                ext = f.suffix.lower()
                ext_counter[ext] += 1
                all_files.append(f)

    print(f"\nFile type distribution ({len(all_files)} total files):")
    for ext, cnt in ext_counter.most_common():
        print(f"  {ext or '(no ext)':12s}: {cnt}")

    # For each student (latest submission), detect problem
    problem_counter = Counter()
    lang_counter = Counter()
    problem_students = defaultdict(list)
    for bid, s in sorted(students.items()):
        s["folders"].sort(key=lambda x: x[0])
        latest_dt, latest_dir = s["folders"][-1]
        text_content = ""
        has_code_file = False
        for f in latest_dir.iterdir():
            if f.is_file() and f.suffix.lower() in (".txt", ".py", ".ipynb"):
                text_content += read_text_file(f) + "\n"
                has_code_file = True

        problem = detect_problem(text_content) if text_content.strip() else "unknown"
        problem_counter[problem] += 1
        problem_students[problem].append(f"{bid} ({s['last']}, {s['first']})")

        has_def = bool(re.search(r"\bdef\s+\w+\s*\(", text_content))
        has_java = bool(re.search(r"public\s+\w+\s+\w+\s*\(", text_content))
        has_class = bool(re.search(r"\bclass\s+\w+", text_content))
        if has_def:
            lang = "python"
        elif has_java:
            lang = "java"
        elif text_content.strip():
            lang = "text/pseudocode"
        else:
            lang = "no-text-file"
        lang_counter[lang] += 1

    print(f"\nProblem detection (latest submission, text files only):")
    for problem, cnt in problem_counter.most_common():
        print(f"  {problem:35s}: {cnt}")
        for s in problem_students[problem]:
            print(f"    {s}")

    print(f"\nLanguage detection:")
    for lang, cnt in lang_counter.most_common():
        print(f"  {lang:20s}: {cnt}")

    # Non-text submissions (images, PDFs, DOCs)
    non_text = []
    for bid, s in sorted(students.items()):
        s["folders"].sort(key=lambda x: x[0])
        latest_dt, latest_dir = s["folders"][-1]
        files = list(latest_dir.iterdir())
        text_files = [f for f in files if f.is_file() and f.suffix.lower() in (".txt", ".py", ".ipynb")]
        binary_files = [f for f in files if f.is_file() and f.suffix.lower() in (
            ".pdf", ".doc", ".docx", ".rtf", ".jpeg", ".jpg", ".png", ".heic"
        )]
        if binary_files and not text_files:
            non_text.append((bid, s, [f.name for f in binary_files]))

    if non_text:
        print(f"\nStudents with ONLY non-text files ({len(non_text)}):")
        for bid, s, files in non_text:
            print(f"  {bid} ({s['last']}, {s['first']}): {files}")


if __name__ == "__main__":
    main()
