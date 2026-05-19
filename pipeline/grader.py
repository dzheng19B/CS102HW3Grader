"""Grader: run student code against test cases per problem.

Two-pass repair system:
  Pass 1 (lightweight): typo fixes, colon insertion, bracket cleanup, comment conversion
  Pass 2 (aggressive): bracket balancing, conservative re-indent, aggressive re-indent,
                        force-runnable fallback. Logic-affecting changes are flagged.

Java files get mechanical transpilation to Python before grading.

Severity labels (based on logic correctness):
  PASS         — all tests pass
  Minor Error  — right approach, some bugs (>50% tests pass)
  Critical Error — wrong approach or major bugs (<=50% tests pass, or uncompilable)
"""

import ast
import csv
import json
import re
import sys
import threading
from pathlib import Path
from typing import List, Optional

ROOT = Path(__file__).resolve().parent.parent

with open(ROOT / "test_cases.json", encoding="utf-8") as f:
    TEST_CASES = json.load(f)

# ── ListNode infrastructure ──────────────────────────────────────────

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        self.value = val

    def __repr__(self):
        vals, node, seen = [], self, set()
        while node and id(node) not in seen:
            seen.add(id(node))
            vals.append(str(node.val))
            node = node.next
        return "->".join(vals)


def list_to_linked(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    cur = head
    for v in arr[1:]:
        cur.next = ListNode(v)
        cur = cur.next
    return head


def linked_to_list(head):
    result, seen = [], set()
    while head and id(head) not in seen:
        seen.add(id(head))
        result.append(head.val)
        head = head.next
    return result


def make_guess(pick):
    def guess(num):
        if num > pick: return -1
        elif num < pick: return 1
        else: return 0
    return guess


# ── Constants ────────────────────────────────────────────────────────

KEYWORD_FIXES = {
    r"\bretrun\b": "return", r"\bresturn\b": "return", r"\bretrn\b": "return",
    r"\brteurn\b": "return", r"\bpritn\b": "print", r"\bprnit\b": "print",
    r"\belseif\b": "elif", r"\belse if\b": "elif",
    r"\bFasle\b": "False", r"\bNull\b": "None", r"\bnull\b": "None",
    r"\bNULL\b": "None", r"\bture\b": "True", r"\bflase\b": "False",
    r"\btrue\b": "True", r"\bfalse\b": "False",
}

NEEDS_COLON = re.compile(
    r"^(\s*)(if|elif|else|for|while|def|class|try|except|finally|with)\b([^\n:#]*?)\s*$"
)

FUNCTION_NAME_VARIANTS = {
    "guess_number": ["guessNumber", "guessnumber", "guess_number", "guessNum", "guessingGame", "guessing_game"],
    "longest_substring": ["lengthOfLongestSubstring", "lengthoflongestsubstring", "lengthofLongestSubstring",
                          "lengthOfLongestSubString", "longestSubstring", "longest_substring"],
    "contains_nearby_duplicate": ["containsNearbyDuplicate", "containsnearbyduplicate",
                                  "contains_nearby_duplicate", "containsDuplicate"],
    "merge_two_sorted_lists": ["mergeTwoLists", "mergetwolists", "merge_two_lists",
                               "mergeTwoSortedLists", "mergetwolist", "mergeTwoList"],
    "eval_rpn": ["evalRPN", "evalrpn", "eval_rpn", "evalPRN", "exalRPN",
                 "reversepolishnotation", "evaluateRPN", "rpn"],
}

PROBLEM_DISPLAY = {
    "guess_number": "Guess Number Higher or Lower",
    "longest_substring": "Longest Substring Without Repeating Characters",
    "contains_nearby_duplicate": "Contains Nearby Duplicate",
    "merge_two_sorted_lists": "Merge Two Sorted Lists",
    "eval_rpn": "Evaluate Reverse Polish Notation",
}

EXPECTED_PARAMS = {
    "guess_number": ["n"],
    "longest_substring": ["s"],
    "contains_nearby_duplicate": ["nums", "k"],
    "merge_two_sorted_lists": ["list1", "list2"],
    "eval_rpn": ["tokens"],
}


# ═══════════════════════════════════════════════════════════════════════
#  PASS 1: Lightweight repair
# ═══════════════════════════════════════════════════════════════════════

def extract_function_block(code, problem):
    lines = code.split("\n")
    variants = FUNCTION_NAME_VARIANTS.get(problem, [])
    start = None
    for i, line in enumerate(lines):
        for v in variants:
            if re.search(rf"\bdef\s+{re.escape(v)}\s*\(", line, re.IGNORECASE):
                start = i
                break
        if start is not None:
            break
    if start is None:
        return code
    def_indent = len(lines[start]) - len(lines[start].lstrip())
    end = len(lines)
    for i in range(start + 1, len(lines)):
        stripped = lines[i].strip()
        if not stripped:
            continue
        indent = len(lines[i]) - len(lines[i].lstrip())
        if indent <= def_indent and not stripped.startswith("#"):
            if re.match(r"(def |class |[A-Z]|print\(|[a-z]+\s*:)", stripped):
                end = i
                break
            if not stripped.startswith("return") and indent < def_indent:
                end = i
                break
    return "\n".join(lines[start:end])


def repair_syntax(code):
    changes = []
    code = code.replace("\r\n", "\n").replace("\r", "\n").replace("\t", "    ")

    if " " in code:
        code = code.replace(" ", "\n")
        changes.append("[syntax-only] Replaced Unicode line separator")

    # // comments
    new_lines = []
    for line in code.split("\n"):
        stripped = line.lstrip()
        if stripped.startswith("//"):
            indent = line[:len(line) - len(stripped)]
            new_lines.append(indent + "#" + stripped[2:])
            if not changes or "// to #" not in changes[-1]:
                changes.append("[syntax-only] Converted // comments to #")
        else:
            new_lines.append(line)
    code = "\n".join(new_lines)

    if "-->" in code:
        code = code.replace("-->", "->")
        changes.append("[syntax-only] Fixed --> to ->")

    for pat in [r"\bDef\b", r"\bFor\b", r"\bIf\b", r"\bElif\b", r"\bElse\b",
                r"\bWhile\b", r"\bReturn\b", r"\bAnd\b", r"\bOr\b", r"\bNot\b"]:
        keyword = pat[2:-2]
        if re.search(pat, code):
            code = re.sub(pat, keyword.lower(), code)
            changes.append(f"[syntax-only] Lowered keyword '{keyword}'")

    if "–" in code or "—" in code:
        code = code.replace("–", "-").replace("—", "-")
        changes.append("[syntax-only] Replaced em/en dashes with hyphens")

    for sq in ["‘", "’"]: code = code.replace(sq, "'")
    for dq in ["“", "”"]: code = code.replace(dq, '"')

    for pat, repl in KEYWORD_FIXES.items():
        if re.search(pat, code):
            code = re.sub(pat, repl, code)
            changes.append(f"[syntax-only] Fixed typo -> '{repl}'")

    if "||" in code:
        code = code.replace("||", " or ")
        changes.append("[syntax-only] Replaced || with or")
    if "&&" in code:
        code = code.replace("&&", " and ")
        changes.append("[syntax-only] Replaced && with and")

    lines = code.split("\n")
    new_lines, semi_fixed = [], False
    for line in lines:
        stripped = line.rstrip()
        if stripped.endswith(";") and not stripped.endswith(";;"):
            new_lines.append(stripped[:-1])
            semi_fixed = True
        else:
            new_lines.append(line)
    if semi_fixed:
        changes.append("[syntax-only] Removed trailing semicolons")
    code = "\n".join(new_lines)

    code = re.sub(r"(\S)\s+O\([^)]*\)\s*(#.*)?$", r"\1 \2", code, flags=re.MULTILINE)

    code_stripped = code.rstrip()
    while code_stripped and code_stripped[-1] in "]}" and not _is_balanced(code_stripped):
        code_stripped = code_stripped[:-1].rstrip()
        changes.append("[syntax-only] Removed stray bracket at EOF")
    code = code_stripped + "\n"

    code = re.sub(r"def\s+(\w+)\s*\((?:int|String|float|bool|char)\s+(\w+)", r"def \1(\2", code)

    code = re.sub(
        r"^(\s*def\s+\w+\s*\([^)]*\)\s*(?:->\s*\w+(?:\[[^\]]*\])?)?)\s*$",
        r"\1:", code, flags=re.MULTILINE)

    lines = code.split("\n")
    new_lines, colon_fixed = [], False
    for line in lines:
        if NEEDS_COLON.match(line):
            new_lines.append(line.rstrip() + ":")
            colon_fixed = True
        else:
            new_lines.append(line)
    if colon_fixed:
        changes.append("[syntax-only] Added missing colons")
    code = "\n".join(new_lines)

    if re.search(r"\)\s*\{", code):
        code = re.sub(r"\)\s*\{", "):", code)
        code = re.sub(r"^\s*\}\s*$", "", code, flags=re.MULTILINE)
        changes.append("[syntax-only] Removed C-style braces")

    code = re.sub(r":\s*in\b(?!\s)", ": int", code)

    code_stripped = code.rstrip()
    if code_stripped.endswith('"""') or code_stripped.endswith("'''"):
        q = code_stripped[-3:]
        if code_stripped.count(q) % 2 == 1:
            code = code_stripped[:-3].rstrip() + "\n"
            changes.append("[syntax-only] Removed trailing triple-quote")

    lines = code.split("\n")
    new_lines = []
    for line in lines:
        opens = line.count("(") - line.count(")")
        if opens > 0 and not line.rstrip().endswith(")"):
            new_lines.append(line.rstrip() + ")" * opens)
        else:
            new_lines.append(line)
    code = "\n".join(new_lines)

    lines = code.split("\n")
    while lines and lines[-1].strip():
        words = lines[-1].strip().split()
        if len(words) > 5 and all(w.isalpha() or w in ".,;:!?()-" for w in words):
            lines.pop()
        else:
            break
    code = "\n".join(lines)

    return code, changes


def _is_balanced(code):
    d_sq = d_cur = 0
    for ch in code:
        if ch == "[": d_sq += 1
        elif ch == "]": d_sq -= 1
        elif ch == "{": d_cur += 1
        elif ch == "}": d_cur -= 1
    return d_sq >= 0 and d_cur >= 0


# ═══════════════════════════════════════════════════════════════════════
#  PASS 2: Aggressive repair (from stage2_repair.py)
# ═══════════════════════════════════════════════════════════════════════

def _count_leading(s):
    i = 0
    while i < len(s) and s[i] == " ":
        i += 1
    return i


def balance_brackets(s):
    changes = []
    opens = {"(": 0, "[": 0, "{": 0}
    close_map = {")": "(", "]": "[", "}": "{"}
    in_str = None
    i = 0
    while i < len(s):
        c = s[i]
        if in_str:
            if c == "\\" and i + 1 < len(s):
                i += 2
                continue
            if c == in_str:
                in_str = None
        else:
            if c in ("'", '"'):
                if s[i:i+3] in ('"""', "'''"):
                    end = s.find(s[i:i+3], i + 3)
                    if end == -1: break
                    i = end + 3
                    continue
                in_str = c
            elif c == "#":
                nl = s.find("\n", i)
                if nl == -1: break
                i = nl
                continue
            elif c in opens:
                opens[c] += 1
            elif c in close_map:
                opens[close_map[c]] -= 1
        i += 1
    tail = ""
    for bracket, close in [("{", "}"), ("[", "]"), ("(", ")")]:
        if opens[bracket] > 0:
            tail += close * opens[bracket]
    if tail:
        changes.append(f"[syntax-only] Appended {len(tail)} missing closing bracket(s)")
        s = s.rstrip() + tail + "\n"
    return s, changes


def conservative_reindent(s):
    lines = s.split("\n")
    indents = sorted({_count_leading(ln) for ln in lines if ln.strip()})
    if not indents or indents == [0]:
        return s
    clusters = [[indents[0]]]
    for x in indents[1:]:
        if x - clusters[-1][-1] <= 2:
            clusters[-1].append(x)
        else:
            clusters.append([x])
    mapping = {}
    tier = 0
    if clusters[0][0] == 0:
        for x in clusters[0]: mapping[x] = 0
        tier = 1
        start = 1
    else:
        start = 0
    for cl in clusters[start:]:
        for x in cl: mapping[x] = tier * 4
        tier += 1
    out = []
    for ln in lines:
        if not ln.strip():
            out.append("")
            continue
        orig = _count_leading(ln)
        out.append(" " * mapping.get(orig, orig) + ln.strip())
    return "\n".join(out)


DEDENT_STARTS = ("else", "elif", "except", "finally")


def aggressive_reindent(s):
    lines = s.split("\n")
    out = []
    stack = [0]
    inside_fn = False

    for raw_line in lines:
        stripped = raw_line.strip()
        if not stripped:
            out.append("")
            continue
        if any(stripped.startswith(k + " ") or stripped == k + ":" or stripped.startswith(k + ":")
               for k in DEDENT_STARTS):
            if len(stack) > 1: stack.pop()
            indent = stack[-1]
            out.append(" " * indent + stripped)
            if stripped.endswith(":"): stack.append(indent + 4)
            continue
        if stripped.startswith("def "):
            out.append(stripped)
            stack = [0]
            stack.append(4)
            inside_fn = True
            continue
        indent = stack[-1] if inside_fn else 0
        out.append(" " * indent + stripped)
        if stripped.endswith(":"):
            stack.append(indent + 4)
    return "\n".join(out)


def force_runnable(s, fn_name, params):
    notes = []
    code = s
    for _ in range(40):
        try:
            ast.parse(code)
            return code, notes
        except SyntaxError as e:
            if "expected an indented block" in str(e.msg):
                lineno = e.lineno or 1
                lines = code.split("\n")
                header_idx = None
                for i in range(min(lineno, len(lines)) - 1, -1, -1):
                    if lines[i].rstrip().endswith(":"):
                        header_idx = i
                        break
                if header_idx is None: break
                indent = _count_leading(lines[header_idx])
                lines.insert(header_idx + 1, " " * (indent + 4) + "pass")
                notes.append(f"[logic-affecting] Inserted `pass` into empty block at line {header_idx + 1}")
                code = "\n".join(lines)
            else:
                break

    if fn_name:
        stub_params = ", ".join(params or [])
        stub = f"def {fn_name}({stub_params}):\n    return 0\n"
        notes.append(f"[logic-affecting] Replaced unparseable code with stub `def {fn_name}({stub_params}): return 0`")
        return stub, notes
    return None, notes


def aggressive_repair(code, problem):
    """Pass 2: aggressive repair. Returns (code, changes, used_aggressive)."""
    changes = []
    fn_name = TEST_CASES[problem]["function"]
    params = EXPECTED_PARAMS.get(problem, [])

    # Balance brackets
    code, bc = balance_brackets(code)
    changes.extend(bc)

    if _try_parse(code):
        return code, changes, bool(bc)

    # Conservative reindent
    code_c = conservative_reindent(code)
    if code_c != code:
        changes.append("[ambiguous] Conservative re-indent: normalized indent levels to 4-space tiers")
    if _try_parse(code_c):
        return code_c, changes, True

    # Aggressive reindent
    code_a = aggressive_reindent(code_c)
    if code_a != code_c:
        changes.append("[ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers")
    if _try_parse(code_a):
        return code_a, changes, True

    # Force-runnable fallback
    code_f, fnotes = force_runnable(code_a, fn_name, params)
    if code_f is not None:
        changes.extend(fnotes)
        if _try_parse(code_f):
            return code_f, changes, True

    return code_a, changes, True


def _try_parse(code):
    try:
        ast.parse(code)
        return True
    except SyntaxError:
        return False


# ═══════════════════════════════════════════════════════════════════════
#  Java → Python transpile (from stage2_repair.py)
# ═══════════════════════════════════════════════════════════════════════

def java_to_python(raw, fn_name):
    changes = ["[syntax-only] Mechanical Java->Python transpile"]
    s = raw.replace("\r\n", "\n").replace("\r", "\n")
    s = re.sub(r"/\*.*?\*/", "", s, flags=re.DOTALL)
    s = re.sub(r"<[A-Za-z0-9_,\s?]+>", "", s)

    lines = s.split("\n")
    out_lines = []
    depth = 0

    for raw_line in lines:
        line = re.sub(r"//.*$", "", raw_line)
        stripped = line.strip()
        if not stripped: continue

        if stripped in ("}", "};", "});", "})"):
            depth = max(0, depth - 1)
            continue
        if stripped.startswith("}"):
            depth = max(0, depth - 1)
            stripped = stripped[1:].strip()
            if not stripped: continue

        has_open = False
        if stripped.endswith("{"):
            stripped = stripped[:-1].strip()
            has_open = True

        if stripped.endswith(";"):
            stripped = stripped[:-1].rstrip()
        if not stripped:
            if has_open: depth += 1
            continue

        line_out = _transpile_java_line(stripped, fn_name)
        out_lines.append("    " * depth + line_out)
        if has_open: depth += 1

    code = "\n".join(out_lines)
    return code, changes


def _transpile_java_line(s, fn_name):
    # Method signature
    sig_re = re.compile(r"^(?:public|private|protected)\s+(?:static\s+)?(?:final\s+)?[\w<>\[\]]+\s+(\w+)\s*\(([^)]*)\)\s*$")
    m = sig_re.match(s)
    if m:
        name, param_str = m.group(1), m.group(2)
        new_params = []
        for p in [x.strip() for x in param_str.split(",") if x.strip()]:
            parts = p.split()
            new_params.append(parts[-1].replace("[]", ""))
        py_name = fn_name or name
        return f"def {py_name}({', '.join(new_params)}):"

    # for (int i=...; i<N; i++)
    m = re.match(r"^for\s*\(\s*(?:int\s+|long\s+)?(\w+)\s*=\s*([^;]+);\s*(\w+)\s*([<>]=?)\s*([^;]+);\s*([^)]+)\)\s*$", s)
    if m:
        var, a, _, cmp, b, step = m.groups()
        a, b = a.strip(), b.strip()
        if cmp == "<=": b = f"({b}) + 1"
        if step.strip() in (f"{var}++", f"++{var}"):
            return f"for {var} in range({a}, {b}):"
        return f"for {var} in range({a}, {b}):"

    # for (Type x : arr)
    m = re.match(r"^for\s*\(\s*(?:\w+(?:\[\])?\s+)?(\w+)\s*:\s*(.+)\)\s*$", s)
    if m:
        return f"for {m.group(1)} in {m.group(2).strip()}:"

    # if/while
    m = re.match(r"^(if|while)\s*\((.*)\)\s*$", s)
    if m: return f"{m.group(1)} {m.group(2).strip()}:"
    m = re.match(r"^else\s+if\s*\((.*)\)\s*$", s)
    if m: return f"elif {m.group(1).strip()}:"
    if s.strip() == "else": return "else:"

    # Strip type declarations
    s = re.sub(r"^(int|long|double|float|boolean|String|char|var)(?:\[\])?\s+", "", s)

    # Java idioms
    s = re.sub(r"(\w+)\+\+", r"\1 += 1", s)
    s = re.sub(r"(\w+)--", r"\1 -= 1", s)
    s = re.sub(r"(\w+)\.length\b", r"len(\1)", s)
    s = re.sub(r"(\w+)\.equals\(([^)]+)\)", r"\1 == \2", s)
    s = re.sub(r"(\w+)\.push\(", r"\1.append(", s)
    s = re.sub(r"(\w+)\.peek\(\)", r"\1[-1]", s)
    s = re.sub(r"(\w+)\.charAt\((\w+)\)", r"\1[\2]", s)
    s = re.sub(r"(\w+)\.size\(\)", r"len(\1)", s)
    s = re.sub(r"(\w+)\.isEmpty\(\)", r"len(\1) == 0", s)
    s = re.sub(r"\bnew\s+\w+(?:\[\])?\s*\([^)]*\)", "[]", s)
    s = re.sub(r"\bnew\s+\w+\[\]\s*\{([^}]*)\}", r"[\1]", s)
    s = re.sub(r"\bMath\.max\b", "max", s)
    s = re.sub(r"\bMath\.min\b", "min", s)
    s = re.sub(r"\bMath\.abs\b", "abs", s)
    s = re.sub(r"\bSystem\.out\.(?:println|print)\s*\(", "print(", s)
    s = re.sub(r"\bInteger\.parseInt\(([^)]+)\)", r"int(\1)", s)
    s = re.sub(r"(\w+)\.parseInt\(\)", r"int(\1)", s)
    s = re.sub(r"\bInteger\.MAX_VALUE\b", "float('inf')", s)
    s = re.sub(r"\bInteger\.MIN_VALUE\b", "float('-inf')", s)
    s = re.sub(r"\btrue\b", "True", s)
    s = re.sub(r"\bfalse\b", "False", s)
    s = re.sub(r"\bnull\b", "None", s)
    s = s.replace("&&", " and ").replace("||", " or ")
    # Ternary
    s = re.sub(r"([^?\n]+?)\s*\?\s*([^:\n]+?)\s*:\s*([^\n]+)", r"(\2 if \1 else \3)", s)
    # != null
    s = re.sub(r"(\w+)\s*!=\s*None", r"\1 is not None", s)
    s = re.sub(r"(\w+)\s*==\s*None", r"\1 is None", s)

    return s


# ═══════════════════════════════════════════════════════════════════════
#  Code transforms
# ═══════════════════════════════════════════════════════════════════════

def unwrap_class_solution(code):
    if not re.search(r"^\s*class\s+Solution", code, re.MULTILINE):
        return code
    lines = code.split("\n")
    new_lines, inside = [], False
    for line in lines:
        if re.match(r"^\s*class\s+Solution", line):
            inside = True
            continue
        if inside:
            if line.startswith("    "): new_lines.append(line[4:])
            elif line.startswith("\t"): new_lines.append(line[1:])
            elif line.strip() == "": new_lines.append("")
            else: new_lines.append(line)
        else:
            new_lines.append(line)
    return "\n".join(new_lines)


def strip_self_param(code):
    code = re.sub(r"def\s+(\w+)\s*\(\s*self\s*,\s*", r"def \1(", code)
    code = re.sub(r"def\s+(\w+)\s*\(\s*self\s*\)", r"def \1()", code)
    return code


def strip_self_calls(code, problem):
    for v in FUNCTION_NAME_VARIANTS.get(problem, []):
        code = code.replace(f"self.{v}(", f"{v}(")
    return code


def strip_student_guess_def(code):
    has_guess = bool(re.search(r"^\s*def\s+guess\s*\(", code, re.MULTILINE))
    has_gN = bool(re.search(r"^\s*def\s+guessNumber\s*\(", code, re.MULTILINE))
    if not has_guess: return code
    if has_gN:
        lines, new_lines, skip = code.split("\n"), [], None
        for line in lines:
            if skip is not None:
                stripped = line.lstrip()
                indent = len(line) - len(stripped)
                if stripped == "" or indent > skip: continue
                else: skip = None
            if re.match(r"^\s*def\s+guess\s*\(", line):
                skip = len(line) - len(line.lstrip())
                continue
            new_lines.append(line)
        return "\n".join(new_lines)
    else:
        return re.sub(r"def\s+guess\s*\(", "def guessNumber(", code, count=1)


def strip_trailing_calls(code):
    lines, new_lines = code.split("\n"), []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("print(") and not line.startswith((" ", "\t")): continue
        if re.match(r"^[a-zA-Z_]\w*\(.*\)\s*$", stripped) and not line.startswith((" ", "\t")): continue
        new_lines.append(line)
    return "\n".join(new_lines)


def strip_from_import(code):
    return re.sub(r"^\s*from\s+typing\s+import\s+.*$", "", code, flags=re.MULTILINE)


def find_function(code_text, problem):
    variants = FUNCTION_NAME_VARIANTS.get(problem, [])
    canonical = TEST_CASES[problem]["function"]
    for name in variants:
        if re.search(rf"\bdef\s+{re.escape(name)}\s*\(", code_text):
            return name
        m = re.search(rf"def\s+(\w+)\s*\(", code_text)
        if m and m.group(1).lower() == name.lower():
            return m.group(1)
    for m in re.finditer(r"def\s+(\w+)\s*\(", code_text):
        if m.group(1).lower() in [v.lower() for v in variants]:
            return m.group(1)
    return canonical


# ═══════════════════════════════════════════════════════════════════════
#  Execution
# ═══════════════════════════════════════════════════════════════════════

def run_with_timeout(func, args, timeout=5):
    result, error = [None], [None]
    def target():
        try: result[0] = func(*args)
        except Exception as e: error[0] = f"{type(e).__name__}: {e}"
    t = threading.Thread(target=target, daemon=True)
    t.start()
    t.join(timeout)
    if t.is_alive(): return None, "TimeoutError: exceeded 5s"
    return result[0], error[0]


def build_exec_env(problem):
    return {
        "__builtins__": __builtins__,
        "List": List, "Optional": Optional, "optional": Optional,
        "ListNode": ListNode, "listNode": ListNode, "Listnode": ListNode,
        "listnode": ListNode, "new_node": ListNode,
        "int": int, "str": str, "bool": bool, "float": float,
        "len": len, "range": range, "abs": abs, "max": max, "min": min,
        "sum": sum, "enumerate": enumerate, "sorted": sorted,
        "set": set, "dict": dict, "list": list, "tuple": tuple,
        "map": map, "filter": filter, "zip": zip,
        "print": lambda *a, **kw: None,
        "math": __import__("math"), "collections": __import__("collections"),
    }


# ═══════════════════════════════════════════════════════════════════════
#  Severity classification
# ═══════════════════════════════════════════════════════════════════════

OPTIMAL_APPROACHES = {
    "guess_number": "Binary search O(log n)",
    "longest_substring": "Sliding window O(n)",
    "contains_nearby_duplicate": "Hash map O(n)",
    "merge_two_sorted_lists": "Iterative merge O(n+m)",
    "eval_rpn": "Stack O(n)",
}


def detect_optimal(code, problem):
    code_lower = code.lower()
    if problem == "guess_number":
        if re.search(r"\bfor\s+\w+\s+in\s+range\s*\(\s*1?\s*,?\s*n", code_lower):
            return False, "Linear scan instead of binary search"
        if "mid" in code_lower or "//" in code or ">> 1" in code or "low" in code_lower:
            return True, None
        if re.search(r"while.*<.*:", code_lower) and ("+" in code or "-" in code):
            return True, None
        return True, None

    if problem == "longest_substring":
        for_count = len(re.findall(r"\bfor\b", code_lower))
        if for_count >= 2:
            return False, "Nested loops instead of sliding window"
        return True, None

    if problem == "contains_nearby_duplicate":
        for_count = len(re.findall(r"\bfor\b", code_lower))
        if for_count >= 2 and not re.search(r"\bdict\b|\bset\b|\{\}", code):
            return False, "Nested loops instead of hash map"
        return True, None

    if problem == "merge_two_sorted_lists":
        if re.search(r"\.sort\s*\(|sorted\s*\(", code):
            return False, "Using sort() instead of iterative merge"
        return True, None

    if problem == "eval_rpn":
        if "stack" in code_lower or "append" in code_lower or re.search(r"\[\s*\]", code):
            return True, None
        return True, None

    return True, None


def classify_severity(result):
    """Assign severity label based on logic correctness."""
    status = result["status"]

    if status in ("java-skip", "pseudocode-skip", "empty", "read-error"):
        return None  # not applicable

    if status in ("compile-error", "exec-error", "no-function"):
        return "Critical Error"

    if status == "graded":
        if result["passed"] == result["total"]:
            return None  # PASS, no error
        ratio = result["passed"] / result["total"] if result["total"] > 0 else 0
        if ratio > 0.5:
            return "Minor Error"
        else:
            return "Critical Error"

    return None


# ═══════════════════════════════════════════════════════════════════════
#  Grade student
# ═══════════════════════════════════════════════════════════════════════

def grade_student(problem, code_path, is_java=False):
    sid = code_path.stem
    ext = code_path.suffix

    result = {
        "student_id": sid, "problem": problem, "file": code_path.name,
        "compile": None, "tests": [], "passed": 0, "total": 0,
        "status": None, "changes": [], "error": None,
        "repair_level": "none", "severity": None,
        "optimal": True, "optimal_note": None,
    }

    try:
        raw_code = code_path.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        result["status"] = "read-error"
        result["error"] = str(e)
        result["severity"] = classify_severity(result)
        return result

    if not raw_code.strip():
        result["status"] = "empty"
        result["error"] = "Empty file"
        result["severity"] = classify_severity(result)
        return result

    # ── Java transpile ──
    if ext == ".java" or is_java:
        fn_name = TEST_CASES[problem]["function"]
        code, transpile_changes = java_to_python(raw_code, fn_name)
        result["changes"].extend(transpile_changes)
        result["repair_level"] = "java-transpile"
    else:
        code = raw_code

    # ── Pass 1: Lightweight repair ──
    code = strip_from_import(code)
    code = unwrap_class_solution(code)
    code = strip_self_param(code)
    code = strip_self_calls(code, problem)
    code = strip_trailing_calls(code)
    if problem == "guess_number":
        code = strip_student_guess_def(code)
    code, changes = repair_syntax(code)
    result["changes"].extend(changes)

    func_name = find_function(code, problem)

    # Try extracting function block if full code doesn't parse
    if not _try_parse(code):
        extracted = extract_function_block(code, problem)
        if extracted != code:
            code = extracted
            if problem == "guess_number":
                code = strip_student_guess_def(code)
            code, extra = repair_syntax(code)
            result["changes"].extend(extra)
            result["changes"].append("[syntax-only] Extracted function block from noisy file")
            func_name = find_function(code, problem)

    if _try_parse(code):
        if result["repair_level"] == "none":
            result["repair_level"] = "lightweight"
    else:
        # ── Pass 2: Aggressive repair ──
        code_agg, agg_changes, _ = aggressive_repair(code, problem)
        result["changes"].extend(agg_changes)
        if _try_parse(code_agg):
            code = code_agg
            result["repair_level"] = "aggressive"
            func_name = find_function(code, problem)
        else:
            # Still broken
            try:
                ast.parse(code_agg)
            except SyntaxError as e:
                result["compile"] = f"SyntaxError: line {e.lineno}: {e.msg}"
            result["status"] = "compile-error"
            result["error"] = result["compile"] or "Unparseable after all repairs"
            result["repair_level"] = "aggressive"
            result["severity"] = classify_severity(result)
            return result

    result["compile"] = "ok"
    is_opt, opt_note = detect_optimal(code, problem)
    result["optimal"] = is_opt
    result["optimal_note"] = opt_note

    # ── Execute ──
    env = build_exec_env(problem)
    if problem == "guess_number":
        env["guess"] = make_guess(1)

    try:
        exec(code, env)
    except Exception as e:
        result["compile"] = f"ExecError: {type(e).__name__}: {e}"
        result["status"] = "exec-error"
        result["error"] = result["compile"]
        result["severity"] = classify_severity(result)
        return result

    func = env.get(func_name) or env.get(TEST_CASES[problem]["function"])
    if func is None:
        for name in FUNCTION_NAME_VARIANTS.get(problem, []):
            if name in env and callable(env[name]):
                func = env[name]
                break

    if func is None:
        result["status"] = "no-function"
        result["error"] = f"Function '{func_name}' not found after exec"
        result["severity"] = classify_severity(result)
        return result

    # ── Run tests ──
    cases = TEST_CASES[problem]["cases"]
    result["total"] = len(cases)

    for case in cases:
        tr = {"name": case["name"], "expected": case["expected"],
              "actual": None, "passed": False, "error": None}
        try:
            args = prepare_args(problem, case, env)
            actual, err = run_with_timeout(func, args)
            if err:
                tr["error"] = err
            else:
                actual = normalize_output(problem, actual)
                tr["actual"] = actual
                tr["passed"] = (actual == case["expected"])
                if tr["passed"]: result["passed"] += 1
        except Exception as e:
            tr["error"] = f"{type(e).__name__}: {e}"
        result["tests"].append(tr)

    result["status"] = "graded"
    result["severity"] = classify_severity(result)
    return result


def prepare_args(problem, case, env):
    if problem == "guess_number":
        env["guess"] = make_guess(case["args"]["pick"])
        return [case["args"]["n"]]
    elif problem == "merge_two_sorted_lists":
        return [list_to_linked(case["args"][0]), list_to_linked(case["args"][1])]
    elif problem == "contains_nearby_duplicate":
        return [list(case["args"][0]), case["args"][1]]
    elif problem == "longest_substring":
        return [case["args"][0]]
    elif problem == "eval_rpn":
        return [list(case["args"][0])]
    return case["args"]


def normalize_output(problem, actual):
    if problem == "merge_two_sorted_lists":
        if actual is None: return []
        if isinstance(actual, ListNode): return linked_to_list(actual)
        return actual
    if problem == "eval_rpn":
        if isinstance(actual, float): return int(actual)
        return actual
    if problem == "contains_nearby_duplicate":
        return bool(actual) if actual is not None else actual
    if actual is not None and isinstance(actual, float) and actual == int(actual):
        return int(actual)
    return actual


# ═══════════════════════════════════════════════════════════════════════
#  Main
# ═══════════════════════════════════════════════════════════════════════

def _print(s):
    try: print(s)
    except UnicodeEncodeError: print(s.encode("ascii", errors="replace").decode("ascii"))


def load_manifest():
    manifest = {}
    with open(ROOT / "inputs" / "manifest.csv", newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            manifest[row["student_id"]] = row
    return manifest


def grade_all():
    manifest = load_manifest()
    assigned = {sid: row["problem"] for sid, row in manifest.items()}
    all_results = []

    for problem in ["guess_number", "longest_substring", "contains_nearby_duplicate",
                    "merge_two_sorted_lists", "eval_rpn"]:
        code_dir = ROOT / problem / "code"
        if not code_dir.exists(): continue

        print(f"\n{'='*60}")
        print(f"  Grading: {problem}")
        print(f"{'='*60}")

        for code_file in sorted(code_dir.iterdir()):
            if code_file.suffix not in (".py", ".java"): continue
            sid = code_file.stem
            if assigned.get(sid) != problem: continue

            m_row = manifest.get(sid, {})
            name = f"{m_row.get('first_name','')} {m_row.get('last_name','')}"

            is_java = code_file.suffix == ".java" or m_row.get("detected_language") == "java"
            result = grade_student(problem, code_file, is_java=is_java)
            all_results.append(result)

            sev = f" [{result['severity']}]" if result.get("severity") else ""
            rl = f" ({result['repair_level']})" if result["repair_level"] not in ("none", "lightweight") else ""

            if result["status"] == "graded":
                score = f"{result['passed']}/{result['total']}"
                failed = [t["name"] for t in result["tests"] if not t["passed"]]
                if failed:
                    _print(f"  {sid} {name:30s} {score}{sev}{rl}  FAILED: {', '.join(failed)}")
                else:
                    _print(f"  {sid} {name:30s} {score}  ALL PASS{rl}")
            else:
                _print(f"  {sid} {name:30s} {result['status']:15s}{sev}{rl} {(result.get('error') or '')[:50]}")

    return all_results


def write_results_csv(results):
    out = ROOT / "reports" / "grading_results.csv"
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["student_id", "problem", "file", "compile", "status",
                     "passed", "total", "score_pct", "failed_tests", "error",
                     "changes", "repair_level", "severity", "optimal", "optimal_note"])
        for r in results:
            failed = "; ".join(t["name"] for t in r["tests"] if not t["passed"])
            pct = f"{r['passed']/r['total']*100:.0f}" if r["total"] > 0 else ""
            w.writerow([
                r["student_id"], r["problem"], r["file"], r["compile"],
                r["status"], r["passed"], r["total"], pct,
                failed, r["error"] or "", "; ".join(r["changes"]),
                r.get("repair_level", ""), r.get("severity", ""),
                r.get("optimal", ""), r.get("optimal_note", ""),
            ])
    print(f"\nResults CSV: {out}")


def write_grading_report(results):
    manifest_rows = load_manifest()
    lines = []
    w = lines.append

    w("# Mock Technical Interview - Grading Report")
    w("")
    from datetime import datetime
    w(f"> Generated {datetime.now().strftime('%Y-%m-%d %H:%M')}  ")
    graded = [r for r in results if r["status"] == "graded"]
    w(f"> {len(graded)} graded, "
      f"{sum(1 for r in graded if r['passed']==r['total'])} all-pass, "
      f"{sum(1 for r in results if r.get('severity')=='Minor Error')} minor errors, "
      f"{sum(1 for r in results if r.get('severity')=='Critical Error')} critical errors, "
      f"{sum(1 for r in results if r['status'] in ('compile-error','exec-error'))} compile errors after repair")
    w("")

    w("## How to read this report")
    w("")
    w("- **PASS**: all tests pass")
    w("- **Minor Error**: right approach, some bugs (>50% tests pass)")
    w("- **Critical Error**: wrong approach or major logic bugs (<=50% tests pass), or uncompilable after all repair attempts")
    w("- **Repair level**: `lightweight` = basic syntax fixes only; `aggressive` = re-indentation / bracket balancing / force-runnable (flagged changes may affect logic); `java-transpile` = mechanical Java-to-Python conversion")
    w("")

    w("## Summary")
    w("")
    w("| # | Student | Problem | Score | Severity | Optimal | Repair | Failed Tests |")
    w("|--:|---------|---------|------:|----------|---------|--------|--------------|")

    def sort_key(r):
        m = manifest_rows.get(r["student_id"], {})
        name = f"{m.get('last_name','?')}, {m.get('first_name','?')}".lower()
        is_pass = 0 if (r["status"] == "graded" and r["passed"] == r["total"]) else 1
        return (r["problem"], is_pass, name)

    results_sorted = sorted(results, key=sort_key)
    for i, r in enumerate(results_sorted, 1):
        m = manifest_rows.get(r["student_id"], {})
        name = f"{m.get('last_name','?')}, {m.get('first_name','?')}"
        prob = PROBLEM_DISPLAY.get(r["problem"], r["problem"])
        sev = r.get("severity") or ("PASS" if r["status"] == "graded" and r["passed"] == r["total"] else r["status"])
        rl = r.get("repair_level", "")
        opt = "Yes" if r.get("optimal", True) else f"No - {r.get('optimal_note', '')}"
        if r["status"] == "graded":
            score = f"{r['passed']}/{r['total']}"
            failed = ", ".join(t["name"] for t in r["tests"] if not t["passed"])
        else:
            score = "-"
            failed = (r.get("error") or "")[:40]
        w(f"| {i} | {name} | {prob} | {score} | {sev} | {opt} | {rl} | {failed} |")
    w("")

    w("---")
    w("")
    w("## Student Details")
    w("")

    current_problem = None
    for r in results_sorted:
        if r["problem"] != current_problem:
            current_problem = r["problem"]
            w(f"### {PROBLEM_DISPLAY.get(current_problem, current_problem)}")
            w("")

        m = manifest_rows.get(r["student_id"], {})
        name = f"{m.get('first_name','?')} {m.get('last_name','?')}"
        sev = r.get("severity")

        w(f"#### {name} (`{r['student_id']}`)")
        w("")
        if sev:
            w(f"- **Severity: {sev}**")
        elif r["status"] == "graded" and r["passed"] == r["total"]:
            w(f"- **PASS**")
        else:
            w(f"- **Status:** {r['status']}")
        if r["status"] == "graded":
            w(f"- **Score:** {r['passed']}/{r['total']}")
        if not r.get("optimal", True):
            w(f"- **Not optimal:** {r.get('optimal_note', 'Sub-optimal approach')}")
        if r.get("repair_level") and r["repair_level"] not in ("none", "lightweight"):
            w(f"- **Repair level:** {r['repair_level']}")
        if r["error"]:
            w(f"- **Error:** `{r['error']}`")
        w("")

        if r["tests"]:
            w("| Test | Expected | Actual | Result |")
            w("|------|----------|--------|--------|")
            for t in r["tests"]:
                exp = _fmt(t["expected"])
                act = _fmt(t["actual"]) if t["error"] is None else f"ERROR: {t['error'][:40]}"
                mark = "PASS" if t["passed"] else "FAIL"
                w(f"| {t['name']} | {exp} | {act} | {mark} |")
            w("")

        # Flag logic-affecting changes
        logic_changes = [c for c in r["changes"] if "[logic-affecting]" in c or "[ambiguous]" in c]
        if logic_changes:
            w("**Warning: potentially logic-affecting changes were applied:**")
            w("")
            for c in logic_changes:
                w(f"- {c}")
            w("")

        if r["changes"]:
            w("<details>")
            w("<summary>All syntax changes made</summary>")
            w("")
            for c in r["changes"]:
                w(f"- {c}")
            w("")
            w("</details>")
            w("")

        code_path = ROOT / r["problem"] / "code" / r["file"]
        if code_path.exists():
            code = code_path.read_text(encoding="utf-8", errors="replace")
            lang = "java" if r["file"].endswith(".java") else "python"
            w("<details>")
            w(f"<summary>Student Code ({r['file']})</summary>")
            w("")
            w(f"```{lang}")
            w(code.rstrip())
            w("```")
            w("")
            w("</details>")
            w("")

        w("---")
        w("")

    report_text = "\n".join(lines)
    out = ROOT / "reports" / "grading_report.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(report_text, encoding="utf-8")
    print(f"Grading report: {out} ({len(report_text):,} chars)")


def _fmt(val):
    if val is None: return "None"
    if isinstance(val, bool): return str(val)
    if isinstance(val, list) and len(str(val)) > 30: return str(val)[:27] + "..."
    return str(val)


if __name__ == "__main__":
    results = grade_all()
    write_results_csv(results)
    write_grading_report(results)
