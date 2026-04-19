"""Generate 3 per-topic report files from the same data as all_students_full.md:
  - problem1_report.md — Problem 1 only (diff, raw, fixed/java, score)
  - problem2_report.md — Problem 2 only
  - pseudocode_report.md — All pseudocode submissions across both problems
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
SEP = "\n\n" + "=" * 100 + "\n\n"


def roster():
    return {r["student_id"]: f"{r['FirstName']} {r['LastName']}"
            for r in csv.DictReader(open(INPUTS / "students.csv", encoding="utf-8"))}


def manifest_map(problem):
    return {r["student_id"]: r for r in csv.DictReader(
        open(ROOT / problem / "manifest.csv", encoding="utf-8"))}


def read_or_blank(path):
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def code_block(text, numbered=True):
    text = text.rstrip("\n")
    if not text:
        return "_(empty)_"
    if numbered:
        lines = text.split("\n")
        w = len(str(len(lines)))
        text = "\n".join(f"{i:>{w}} | {ln}" for i, ln in enumerate(lines, 1))
    fence = "```"
    while fence in text:
        fence += "`"
    return f"{fence}\n{text}\n{fence}"


def get_score(problem, sid, lang):
    if lang == "java":
        p = ROOT / problem / "results" / f"{sid}_java.json"
        if p.exists():
            d = json.load(open(p, encoding="utf-8"))
            t = d.get("tests_passed", 0) + d.get("tests_failed", 0)
            return round(20 * d.get("tests_passed", 0) / t, 2) if t else 0.0
    p = ROOT / problem / "results" / f"{sid}.json"
    if p.exists():
        d = json.load(open(p, encoding="utf-8"))
        t = d.get("tests_passed", 0) + d.get("tests_failed", 0)
        return round(20 * d.get("tests_passed", 0) / t, 2) if t else 0.0
    return 0.0


def format_score(problem, sid, lang):
    if lang == "java":
        p = ROOT / problem / "results" / f"{sid}_java.json"
    else:
        p = ROOT / problem / "results" / f"{sid}.json"
    if not p.exists():
        return "no results"
    d = json.load(open(p, encoding="utf-8"))
    passed = d.get("tests_passed", 0)
    failed = d.get("tests_failed", 0)
    total = passed + failed
    score = round(20 * passed / total, 2) if total else 0
    err = (d.get("load_error") or "").strip()
    base = f"{score}/20  ({passed}/{total} tests passed)"
    if err:
        base += f"  -- {err.splitlines()[0][:120]}"
    return base


def build_problem_section(problem, sid, manifest_row):
    pdir = ROOT / problem
    out = []
    if manifest_row is None:
        out.append("_(no submission)_")
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
        from_l, to_l = "raw", "java (repaired)"
    else:
        repaired = read_or_blank(pdir / "fixed" / f"{sid}.py")
        diff = read_or_blank(pdir / "fixed" / f"{sid}.diff.md")
        from_l, to_l = "raw", "fixed"

    out.append("**Diff:**")
    out.append("")
    out.append(diff.strip() if diff.strip() else "_(no diff file)_")
    out.append("")

    out.append(f"<details><summary><b>Highlighted changes {from_l} → {to_l} (click to expand)</b></summary>")
    out.append("")
    if raw.strip() or repaired.strip():
        udiff = list(difflib.unified_diff(
            raw.splitlines(), repaired.splitlines(),
            fromfile=from_l, tofile=to_l, lineterm="", n=2))
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
    else:
        out.append("**Fixed input:**")
        out.append("")
        out.append(code_block(repaired))

    out.append("")
    out.append("**Potential Mistake & Suggestion:**")
    out.append("")
    h = hint_for(problem, sid, lang)
    out.append(h if h else "_All auto-graded tests passed (or no results to analyze)._")
    out.append("")
    out.append(f"**Score:** {format_score(problem, sid, lang)}")
    return out


def write_problem_report(problem, title, out_name):
    names = roster()
    pm = manifest_map(problem)
    ids = sorted(pm.keys())

    def sort_key(sid):
        row = pm[sid]
        review = row["status"] in ("needs-manual-review", "unrepairable")
        lang = row["detected_language"]
        score = get_score(problem, sid, lang)
        return (review, -score, sid)

    ids = sorted(ids, key=sort_key)

    parts = [f"# {title}",
             "",
             f"_{len(ids)} students. Ordered by score (highest first); "
             "students needing manual review at the end._",
             ""]

    for sid in ids:
        row = pm[sid]
        name = names.get(sid, "?")
        block = [f"# {sid} — {name}", ""]
        block.extend(build_problem_section(problem, sid, row))
        parts.append("\n".join(block))

    out_path = REPORTS / out_name
    out_path.write_text(SEP.join(parts) + "\n", encoding="utf-8")
    print(f"Wrote {out_path}  ({out_path.stat().st_size:,} bytes, {len(ids)} students)")


def write_pseudocode_report():
    names = roster()
    p1m = manifest_map("problem1")
    p2m = manifest_map("problem2")

    parts = ["# Pseudocode Submissions",
             "",
             "_Students who submitted pseudocode for Problem 1 and/or Problem 2. "
             "These require manual grading._",
             ""]

    count = 0
    seen = set()
    for problem, pm, title in [("problem1", p1m, "Problem 1 — Maximum Valid Window Sum"),
                                ("problem2", p2m, "Problem 2 — Count Valid Pairs With Constraint")]:
        for sid, row in sorted(pm.items()):
            if row["detected_language"] != "pseudocode":
                continue
            name = names.get(sid, "?")
            raw = read_or_blank(ROOT / problem / "raw" / f"{sid}.txt")
            block = [f"# {sid} — {name}", "", f"## {title}", ""]
            block.append(code_block(raw))
            parts.append("\n".join(block))
            count += 1
            seen.add(sid)

    out_path = REPORTS / "pseudocode_report.md"
    out_path.write_text(SEP.join(parts) + "\n", encoding="utf-8")
    print(f"Wrote {out_path}  ({out_path.stat().st_size:,} bytes, {count} entries from {len(seen)} students)")


def main():
    write_problem_report("problem1", "Problem 1 — Maximum Valid Window Sum", "problem1_report.md")
    write_problem_report("problem2", "Problem 2 — Count Valid Pairs With Constraint", "problem2_report.md")
    write_pseudocode_report()


if __name__ == "__main__":
    main()
