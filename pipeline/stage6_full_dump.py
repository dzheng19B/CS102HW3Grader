"""Stage 6: write a single continuous markdown with every student's full data.

Per student:
  Problem 1 — raw, fixed, diff
  Problem 2 — raw, fixed, diff
  Problem 3 — raw code (if any)
  Score summary across all problems
  Visible separator
"""
import csv
import difflib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "pipeline"))
from hints import hint_for
INPUTS = ROOT / "inputs"
REPORTS = ROOT / "reports"
REPORTS.mkdir(exist_ok=True)
OUT = REPORTS / "all_students_full.md"
SEP = "\n\n" + "=" * 100 + "\n\n"


def roster():
    return {r["student_id"]: f"{r['FirstName']} {r['LastName']}"
            for r in csv.DictReader(open(INPUTS / "students.csv", encoding="utf-8"))}


def manifest_map(problem):
    return {r["student_id"]: r for r in csv.DictReader(
        open(ROOT / problem / "manifest.csv", encoding="utf-8"))}


def read_or_blank(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="replace")


def code_block(text: str, lang: str = "", numbered: bool = True) -> str:
    text = text.rstrip("\n")
    if not text:
        return "_(empty)_"
    if numbered:
        lines = text.split("\n")
        width = len(str(len(lines)))
        text = "\n".join(f"{i:>{width}} | {ln}" for i, ln in enumerate(lines, 1))
        lang = ""  # disable syntax highlighting since prefix would mis-tokenize
    fence = "```"
    while fence in text:
        fence += "`"
    return f"{fence}{lang}\n{text}\n{fence}"


def section_problem(problem: str, sid: str, manifest_row: dict | None) -> list[str]:
    pdir = ROOT / problem
    out = []
    if manifest_row is None:
        out.append("_(student not in this problem's manifest)_")
        return out

    lang = manifest_row["detected_language"]
    status = manifest_row["status"]
    out.append(f"- **detected language:** `{lang}`")
    out.append(f"- **status:** `{status}`")
    out.append(f"- **attempt #:** {manifest_row['attempt_num']}")
    out.append("")

    raw = read_or_blank(pdir / "raw" / f"{sid}.txt")

    if lang == "java":
        repaired = read_or_blank(pdir / "java" / f"{sid}.java")
        diff = read_or_blank(pdir / "java" / f"{sid}.diff.md")
        from_label, to_label = "raw", "java (repaired)"
    else:
        repaired = read_or_blank(pdir / "fixed" / f"{sid}.py")
        diff = read_or_blank(pdir / "fixed" / f"{sid}.diff.md")
        from_label, to_label = "raw", "fixed"

    out.append("**Diff:**")
    out.append("")
    out.append(diff.strip() if diff.strip() else "_(no diff file)_")
    out.append("")
    out.append(f"<details><summary><b>Highlighted changes {from_label} → {to_label} (click to expand)</b></summary>")
    out.append("")
    if raw.strip() or repaired.strip():
        udiff = list(difflib.unified_diff(
            raw.splitlines(), repaired.splitlines(),
            fromfile=from_label, tofile=to_label, lineterm="", n=2,
        ))
        if udiff:
            out.append("```diff")
            out.extend(udiff)
            out.append("```")
        else:
            out.append("_(no textual difference)_")
    else:
        out.append("_(empty)_")
    out.append("")
    out.append("</details>")
    out.append("")
    out.append("**Raw extracted input:**")
    out.append("")
    out.append(code_block(raw))
    out.append("")
    if lang == "java":
        out.append("**Java source (repaired):**")
        out.append("")
        out.append(code_block(repaired))
        return out

    out.append("**Fixed input:**")
    out.append("")
    out.append(code_block(repaired))
    return out


def _format_result(d: dict) -> str:
    passed = d.get("tests_passed", 0)
    failed = d.get("tests_failed", 0)
    total = passed + failed
    score = round(20 * passed / total, 2) if total else 0
    err = (d.get("load_error") or "").strip()
    base = f"{score}/20  ({passed}/{total} tests passed)"
    if err:
        base += f"  — load error: {err.splitlines()[0][:120]}"
    return base


def score_for(problem: str, sid: str, lang: str = "python") -> str:
    if lang == "java":
        java_path = ROOT / problem / "results" / f"{sid}_java.json"
        if java_path.exists():
            return _format_result(json.load(open(java_path, encoding="utf-8")))
    py_path = ROOT / problem / "results" / f"{sid}.json"
    if py_path.exists():
        return _format_result(json.load(open(py_path, encoding="utf-8")))
    return "no results"


