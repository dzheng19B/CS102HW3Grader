"""
grade_python.py
───────────────
Tests all Python student submissions for Two Sum and First Bad Version,
then writes:
  • python_results.csv   — pass/fail summary per student per question
  • grader_report.md     — human-readable report with original vs. modified
                           code and a changelog of every edit the script made

Usage:
    python grade_python.py <path_to_csv>
    python grade_python.py "Homework_4_-_Attempt_Details_wr_filtered.csv"

Requirements: Python 3.8+ stdlib only (no extra pip installs needed).
"""

import sys
import csv
import textwrap
import multiprocessing
from typing import List
from datetime import datetime

CSV_PATH = sys.argv[1] if len(sys.argv) > 1 else "Homework_4_-_Attempt_Details_wr_filtered.csv"

# ──────────────────────────────────────────────────────────────────────────────
# TEST CASES
# ──────────────────────────────────────────────────────────────────────────────

TWO_SUM_TESTS = [
    ([2, 7, 11, 15],       9,   {0, 1}),
    ([3, 2, 4],            6,   {1, 2}),
    ([3, 3],               6,   {0, 1}),
    ([-1, -2, -3, -4, -5], -8,  {2, 4}),
    ([-3, 4, 3, 90],       0,   {0, 2}),
    ([0, 4, 3, 0],         0,   {0, 3}),
    ([100, 200, 300, 400], 700, {2, 3}),
    ([1, 2, 3, 4, 5],      9,   {3, 4}),
    ([1, 9],               10,  {0, 1}),
    (list(range(1, 101)),  100, {48, 50}),
]
TWO_SUM_LABELS = [
    "basic [2,7,11,15] t=9",
    "answer not at start [3,2,4] t=6",
    "duplicates [3,3] t=6",
    "all negatives t=-8",
    "mixed pos/neg t=0",
    "zeros t=0",
    "large target t=700",
    "pair at end t=9",
    "two-element array t=10",
    "100-element array t=100",
]

FBV_TESTS = [
    (5,        1,           1),
    (5,        5,           5),
    (5,        3,           3),
    (1,        1,           1),
    (2,        1,           1),
    (2,        2,           2),
    (10**9,    1,           1),
    (10**9,    10**9,       10**9),
    (10**9,    500_000_000, 500_000_000),
    (5,        4,           4),
]
FBV_LABELS = [
    "bad=first n=5",
    "bad=last n=5",
    "bad=middle n=5",
    "single version n=1",
    "n=2 first bad",
    "n=2 second bad",
    "large n bad=1",
    "large n bad=last",
    "large n bad=mid",
    "bad=second-to-last n=5",
]

# ──────────────────────────────────────────────────────────────────────────────
# DETECTION HELPERS
# ──────────────────────────────────────────────────────────────────────────────

JAVA_MARKERS = [
    "public int[] twoSum", "public int firstBadVersion",
    "HashMap", "Map<Integer", "import java", "extends VersionControl",
    "class Solution {",
]

def detect_java(code: str) -> bool:
    return any(m in code for m in JAVA_MARKERS)

def is_pseudocode(code: str) -> bool:
    """Heuristic: no Python def or class → treat as pseudocode / plain English."""
    return "def " not in code and "class Solution" not in code

# ──────────────────────────────────────────────────────────────────────────────
# NORMALISATION  —  returns (modified_code, list_of_edit_descriptions)
# ──────────────────────────────────────────────────────────────────────────────

def wrap_two_sum(raw: str):
    edits = []
    code  = raw.replace("\r\n", "\n").replace("\r", "\n")

    # 1. Strip stray template comment lines
    before = code
    lines  = [l for l in code.splitlines()
              if not l.strip().startswith("#def isBadVersion")]
    code   = "\n".join(lines)
    if code != before:
        edits.append(
            "Removed stray `#def isBadVersion` template comment line(s) "
            "that some students accidentally left in their Two Sum answer."
        )

    # 2. Wrap bare function in a class
    if "class Solution" not in code and "def twoSum" in code:
        code = "class Solution:\n" + textwrap.indent(code, "    ")
        edits.append(
            "Wrapped bare `def twoSum(...)` in `class Solution:` so it "
            "matches the expected `Solution().twoSum(...)` call interface."
        )

    # 3. Inject typing import
    code = "from typing import List\n" + code
    edits.append("Prepended `from typing import List` to satisfy `List[int]` type hints.")

    return code, edits


