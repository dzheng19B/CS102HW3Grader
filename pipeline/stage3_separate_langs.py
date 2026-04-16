"""Reorganize fixed/ into python/, java/, pseudocode/ subfolders per problem.

For Java students:
  - Copy raw/<id>.txt → java/<id>.java (minimal repair: ensure class wrapper, close braces)
  - Keep transpiled python in python/<id>.py as a backup
For Python students:
  - Move fixed/<id>.py → python/<id>.py
For Pseudocode students:
  - Copy raw/<id>.txt → pseudocode/<id>.txt
"""
import csv
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROBLEMS = [
    ("problem1", "maxValidWindowSum", "max_valid_window_sum", ["int[] nums", "int k"], "int"),
    ("problem2", "countPairs", "count_pairs", ["int[] nums", "int T"], "int"),
]


def ensure_dirs(pdir):
    for sub in ("python", "java", "pseudocode"):
        (pdir / sub).mkdir(exist_ok=True)


def repair_java(raw: str, java_fn: str, java_params: list[str], ret_type: str) -> tuple[str, list[tuple[str, str]]]:
    """Minimal Java syntax repair. Returns (repaired_code, diff_entries)."""
    diff: list[tuple[str, str]] = []
    s = raw.strip()

    # Strip leading prose
    lines = s.split("\n")
    start = 0
    for i, ln in enumerate(lines):
        stripped = ln.strip()
        if any(stripped.startswith(k) for k in (
            "public", "private", "int ", "long ", "double ", "float ", "boolean ",
            "String ", "for", "if", "while", "return", "{", "}", "//", "/*", "@",
            "class ", "static ", "void ", "import "
        )) or stripped.startswith(f"{java_fn}") or "(" in stripped:
            start = i
            break
    if start > 0:
        diff.append(("[syntax-only]", f"stripped {start} leading prose line(s)"))
    s = "\n".join(lines[start:])

    # Remove trailing prose after last }
    last_brace = s.rfind("}")
    if last_brace != -1:
        trailing = s[last_brace + 1:].strip()
        if trailing:
            diff.append(("[syntax-only]", "stripped trailing prose after last `}`"))
        s = s[:last_brace + 1]

    # Add missing semicolons
    fixed_lines = []
    semi_count = 0
    no_semi = re.compile(r"^\s*(if|else|for|while|do|try|catch|finally|switch|class|public|private|protected)\b")
    for ln in s.split("\n"):
        stripped = ln.rstrip()
        if (stripped and
            not stripped.endswith((";", "{", "}", ":", ",", "//", "*/")) and
            not no_semi.match(stripped) and
            not stripped.lstrip().startswith(("//", "/*", "*")) and
            re.search(r"[\w)\]\"]$", stripped)):
            stripped += ";"
            semi_count += 1
        fixed_lines.append(stripped)
    if semi_count:
        diff.append(("[syntax-only]", f"added missing semicolons ({semi_count} line(s))"))
    s = "\n".join(fixed_lines)

    has_class = bool(re.search(r"\bclass\s+\w+", s))
    has_method = bool(re.search(rf"\b{java_fn}\s*\(", s))

    if not has_method:
        param_str = ", ".join(java_params)
        s = f"    public static {ret_type} {java_fn}({param_str}) {{\n{s}\n    }}"
        has_class = False
        diff.append(("[ambiguous]", f"wrapped code in method signature `{java_fn}({param_str})`"))

    # Fix .length() -> .length
    length_count = len(re.findall(r"\.length\(\)", s))
    if length_count:
        s = re.sub(r"\.length\(\)", ".length", s)
        diff.append(("[syntax-only]", f"fixed `.length()` -> `.length` ({length_count}x)"))

    # Add "return 0;" only when the method body has NO return statement at all
    if re.search(rf"\b{java_fn}\s*\(", s) and not re.search(r"\breturn\b", s):
        last = s.rfind("}")
        if last != -1:
            s = s[:last] + "    return 0;\n" + s[last:]
            diff.append(("[logic-affecting]", "added fallback `return 0;` (no return statement found)"))

    # Balance braces
    opens = s.count("{")
    closes = s.count("}")
    if opens > closes:
        n = opens - closes
        s += "\n}" * n
        diff.append(("[syntax-only]", f"appended {n} missing closing brace(s) `}}`"))
    elif closes > opens:
        n = closes - opens
        s = "{\n" * n + s
        diff.append(("[syntax-only]", f"prepended {n} opening brace(s) `{{` to balance"))

    # Wrap in class if needed
    if not has_class:
        s = f"public class Solution {{\n{s}\n}}"
        diff.append(("[syntax-only]", "wrapped in `public class Solution { ... }`"))

    # Ensure class name is Solution
    m = re.search(r"\bclass\s+(\w+)", s)
    if m and m.group(1) != "Solution":
        diff.append(("[syntax-only]", f"renamed class `{m.group(1)}` -> `Solution`"))
    s = re.sub(r"\bclass\s+\w+", "class Solution", s, count=1)

    if not diff:
        diff.append(("[syntax-only]", "no changes required (parsed as-is)"))

    return s, diff


