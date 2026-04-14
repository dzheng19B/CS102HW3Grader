"""
Stage 3 grader — Problem 2: count_pairs
Accepts both Python name (count_pairs) and Java-transpile name (countPairs).
"""

import csv
import json
import os
import subprocess
import sys
import tempfile
import textwrap

PROBLEM_DIR = os.path.dirname(os.path.abspath(__file__))
FIXED_DIR   = os.path.join(PROBLEM_DIR, "fixed")
RESULTS_DIR = os.path.join(PROBLEM_DIR, "results")
MANIFEST    = os.path.join(PROBLEM_DIR, "manifest.csv")
TEST_CASES  = os.path.join(PROBLEM_DIR, "test_cases.json")

TIMEOUT     = 5        # seconds per test
TOTAL_SCORE = 20       # max points
# Function names to try (Python camelCase last, Python snake_case first)
FUNC_NAMES  = ["count_pairs", "countPairs"]

os.makedirs(RESULTS_DIR, exist_ok=True)


def load_manifest():
    with open(MANIFEST, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_test_cases():
    with open(TEST_CASES, encoding="utf-8") as f:
        return json.load(f)


def run_one_test(student_py_path, test_case, func_names):
    """
    Run a single test case against the student file.
    Returns a dict: {id, passed, actual, error, timed_out}.
    """
    tc_input  = test_case["input"]
    expected  = test_case["expected"]

    # Build a self-contained runner script
    runner = textwrap.dedent(f"""\
        import sys, json, traceback

        # ---- student code ----
        try:
            with open({json.dumps(student_py_path)}, encoding='utf-8') as _f:
                exec(compile(_f.read(), {json.dumps(student_py_path)}, 'exec'), globals())
        except Exception as _e:
            print(json.dumps({{"error": "import_error: " + str(_e), "actual": None}}))
            sys.exit(0)

        # ---- locate function ----
        _fn = None
        for _name in {json.dumps(func_names)}:
            if _name in globals() and callable(globals()[_name]):
                _fn = globals()[_name]
                break
        if _fn is None:
            print(json.dumps({{"error": "function_not_found: tried " + str({json.dumps(func_names)}), "actual": None}}))
            sys.exit(0)

        # ---- call function ----
        try:
            _result = _fn(**{json.dumps(tc_input)})
            print(json.dumps({{"actual": _result, "error": None}}))
        except Exception as _e:
            print(json.dumps({{"error": "runtime_error: " + str(_e), "actual": None}}))
    """)

    with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False,
                                     encoding="utf-8") as tmp:
        tmp.write(runner)
        runner_path = tmp.name

    try:
        proc = subprocess.run(
            [sys.executable, runner_path],
            capture_output=True, text=True, timeout=TIMEOUT
        )
        stdout = proc.stdout.strip()
        if not stdout:
            return {
                "id": test_case["id"],
                "description": test_case["description"],
                "passed": False,
                "expected": expected,
                "actual": None,
                "error": f"no_output (stderr: {proc.stderr.strip()[:200]})",
                "timed_out": False,
            }
        result = json.loads(stdout)
        actual = result.get("actual")
        error  = result.get("error")
        passed = (error is None) and (actual == expected)
        return {
            "id": test_case["id"],
            "description": test_case["description"],
            "passed": passed,
            "expected": expected,
            "actual": actual,
            "error": error,
            "timed_out": False,
        }
    except subprocess.TimeoutExpired:
        return {
            "id": test_case["id"],
            "description": test_case["description"],
            "passed": False,
            "expected": expected,
            "actual": None,
            "error": "timeout",
            "timed_out": True,
        }
    except json.JSONDecodeError as e:
        return {
            "id": test_case["id"],
            "description": test_case["description"],
            "passed": False,
            "expected": expected,
            "actual": None,
            "error": f"json_parse_error: {e}",
            "timed_out": False,
        }
    finally:
        os.unlink(runner_path)


def grade_student(student_id, py_path, test_cases):
    """Run all test cases for one student. Returns per-test results."""
    results = []
    for tc in test_cases:
        r = run_one_test(py_path, tc, FUNC_NAMES)
        results.append(r)
    return results


def main():
    manifest    = load_manifest()
    test_cases  = load_test_cases()
    n_tests     = len(test_cases)

    summary_rows = []
    print(f"Running {n_tests} test cases per student...\n")

    for row in manifest:
        sid    = row["student_id"]
        status = row["status"]

        # Skip non-gradeable submissions
        if status in ("empty", "pseudocode", "unrepairable"):
            summary_rows.append({
                "student_id": sid,
                "status": status,
                "tests_passed": "N/A",
                "tests_failed": "N/A",
                "total_score": 0,
                "notes": f"skipped ({status})",
            })
            print(f"  {sid}: skipped ({status})")
            continue

        py_path = os.path.join(FIXED_DIR, f"{sid}.py")
        if not os.path.exists(py_path):
            summary_rows.append({
                "student_id": sid,
                "status": status,
                "tests_passed": 0,
                "tests_failed": n_tests,
                "total_score": 0,
                "notes": "fixed file missing",
            })
            print(f"  {sid}: fixed file missing")
            continue

        results = grade_student(sid, py_path, test_cases)

        passed = sum(1 for r in results if r["passed"])
        failed = n_tests - passed
        score  = round((passed / n_tests) * TOTAL_SCORE, 2)
        notes  = "needs-manual-review" if status == "needs-manual-review" else ""

        # Write per-student JSON
        out = {
            "student_id": sid,
            "status": status,
            "tests_passed": passed,
            "tests_failed": failed,
            "total_score": score,
            "test_results": results,
        }
        with open(os.path.join(RESULTS_DIR, f"{sid}.json"), "w", encoding="utf-8") as f:
            json.dump(out, f, indent=2)

        summary_rows.append({
            "student_id": sid,
            "status": status,
            "tests_passed": passed,
            "tests_failed": failed,
            "total_score": score,
            "notes": notes,
        })

        # Console output
        bar = "".join("P" if r["passed"] else "F" for r in results)
        flag = " [MANUAL]" if status == "needs-manual-review" else ""
        print(f"  {sid}: {passed}/{n_tests}  [{bar}]  score={score:.1f}/20{flag}")

    # Write summary CSV
    summary_path = os.path.join(RESULTS_DIR, "summary.csv")
    with open(summary_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["student_id", "status", "tests_passed",
                                           "tests_failed", "total_score", "notes"])
        w.writeheader()
        w.writerows(summary_rows)

    # Print aggregate stats
    gradeable = [r for r in summary_rows if isinstance(r["tests_passed"], int)]
    if gradeable:
        avg = sum(r["total_score"] for r in gradeable) / len(gradeable)
        perfect = sum(1 for r in gradeable if r["total_score"] == TOTAL_SCORE)
        zero    = sum(1 for r in gradeable if r["total_score"] == 0)
        print(f"\nGradeable: {len(gradeable)}  |  Avg score: {avg:.1f}/20  |"
              f"  Perfect: {perfect}  |  Zero: {zero}")
    print(f"Summary written to {summary_path}")


if __name__ == "__main__":
    main()