def wrap_fbv(raw: str, bad: int):
    edits = []
    code  = raw.replace("\r\n", "\n").replace("\r", "\n")

    # 1. Strip template isBadVersion comment (conflicts with our injected mock)
    before = code
    lines  = [l for l in code.splitlines()
              if not (l.strip().startswith("#") and "isBadVersion" in l and "def isBadVersion" in l)]
    code   = "\n".join(lines)
    if code != before:
        edits.append(
            "Removed template `#def isBadVersion` comment to avoid shadowing "
            "the injected test mock."
        )

    # 2. Wrap bare function in a class
    if "class Solution" not in code and "def firstBadVersion" in code:
        code = "class Solution:\n" + textwrap.indent(code, "    ")
        edits.append("Wrapped bare `def firstBadVersion(...)` in `class Solution:`.")

    # 3. Inject isBadVersion mock + typing import
    header = (
        "from typing import List\n\n"
        f"def isBadVersion(v): return v >= {bad}  # injected test mock\n\n"
    )
    code = header + code
    edits.append(
        f"Prepended `from typing import List` and injected a `isBadVersion(v)` "
        f"mock that returns `True` when `v >= bad`. The `bad` value is swapped "
        f"per test case at runtime."
    )

    return code, edits

# ──────────────────────────────────────────────────────────────────────────────
# TIMEOUT HELPER  (works on Windows, Mac, Linux via multiprocessing)
# ──────────────────────────────────────────────────────────────────────────────

TIMEOUT_SECONDS = 3  # per individual test case

def _exec_two_sum_worker(code: str, nums: list, target: int, result_queue):
    """Runs in a child process; puts ("ok", output) or ("err", msg) on the queue."""
    try:
        ns = {}
        exec(compile(code, "<student>", "exec"), ns)
        sol = ns["Solution"]()
        out = sol.twoSum(list(nums), target)
        result_queue.put(("ok", list(out)))
    except Exception as e:
        result_queue.put(("err", f"{type(e).__name__}: {e}"))


def _exec_fbv_worker(code: str, n: int, result_queue):
    try:
        ns = {}
        exec(compile(code, "<student>", "exec"), ns)
        sol = ns["Solution"]()
        out = sol.firstBadVersion(n)
        result_queue.put(("ok", out))
    except Exception as e:
        result_queue.put(("err", f"{type(e).__name__}: {e}"))


def _run_in_subprocess(target_fn, args, timeout=TIMEOUT_SECONDS):
    """
    Runs target_fn(*args, queue) in a child process.
    Returns ("ok", value) | ("err", msg) | ("timeout", None).
    """
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=target_fn, args=(*args, q))
    p.start()
    p.join(timeout)
    if p.is_alive():
        p.terminate()
        p.join()
        return ("timeout", None)
    if not q.empty():
        return q.get()
    return ("err", "No result returned (process crashed)")

# ──────────────────────────────────────────────────────────────────────────────
# TEST RUNNERS
# ──────────────────────────────────────────────────────────────────────────────

def run_two_sum(raw: str):
    """Returns (test_results, modified_code, edits)."""
    modified, edits = wrap_two_sum(raw)

    # Compile check first (fast, no subprocess needed)
    try:
        compile(modified, "<student>", "exec")
    except SyntaxError as e:
        results = [(lbl, False, f"COMPILE ERROR: {e}") for lbl in TWO_SUM_LABELS]
        return results, modified, edits

    results = []
    for (nums, target, expected_set), lbl in zip(TWO_SUM_TESTS, TWO_SUM_LABELS):
        status, value = _run_in_subprocess(_exec_two_sum_worker, (modified, nums, target))
        if status == "timeout":
            results.append((lbl, False, f"TIMEOUT (>{TIMEOUT_SECONDS}s) — likely infinite loop"))
        elif status == "err":
            results.append((lbl, False, f"RUNTIME ERROR: {value}"))
        else:  # "ok"
            out = value
            try:
                passed = set(out) == expected_set
                detail = "OK" if passed else f"got {out}, expected indices {sorted(expected_set)}"
            except TypeError:
                passed = False
                detail = f"returned non-iterable: {out!r}"
            results.append((lbl, passed, detail))

    return results, modified, edits