def process(problem: str, java_fn: str, py_fn: str, java_params: list[str], ret_type: str):
    pdir = ROOT / problem
    ensure_dirs(pdir)
    rows = list(csv.DictReader(open(pdir / "manifest.csv", encoding="utf-8")))

    counts = {"python": 0, "java": 0, "pseudocode": 0, "empty": 0}

    for r in rows:
        sid = r["student_id"]
        lang = r["detected_language"]
        raw_path = ROOT / r["raw_path"]
        fixed_py = pdir / "fixed" / f"{sid}.py"
        diff_md = pdir / "fixed" / f"{sid}.diff.md"

        if lang == "python":
            if fixed_py.exists():
                shutil.copy2(fixed_py, pdir / "python" / f"{sid}.py")
            if diff_md.exists():
                shutil.copy2(diff_md, pdir / "python" / f"{sid}.diff.md")
            counts["python"] += 1

        elif lang == "java":
            if raw_path.exists():
                raw = raw_path.read_text(encoding="utf-8")
                repaired, diff_entries = repair_java(raw, java_fn, java_params, ret_type)
                (pdir / "java" / f"{sid}.java").write_text(repaired, encoding="utf-8")
                # Write diff.md in same format as Python diffs
                diff_lines = [f"# Diff for {sid}", "", "| Tag | Change |", "|---|---|"]
                for tag, msg in diff_entries:
                    diff_lines.append(f"| {tag} | {msg.replace('|', chr(92)+'|')} |")
                (pdir / "java" / f"{sid}.diff.md").write_text(
                    "\n".join(diff_lines) + "\n", encoding="utf-8")
            counts["java"] += 1

        elif lang == "pseudocode":
            if raw_path.exists():
                shutil.copy2(raw_path, pdir / "pseudocode" / f"{sid}.txt")
            counts["pseudocode"] += 1

        elif lang in ("empty", "missing"):
            counts["empty"] += 1

    print(f"=== {problem} ===")
    for k, v in counts.items():
        if v:
            print(f"  {k}: {v}")


def main():
    for problem, java_fn, py_fn, java_params, ret_type in PROBLEMS:
        process(problem, java_fn, py_fn, java_params, ret_type)

    # P3 bonus — just separate by lang, no Java repair needed (unknown problem)
    pdir = ROOT / "problem3_bonus"
    ensure_dirs(pdir)
    rows = list(csv.DictReader(open(pdir / "manifest.csv", encoding="utf-8")))
    for r in rows:
        sid = r["student_id"]
        lang = r["detected_language"]
        raw_path = ROOT / r["raw_path"]
        fixed_py = pdir / "fixed" / f"{sid}.py"
        if lang == "python":
            if fixed_py.exists():
                shutil.copy2(fixed_py, pdir / "python" / f"{sid}.py")
        elif lang == "java":
            if raw_path.exists():
                shutil.copy2(raw_path, pdir / "java" / f"{sid}.txt")
            if fixed_py.exists():
                shutil.copy2(fixed_py, pdir / "python" / f"{sid}.py")
        elif lang == "pseudocode":
            if raw_path.exists():
                shutil.copy2(raw_path, pdir / "pseudocode" / f"{sid}.txt")
    print(f"=== problem3_bonus ===  done")


if __name__ == "__main__":
    main()