def get_score(problem: str, sid: str, lang: str) -> float:
    """Return numeric score (0-20) for sorting."""
    if lang == "java":
        p = ROOT / problem / "results" / f"{sid}_java.json"
        if p.exists():
            d = json.load(open(p, encoding="utf-8"))
            total = d.get("tests_passed", 0) + d.get("tests_failed", 0)
            return round(20 * d.get("tests_passed", 0) / total, 2) if total else 0.0
    p = ROOT / problem / "results" / f"{sid}.json"
    if p.exists():
        d = json.load(open(p, encoding="utf-8"))
        total = d.get("tests_passed", 0) + d.get("tests_failed", 0)
        return round(20 * d.get("tests_passed", 0) / total, 2) if total else 0.0
    return 0.0


def needs_review(sid: str, p1m: dict, p2m: dict) -> bool:
    for m in (p1m, p2m):
        row = m.get(sid)
        if row and row["status"] in ("needs-manual-review", "unrepairable"):
            return True
    return False


def main():
    names = roster()
    p1m = manifest_map("problem1")
    p2m = manifest_map("problem2")
    p3m = manifest_map("problem3_bonus")
    all_ids = sorted(set(p1m) | set(p2m) | set(p3m))

    # Sort: highest combined score first, then needs-manual-review students last
    def sort_key(sid):
        review = needs_review(sid, p1m, p2m)
        p1_lang = p1m[sid]["detected_language"] if sid in p1m else "python"
        p2_lang = p2m[sid]["detected_language"] if sid in p2m else "python"
        p1_score = get_score("problem1", sid, p1_lang)
        p2_score = get_score("problem2", sid, p2_lang)
        combined = p1_score + p2_score
        # Primary: non-review before review (False=0 < True=1)
        # Secondary: higher combined score first (negate for descending)
        return (review, -combined, sid)

    all_ids = sorted(all_ids, key=sort_key)

    parts = ["# All Students — Full Submission Dump",
             "",
             f"_{len(all_ids)} students. Ordered by combined score (highest first); "
             "students needing manual review are listed at the end._",
             ""]

    for sid in all_ids:
        name = names.get(sid, "?")
        block = []
        block.append(f"# {sid} — {name}")
        block.append("")
        block.append("## Problem 1 — Maximum Valid Window Sum")
        block.append("")
        block.extend(section_problem("problem1", sid, p1m.get(sid)))
        block.append("")
        block.append("## Problem 2 — Count Valid Pairs With Constraint")
        block.append("")
        block.extend(section_problem("problem2", sid, p2m.get(sid)))
        block.append("")
        block.append("## Problem 3 — Bonus (LeetCode POTD)")
        block.append("")
        if p3m.get(sid):
            p3_lang = p3m[sid]["detected_language"]
            p3_status = p3m[sid]["status"]
            block.append(f"- **detected language:** `{p3_lang}`")
            block.append(f"- **status:** `{p3_status}`")
            block.append("")
            block.append("**Raw bonus code:**")
            block.append("")
            block.append(code_block(read_or_blank(ROOT / "problem3_bonus" / "raw" / f"{sid}.txt")))
        else:
            block.append("_(not in P3 manifest)_")
        block.append("")
        p1_lang = p1m[sid]["detected_language"] if sid in p1m else "python"
        p2_lang = p2m[sid]["detected_language"] if sid in p2m else "python"

        block.append("## Potential Mistake & Suggestion")
        block.append("")
        h1 = hint_for("problem1", sid, p1_lang) if sid in p1m else ""
        h2 = hint_for("problem2", sid, p2_lang) if sid in p2m else ""
        if h1:
            block.append("**Problem 1:**")
            block.append("")
            block.append(h1)
            block.append("")
        if h2:
            block.append("**Problem 2:**")
            block.append("")
            block.append(h2)
            block.append("")
        if not h1 and not h2:
            block.append("_All auto-graded tests passed (or no results to analyze)._")
            block.append("")

        block.append("## Score Summary")
        block.append("")
        block.append(f"- **Problem 1:** {score_for('problem1', sid, p1_lang)}")
        block.append(f"- **Problem 2:** {score_for('problem2', sid, p2_lang)}")
        block.append(f"- **Problem 3:** manual grade (LeetCode POTD varies per student)")

        parts.append("\n".join(block))

    OUT.write_text(SEP.join(parts) + "\n", encoding="utf-8")
    print(f"Wrote {OUT}  ({OUT.stat().st_size:,} bytes, {len(all_ids)} students)")


if __name__ == "__main__":
    main()