def run_fbv(raw: str):
    """Returns (test_results, representative_modified_code, edits)."""
    _, edits = wrap_fbv(raw, FBV_TESTS[0][1])
    last_modified = ""
    results = []

    for (n, bad, expected), lbl in zip(FBV_TESTS, FBV_LABELS):
        modified, _ = wrap_fbv(raw, bad)
        last_modified = modified

        # Compile check
        try:
            compile(modified, "<student>", "exec")
        except SyntaxError as e:
            results.append((lbl, False, f"COMPILE ERROR: {e}"))
            continue

        status, value = _run_in_subprocess(_exec_fbv_worker, (modified, n))
        if status == "timeout":
            results.append((lbl, False, f"TIMEOUT (>{TIMEOUT_SECONDS}s) — likely infinite loop"))
        elif status == "err":
            results.append((lbl, False, f"ERROR: {value}"))
        else:
            out    = value
            passed = (out == expected)
            detail = "OK" if passed else f"got {out}, expected {expected}"
            results.append((lbl, passed, detail))

    return results, last_modified, edits

# ──────────────────────────────────────────────────────────────────────────────
# MARKDOWN REPORT
# ──────────────────────────────────────────────────────────────────────────────

def build_markdown(full_report):
    ts    = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = [
        "# Python Grader Report",
        "",
        f"Generated: {ts}  ",
        f"Source CSV: `{CSV_PATH}`",
        "",
        "> **How to read this report**  ",
        "> Each student section shows their *original* submission exactly as it came",
        "> from the CSV, followed by the *modified* version the grader actually ran.",
        "> The **Edits** list explains every change made and why.",
        "",
        "---",
        "",
        "## Summary Table",
        "",
        "| Student | Question | Score | Status |",
        "|---------|----------|:-----:|--------|",
    ]

    for r in sorted(full_report, key=lambda x: (x["name"], x["question"])):
        score = f"{r['passed']}/{r['total']}" if r["status"] == "TESTED" else r["status"]
        lines.append(f"| {r['name']} | {r['question']} | {score} | {r['status']} |")

    lines += ["", "---", "", "## Per-Student Details", ""]

    for r in sorted(full_report, key=lambda x: (x["name"], x["question"])):
        score = f"{r['passed']}/{r['total']}" if r["status"] == "TESTED" else "—"
        lines += [
            f"### {r['name']} — {r['question']} &nbsp;`{score}`",
            "",
            f"**Status:** `{r['status']}`  ",
            "",
        ]

        # ── Non-tested submissions ──────────────────────────────────────────
        if r["status"] != "TESTED":
            reason = {
                "NO SUBMISSION": "Student did not submit an answer.",
                "PSEUDOCODE":    "Answer appears to be pseudocode or plain English — no executable Python detected.",
            }.get(r["status"], r["status"])
            lines += [f"> ⚠️ {reason}", ""]

            orig = r.get("original_code", "").strip()
            if orig and orig not in ("nan", "NaN", ""):
                lines += [
                    "<details>",
                    "<summary>Original submission</summary>",
                    "",
                    "```python",
                    orig,
                    "```",
                    "",
                    "</details>",
                    "",
                ]
            lines += ["---", ""]
            continue

        # ── Test results table ──────────────────────────────────────────────
        lines += ["**Test results:**", ""]
        lines += ["| # | Test Case | Result | Detail |",
                  "|---|-----------|:------:|--------|"]
        for i, (lbl, passed, detail) in enumerate(r["test_results"], 1):
            icon = "✅ Pass" if passed else "❌ Fail"
            lines.append(f"| {i} | `{lbl}` | {icon} | {detail} |")
        lines += [""]

        # ── Edits changelog ─────────────────────────────────────────────────
        if r["edits"]:
            lines += ["**Edits made by the grader:**", ""]
            for i, edit in enumerate(r["edits"], 1):
                lines.append(f"{i}. {edit}")
            lines += [""]
        else:
            lines += ["> ✅ No edits required — code ran as submitted.", ""]

        # ── Original code ───────────────────────────────────────────────────
        lines += [
            "<details>",
            "<summary><strong>Original code</strong> (exactly as submitted)</summary>",
            "",
            "```python",
            r["original_code"].strip(),
            "```",
            "",
            "</details>",
            "",
        ]

        # ── Modified code ───────────────────────────────────────────────────
        lines += [
            "<details>",
            "<summary><strong>Modified code</strong> (what the grader executed)</summary>",
            "",
            "```python",
            r["modified_code"].strip(),
            "```",
            "",
            "</details>",
            "",
            "---",
            "",
        ]

    return "\n".join(lines)

