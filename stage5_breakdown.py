"""Stage 5: human-readable breakdown of every student's score.

Produces `score_breakdown.md` — one section per student, with:
- roster name
- P1/P2 scores
- brief explanation: status, common error/failure pattern, notable flags
- P3 bonus status (submitted / pseudocode / empty / needs-review)
"""
import csv
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).parent


def load_roster():
    return {r["student_id"]: f"{r['FirstName']} {r['LastName']}"
            for r in csv.DictReader(open(ROOT / "students.csv", encoding="utf-8"))}


def load_manifest(problem: str):
    return {r["student_id"]: r for r in csv.DictReader(
        open(ROOT / problem / "manifest.csv", encoding="utf-8"))}


def load_results(problem: str, sid: str):
    p = ROOT / problem / "results" / f"{sid}.json"
    if not p.exists():
        return None
    return json.load(open(p, encoding="utf-8"))


def explain(problem: str, sid: str, manifest_row: dict, results: dict | None) -> tuple[str, str]:
    """Return (score_str, reason)."""
    status = manifest_row["status"]
    lang = manifest_row["detected_language"]

    if lang == "empty":
        return "0/20", "no submission (blank answer)"
    if lang == "missing":
        return "0/20", "no submission"
    if lang == "pseudocode":
        return "n/a", "pseudocode — not auto-graded; grade manually"

    if results is None:
        return "0/20", f"no results file (manifest status: {status})"

    passed = results["tests_passed"]
    failed = results["tests_failed"]
    total = passed + failed
    score = round(20 * passed / total, 2) if total else 0
    score_str = f"{score}/20 ({passed}/{total} tests)"
    load_err = (results.get("load_error") or "").strip()

    # Inspect diff for notable tags
    diff_path = ROOT / problem / "fixed" / f"{sid}.diff.md"
    diff_text = diff_path.read_text(encoding="utf-8") if diff_path.exists() else ""
    flags = []
    if "[logic-affecting]" in diff_text:
        if "stub" in diff_text:
            flags.append("force-runnable stub (original unparseable)")
        elif "pass` into empty block" in diff_text:
            flags.append("force-runnable: injected `pass` into empty block(s)")
        else:
            flags.append("logic-affecting repair applied")
    if "[ambiguous]" in diff_text:
        flags.append("ambiguous re-indent")
    if "Java->Python" in diff_text:
        flags.append("transpiled from Java")

    # Characterize failures
    if load_err:
        reason = f"failed to load: {load_err[:120]}"
    elif passed == total:
        reason = "all tests passed"
    elif passed == 0:
        err_counter = Counter()
        fail_cases = []
        for r in results["results"]:
            if not r.get("passed"):
                if r.get("error"):
                    err_counter[r["error"].split(":")[0].strip()] += 1
                else:
                    fail_cases.append(r["name"])
        if err_counter:
            top = err_counter.most_common(1)[0]
            reason = f"runtime error on all tests: {top[0]} (x{top[1]})"
        else:
            reason = "wrong output on every test (logic error)"
    else:
        # partial credit — summarize what failed
        fails = [r for r in results["results"] if not r.get("passed")]
        err_counter = Counter()
        wrong_ans = 0
        for r in fails:
            if r.get("error"):
                err_counter[r["error"].split(":")[0].strip()] += 1
            else:
                wrong_ans += 1
        parts = []
        if wrong_ans:
            parts.append(f"{wrong_ans} wrong output" + ("s" if wrong_ans != 1 else ""))
        for err, cnt in err_counter.most_common(2):
            parts.append(f"{cnt}x {err}")
        reason = f"passed {passed}/{total}; failures: " + "; ".join(parts)

    if flags:
        reason += " [" + "; ".join(flags) + "]"
    return score_str, reason


def main():
    roster = load_roster()
    p1_manifest = load_manifest("problem1")
    p2_manifest = load_manifest("problem2")
    p3_manifest = load_manifest("problem3_bonus")

    all_ids = sorted(set(p1_manifest) | set(p2_manifest) | set(p3_manifest))

    out = ["# Score Breakdown", "",
           f"Students: {len(all_ids)}. Scores are automated estimates; "
           "entries flagged in the reason text should be manually reviewed.",
           ""]

    # Also write a flat CSV
    csv_rows = []

    for sid in all_ids:
        name = roster.get(sid, "?")
        p1 = p1_manifest.get(sid)
        p2 = p2_manifest.get(sid)
        p3 = p3_manifest.get(sid)

        p1_score, p1_reason = explain("problem1", sid, p1, load_results("problem1", sid)) if p1 else ("—", "not in P1 manifest")
        p2_score, p2_reason = explain("problem2", sid, p2, load_results("problem2", sid)) if p2 else ("—", "not in P2 manifest")

        if p3:
            p3_lang = p3["detected_language"]
            p3_status = p3["status"]
            if p3_lang == "empty":
                p3_summary = "no bonus submission"
            elif p3_lang == "pseudocode":
                p3_summary = "pseudocode (manual grade)"
            elif p3_status == "needs-manual-review":
                p3_summary = "submitted but needs manual review (force-runnable / commented)"
            else:
                p3_summary = f"submitted ({p3_lang}) — manual LeetCode POTD grade"
        else:
            p3_summary = "—"

        out.append(f"## {sid} — {name}")
        out.append(f"- **Problem 1**: {p1_score} — {p1_reason}")
        out.append(f"- **Problem 2**: {p2_score} — {p2_reason}")
        out.append(f"- **Bonus**: {p3_summary}")
        out.append("")

        csv_rows.append({
            "student_id": sid, "name": name,
            "p1_score": p1_score, "p1_reason": p1_reason,
            "p2_score": p2_score, "p2_reason": p2_reason,
            "bonus": p3_summary,
        })

    (ROOT / "score_breakdown.md").write_text("\n".join(out), encoding="utf-8")
    with (ROOT / "score_breakdown.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["student_id", "name", "p1_score",
                                          "p1_reason", "p2_score", "p2_reason", "bonus"])
        w.writeheader()
        w.writerows(csv_rows)

    print(f"Wrote score_breakdown.md and score_breakdown.csv ({len(all_ids)} students)")


if __name__ == "__main__":
    main()
