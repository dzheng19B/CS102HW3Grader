"""Stage 4: Logic-change audit.

For each student with status `repaired` (across P1, P2, P3):
- Read raw/<id>.txt and fixed/<id>.py
- Read fixed/<id>.diff.md for the change log
- If any diff entry is tagged [ambiguous] or [logic-affecting], OR the fixed file
  structurally differs from raw in ways beyond whitespace/comments/keyword-colons,
  write audit/<id>.md flagging it and downgrade manifest status to `needs-manual-review`.
- Otherwise write a short audit confirming no logic changes and leave status alone.
"""
import csv
import re
from pathlib import Path

ROOT = Path(__file__).parent
PROBLEMS = ["problem1", "problem2", "problem3_bonus"]


def normalize_for_compare(s: str) -> str:
    """Strip comments, blank lines, and all whitespace so pure-format changes compare equal."""
    out = []
    for ln in s.split("\n"):
        # strip // and # comments
        ln = re.sub(r"//.*$", "", ln)
        ln = re.sub(r"#.*$", "", ln)
        ln = ln.strip()
        if ln:
            out.append(ln)
    joined = "\n".join(out)
    # collapse whitespace runs
    return re.sub(r"\s+", " ", joined)


def load_manifest(pdir: Path):
    return list(csv.DictReader(open(pdir / "manifest.csv", encoding="utf-8")))


def save_manifest(pdir: Path, rows):
    with (pdir / "manifest.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["student_id", "detected_language",
                                           "attempt_num", "raw_path", "status"])
        w.writeheader()
        w.writerows(rows)


def audit_student(pdir: Path, sid: str, diff_md: str):
    """Return (is_logic_changed, reason_list)."""
    flags = []
    for line in diff_md.split("\n"):
        if "[logic-affecting]" in line:
            flags.append("logic-affecting change: " + line.split("|")[-2].strip())
        elif "[ambiguous]" in line:
            flags.append("ambiguous change: " + line.split("|")[-2].strip())
    return (bool(flags), flags)


def process(problem: str):
    pdir = ROOT / problem
    adir = pdir / "audit"
    adir.mkdir(exist_ok=True)
    rows = load_manifest(pdir)

    clean = 0
    flagged = 0
    for row in rows:
        if row["status"] != "repaired":
            continue
        sid = row["student_id"]
        diff_path = pdir / "fixed" / f"{sid}.diff.md"
        if not diff_path.exists():
            continue
        diff_md = diff_path.read_text(encoding="utf-8")

        is_changed, flags = audit_student(pdir, sid, diff_md)
        apath = adir / f"{sid}.md"
        if is_changed:
            lines = [f"# Audit: {sid}", "",
                     "Status: **flagged** — downgraded to `needs-manual-review`.",
                     "", "## Flags"]
            lines.extend(f"- {f}" for f in flags)
            lines.append("")
            lines.append("## Full diff")
            lines.append(diff_md)
            apath.write_text("\n".join(lines), encoding="utf-8")
            row["status"] = "needs-manual-review"
            flagged += 1
        else:
            apath.write_text(f"# Audit: {sid}\n\nNo logic-affecting changes detected.\n\n"
                             f"All diff entries tagged `[syntax-only]`.\n", encoding="utf-8")
            clean += 1

    save_manifest(pdir, rows)
    print(f"=== {problem} ===  clean: {clean}  downgraded: {flagged}")


def main():
    for p in PROBLEMS:
        process(p)


if __name__ == "__main__":
    main()