# ──────────────────────────────────────────────────────────────────────────────
# MAIN
# ──────────────────────────────────────────────────────────────────────────────

def main():
    rows = []
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)

    full_report = []

    for row in rows:
        answer = str(row["Answer"]).strip()
        first  = row["FirstName"].strip()
        last   = row["LastName"].strip()
        name   = f"{first} {last}"
        q_text = str(row["Q Text"])
        q_type = "TwoSum" if ("Two Sum" in q_text or "twoSum" in q_text) else "FBV"

        base = {
            "name": name, "question": q_type, "language": "Python",
            "passed": 0,  "total": 10,
            "original_code": answer,
            "modified_code": "", "edits": [], "test_results": [],
        }

        if answer in ("nan", "", "NaN"):
            full_report.append({**base, "status": "NO SUBMISSION", "details": ""})
            continue

        if detect_java(answer):
            continue  # Java submissions handled by separate Java suite

        if is_pseudocode(answer):
            full_report.append({**base, "status": "PSEUDOCODE", "details": ""})
            continue

        if q_type == "TwoSum":
            test_results, modified, edits = run_two_sum(answer)
        else:
            test_results, modified, edits = run_fbv(answer)

        passed_count   = sum(1 for _, p, _ in test_results if p)
        failed_details = "; ".join(
            f"[{lbl}] {detail}" for lbl, passed, detail in test_results if not passed
        )

        full_report.append({
            **base,
            "status":        "TESTED",
            "passed":        passed_count,
            "details":       failed_details,
            "modified_code": modified,
            "edits":         edits,
            "test_results":  test_results,
        })

    # ── Console summary ────────────────────────────────────────────────────────
    print(f"\n{'='*72}")
    print(f"{'STUDENT':<30} {'Q':<8} {'SCORE':>7}  FAILURES")
    print(f"{'='*72}")
    for r in sorted(full_report, key=lambda x: (x["name"], x["question"])):
        score_str = f"{r['passed']}/{r['total']}" if r["status"] == "TESTED" else r["status"]
        trunc     = r["details"][:60] + "…" if len(r["details"]) > 60 else r["details"]
        print(f"{r['name']:<30} {r['question']:<8} {score_str:>7}  {trunc}")

    # ── CSV ────────────────────────────────────────────────────────────────────
    csv_out = "python_results.csv"
    with open(csv_out, "w", newline="", encoding="utf-8") as f:
        fields = ["name", "question", "language", "status", "passed", "total", "details"]
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for r in full_report:
            writer.writerow({k: r[k] for k in fields})
    print(f"\nCSV  saved → {csv_out}")

    # ── Markdown ───────────────────────────────────────────────────────────────
    md_out = "grader_report.md"
    with open(md_out, "w", encoding="utf-8") as f:
        f.write(build_markdown(full_report))
    print(f"MD   saved → {md_out}")


if __name__ == "__main__":
    multiprocessing.freeze_support()  # needed when frozen on Windows (PyInstaller etc.)
    main()
