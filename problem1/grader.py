"""Stage 3 grader for problem 1.

Runs each fixed/<student_id>.py in a subprocess with a 5s timeout, calls
max_valid_window_sum(nums, k), compares to expected. Writes per-student JSON
and a summary.csv. Deterministic; does not modify student files.
"""
import csv
import json
import subprocess
import sys
from pathlib import Path

PDIR = Path(__file__).parent
FIXED = PDIR / "fixed"
RESULTS = PDIR / "results"
TEST_CASES_PATH = PDIR / "test_cases.json"
TIMEOUT_SEC = 5
MAX_SCORE = 20

RUNNER = r'''
import json, sys, importlib.util, traceback, io, contextlib

fixed_path, cases_path, fn_name = sys.argv[1], sys.argv[2], sys.argv[3]

spec = importlib.util.spec_from_file_location("student", fixed_path)
mod = importlib.util.module_from_spec(spec)
out = {"load_error": None, "results": []}
buf = io.StringIO()
try:
    with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
        spec.loader.exec_module(mod)
except Exception:
    out["load_error"] = traceback.format_exc(limit=3)
    print(json.dumps(out))
    sys.exit(0)

fn = getattr(mod, fn_name, None)
if not callable(fn):
    out["load_error"] = f"function `{fn_name}` not defined"
    print(json.dumps(out))
    sys.exit(0)

cases = json.load(open(cases_path, encoding="utf-8"))["cases"]
for c in cases:
    entry = {"name": c["name"], "expected": c["expected"]}
    try:
        with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
            got = fn(*[_copy(a) for a in c["args"]]) if False else fn(*c["args"])
        entry["got"] = got
        entry["passed"] = got == c["expected"]
    except Exception:
        entry["got"] = None
        entry["passed"] = False
        entry["error"] = traceback.format_exc(limit=2).strip().splitlines()[-1]
    out["results"].append(entry)

print(json.dumps(out))
'''

def run_one(sid: str, fixed_path: Path, fn_name: str) -> dict:
    runner_path = PDIR / "_runner.py"
    runner_path.write_text(RUNNER, encoding="utf-8")
    try:
        proc = subprocess.run(
            [sys.executable, str(runner_path), str(fixed_path), str(TEST_CASES_PATH), fn_name],
            capture_output=True, text=True, timeout=TIMEOUT_SEC,
        )
    except subprocess.TimeoutExpired:
        return {"student_id": sid, "load_error": f"timeout after {TIMEOUT_SEC}s",
                "results": [], "tests_passed": 0, "tests_failed": 0}
    if proc.returncode != 0 or not proc.stdout.strip():
        return {"student_id": sid, "load_error": (proc.stderr or "no output").strip()[-500:],
                "results": [], "tests_passed": 0, "tests_failed": 0}
    try:
        data = json.loads(proc.stdout.strip().splitlines()[-1])
    except json.JSONDecodeError:
        return {"student_id": sid, "load_error": f"bad runner output: {proc.stdout[-300:]}",
                "results": [], "tests_passed": 0, "tests_failed": 0}
    data["student_id"] = sid
    data["tests_passed"] = sum(1 for r in data["results"] if r.get("passed"))
    data["tests_failed"] = len(data["results"]) - data["tests_passed"]
    return data


def main(fn_name: str):
    RESULTS.mkdir(exist_ok=True)
    cases = json.load(open(TEST_CASES_PATH, encoding="utf-8"))["cases"]
    total_cases = len(cases)

    # manifest drives who to grade
    manifest_rows = list(csv.DictReader(open(PDIR / "manifest.csv", encoding="utf-8")))

    summary_rows = []
    for row in manifest_rows:
        sid = row["student_id"]
        status = row["status"]
        fixed_file = FIXED / f"{sid}.py"
        if not fixed_file.exists():
            summary_rows.append({
                "student_id": sid, "status": status, "tests_passed": 0,
                "tests_failed": total_cases, "total_score": 0, "note": "no fixed file",
            })
            continue
        result = run_one(sid, fixed_file, fn_name)
        (RESULTS / f"{sid}.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
        passed = result["tests_passed"]
        score = round(MAX_SCORE * passed / total_cases, 2) if total_cases else 0
        note = result.get("load_error") or ""
        summary_rows.append({
            "student_id": sid, "status": status, "tests_passed": passed,
            "tests_failed": result["tests_failed"], "total_score": score,
            "note": (note or "").replace("\n", " ")[:200],
        })
        print(f"  {sid}: {passed}/{total_cases}  {note[:60]}")

    sp = RESULTS / "summary.csv"
    with sp.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["student_id", "status", "tests_passed",
                                           "tests_failed", "total_score", "note"])
        w.writeheader()
        w.writerows(summary_rows)
    print(f"\nSummary: {sp}")
    (PDIR / "_runner.py").unlink(missing_ok=True)


if __name__ == "__main__":
    main("max_valid_window_sum")
