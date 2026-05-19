"""Generate combined extraction + grading report for mock technical interview."""

import csv
import json
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PROBLEM_DISPLAY = {
    "guess_number": "Guess Number Higher or Lower",
    "longest_substring": "Longest Substring Without Repeating Characters",
    "contains_nearby_duplicate": "Contains Nearby Duplicate",
    "merge_two_sorted_lists": "Merge Two Sorted Lists",
    "eval_rpn": "Evaluate Reverse Polish Notation",
    "unknown_problem": "Unknown / Undetected",
}

STATUS_EMOJI = {
    "graded": "",
    "compile-error": "",
    "exec-error": "",
    "java-skip": "",
    "pseudocode-skip": "",
    "no-function": "",
    "empty": "",
    "manual-review": "",
    "extracted": "",
}


def load_manifest():
    rows = []
    with open(ROOT / "inputs" / "manifest.csv", newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            rows.append(r)
    return rows


def load_grading_results():
    path = ROOT / "reports" / "grading_results.csv"
    if not path.exists():
        return {}
    results = {}
    with open(path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            key = (r["student_id"], r["problem"])
            results[key] = r
    return results


OPTIMAL_APPROACHES = {
    "guess_number": "Binary search O(log n)",
    "longest_substring": "Sliding window O(n)",
    "contains_nearby_duplicate": "Hash map O(n)",
    "merge_two_sorted_lists": "Iterative merge O(n+m)",
    "eval_rpn": "Stack O(n)",
}


def load_grading_details():
    """Load full grading details from the grader's JSON output if available."""
    # Re-run grader inline to get full test details
    try:
        from pipeline.grader import grade_all
    except ImportError:
        return {}
    return {}


def read_file(path):
    if not path.exists():
        return None
    return path.read_text(encoding="utf-8", errors="replace")


def escape_md(text):
    return text.replace("|", "\\|").replace("\n", " ")


def generate_report():
    rows = load_manifest()
    rows.sort(key=lambda r: (r["problem"], r["last_name"].lower(), r["first_name"].lower()))
    grading = load_grading_results()

    # --- stats ---
    problem_counts = {}
    lang_counts = {}
    for r in rows:
        p = r["problem"]
        problem_counts[p] = problem_counts.get(p, 0) + 1
        lang = r["detected_language"]
        lang_counts[lang] = lang_counts.get(lang, 0) + 1

    # Grading stats
    total_graded = sum(1 for g in grading.values() if g["status"] == "graded")
    total_pass = sum(1 for g in grading.values()
                     if g["status"] == "graded" and g["passed"] == g["total"])
    total_compile = sum(1 for g in grading.values()
                        if g["status"] in ("compile-error", "exec-error"))
    total_minor = sum(1 for g in grading.values() if g.get("severity") == "Minor Error")
    total_critical = sum(1 for g in grading.values() if g.get("severity") == "Critical Error")
    total_not_optimal = sum(1 for g in grading.values() if g.get("optimal") == "False")

    lines = []
    w = lines.append

    # ── Header ──
    w("# Mock Technical Interview - Full Report")
    w("")
    w(f"> Generated {datetime.now().strftime('%Y-%m-%d %H:%M')}  ")
    w(f"> {len(rows)} students | {total_graded} graded | {total_pass} all-pass | "
      f"{total_minor} minor errors | {total_critical} critical errors | "
      f"{total_compile} compile errors | {total_not_optimal} non-optimal solutions")
    w("")

    # ── How to read ──
    w("## How to read this report")
    w("")
    w("- **Summary table**: one row per student with problem, language, score, severity, and optimality.")
    w("- **Per-student sections**: test results (if graded), syntax changes, extracted code, and original document.")
    w("- **Score**: `passed/total` test cases. A dash means the code could not be graded.")
    w("- **Severity**: `PASS` = all tests pass; `Minor Error` = right approach, some bugs (>50% pass); "
      "`Critical Error` = wrong approach or major bugs (<=50% pass or uncompilable).")
    w("- **Optimal**: whether the student used the expected optimal algorithm. "
      f"Expected approaches: {'; '.join(f'{PROBLEM_DISPLAY.get(k,k)}: {v}' for k,v in OPTIMAL_APPROACHES.items())}.")
    w("")

    # ── Distribution ──
    w("## Distribution")
    w("")
    w("| Problem | Students |")
    w("|---------|--------:|")
    for p in ["guess_number", "longest_substring", "contains_nearby_duplicate",
              "merge_two_sorted_lists", "eval_rpn", "unknown_problem"]:
        if p in problem_counts:
            w(f"| {PROBLEM_DISPLAY.get(p, p)} | {problem_counts[p]} |")
    w(f"| **Total** | **{len(rows)}** |")
    w("")

    w("| Language | Count |")
    w("|----------|------:|")
    for lang in sorted(lang_counts):
        w(f"| {lang} | {lang_counts[lang]} |")
    w("")

    # ── Summary table (sorted: PASS first, then FAIL, alphabetically within each) ──
    w("## Summary")
    w("")
    w("| # | Student | Question | Score | Severity | Optimal | Failed Tests |")
    w("|--:|---------|----------|------:|----------|---------|--------------|")

    def summary_sort_key(r):
        key = (r["student_id"], r["problem"])
        g = grading.get(key)
        name = f"{r['last_name']}, {r['first_name']}".lower()
        is_pass = 0 if (g and g["status"] == "graded" and g["passed"] == g["total"]) else 1
        return (r["problem"], is_pass, name)

    rows_sorted = sorted(rows, key=summary_sort_key)

    for i, r in enumerate(rows_sorted, 1):
        name = f"{r['last_name']}, {r['first_name']}"
        prob = PROBLEM_DISPLAY.get(r["problem"], r["problem"])
        key = (r["student_id"], r["problem"])
        g = grading.get(key)

        if g and g["status"] == "graded":
            score = f"{g['passed']}/{g['total']}"
            sev = g.get("severity") or "PASS"
            failed = g.get("failed_tests", "")
        elif g:
            score = "-"
            sev = g.get("severity") or g["status"]
            failed = (g.get("error") or "")[:40]
        elif r["problem"] == "unknown_problem":
            score = "-"
            sev = "unknown-problem"
            failed = ""
        else:
            score = "-"
            sev = r["status"]
            failed = ""

        opt = "Yes" if not g or g.get("optimal", "True") != "False" else f"No - {g.get('optimal_note', '')}"
        w(f"| {i} | {escape_md(name)} | {escape_md(prob)} | {score} | {sev} | {opt} | {failed} |")
    w("")

    # ── Per-student detail ──
    w("---")
    w("")
    w("## Student Details")
    w("")

    current_problem = None
    for r in rows:
        if r["problem"] != current_problem:
            current_problem = r["problem"]
            w(f"### {PROBLEM_DISPLAY.get(current_problem, current_problem)}")
            w("")

        sid = r["student_id"]
        name = f"{r['first_name']} {r['last_name']}"
        prob_dir = r["problem"] if r["problem"] != "unknown_problem" else "unknown_problem"
        key = (sid, r["problem"])
        g = grading.get(key)

        w(f"#### {name} (`{sid}`)")
        w("")

        # Metadata
        w(f"- **Problem:** {PROBLEM_DISPLAY.get(r['problem'], r['problem'])}")
        w(f"- **Language:** {r['detected_language']}")
        if g and g["status"] == "graded":
            sev = g.get("severity") or "PASS"
            w(f"- **Score:** {g['passed']}/{g['total']} ({sev})")
            w(f"- **Grading status:** graded")
            if g.get("optimal") == "False":
                w(f"- **Not optimal:** {g.get('optimal_note', 'Sub-optimal approach')}")
            if g.get("repair_level") and g["repair_level"] not in ("none", "lightweight"):
                w(f"- **Repair level:** {g['repair_level']}")
        elif g:
            w(f"- **Grading status:** {g['status']}")
            if g.get("severity"):
                w(f"- **Severity:** {g['severity']}")
            if g.get("error"):
                w(f"- **Error:** `{g['error']}`")
        else:
            w(f"- **Extraction status:** {r['status']}")
        w(f"- **Files:** {r['files']}")
        w("")

        # Test results table (from grading CSV)
        if g and g["status"] == "graded":
            failed_tests = g.get("failed_tests", "")
            total = int(g["total"]) if g["total"] else 0
            passed = int(g["passed"]) if g["passed"] else 0

            # Load test case names from test_cases.json for this problem
            tc_path = ROOT / "test_cases.json"
            if tc_path.exists() and r["problem"] in ("guess_number", "longest_substring",
                                                       "contains_nearby_duplicate",
                                                       "merge_two_sorted_lists", "eval_rpn"):
                with open(tc_path, encoding="utf-8") as f:
                    tc = json.load(f)
                cases = tc.get(r["problem"], {}).get("cases", [])
                failed_set = set(t.strip() for t in failed_tests.split(";") if t.strip())

                w("| Test Case | Result |")
                w("|-----------|--------|")
                for c in cases:
                    mark = "FAIL" if c["name"] in failed_set else "PASS"
                    w(f"| {c['name']} | {mark} |")
                w("")

        # Syntax changes
        if g and g.get("changes"):
            changes_list = [c.strip() for c in g["changes"].split(";") if c.strip()]
            if changes_list:
                w("<details>")
                w("<summary>Edits made by grader</summary>")
                w("")
                for c in changes_list:
                    w(f"- {c}")
                w("")
                w("</details>")
                w("")

        # Extracted code
        code_ext = ".java" if r["detected_language"] == "java" else ".py"
        code_path = ROOT / prob_dir / "code" / f"{sid}{code_ext}"
        code = read_file(code_path)

        if code and code.strip():
            lang_hint = "java" if r["detected_language"] == "java" else "python"
            w("<details>")
            w(f"<summary>Extracted Code ({code_path.name})</summary>")
            w("")
            w(f"```{lang_hint}")
            w(code.rstrip())
            w("```")
            w("")
            w("</details>")
            w("")
        else:
            w("*No code extracted.*")
            w("")

        # Original raw document
        raw_path = ROOT / prob_dir / "raw" / f"{sid}.txt"
        raw = read_file(raw_path)

        if raw and raw.strip():
            w("<details>")
            w(f"<summary>Original Document ({raw_path.name})</summary>")
            w("")
            w("```")
            w(raw.rstrip())
            w("```")
            w("")
            w("</details>")
            w("")
        else:
            w("*No raw document available.*")
            w("")

        w("---")
        w("")

    return "\n".join(lines)


if __name__ == "__main__":
    report = generate_report()
    out = ROOT / "reports" / "extraction_report.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(report, encoding="utf-8")
    print(f"Report written to {out} ({len(report):,} chars)")
