"""Java grader for problems 1 and 2.

For each .java file in problem{N}/java/:
  1. Generate a Harness.java that imports the student's Solution class,
     runs test cases, prints JSON results to stdout.
  2. Compile (javac) both files.
  3. Run (java) with 5s timeout.
  4. Parse results, write per-student JSON and update results/summary.csv.

Requires: Java JDK on PATH (javac + java).
"""
import csv
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TIMEOUT_SEC = 5
MAX_SCORE = 20

HARNESS_TEMPLATE_P1 = r'''
import java.util.*;

public class Harness {{
    public static void main(String[] args) throws Exception {{
        int[][] allArgs = {test_args};
        int[] expected = {test_expected};
        String[] names = {test_names};

        StringBuilder sb = new StringBuilder();
        sb.append("[");
        for (int t = 0; t < expected.length; t++) {{
            int[] nums = allArgs[t * 2 + 0 < allArgs.length ? t : 0];  // placeholder
            int k_or_T = 0;
            // parsed below
        }}
        // Direct approach: run each test inline
        sb.setLength(0);
        sb.append("{\"results\":[");
        for (int t = 0; t < names.length; t++) {{
            try {{
                int got = Solution.{fn_name}({call_unpack});
                boolean pass = got == expected[t];
                sb.append(String.format("{{\"name\":\"%s\",\"expected\":%d,\"got\":%d,\"passed\":%s}}",
                    names[t], expected[t], got, pass));
            }} catch (Exception e) {{
                sb.append(String.format("{{\"name\":\"%s\",\"expected\":%d,\"got\":null,\"passed\":false,\"error\":\"%s\"}}",
                    names[t], expected[t], e.toString().replace("\"", "'")));
            }}
            if (t < names.length - 1) sb.append(",");
        }}
        sb.append("]}");
        System.out.println(sb.toString());
    }}
}}
'''

def build_harness_java(test_cases: dict, fn_name: str, problem: str) -> str:
    """Generate a self-contained Harness.java with all test data inlined."""
    cases = test_cases["cases"]
    lines = ["import java.util.*;", "", "public class Harness {",
             "    public static void main(String[] args) {",
             "        StringBuilder sb = new StringBuilder();",
             '        sb.append("{\\\"results\\\":[");']

    for i, c in enumerate(cases):
        args = c["args"]
        exp = c["expected"]
        name = c["name"]

        if problem in ("problem1", "problem2"):
            arr = args[0]
            scalar = args[1]
            arr_literal = "new int[]{" + ",".join(str(x) for x in arr) + "}"
            call = f"Solution.{fn_name}({arr_literal}, {scalar})"
        else:
            continue

        lines.append(f"        // test {i}: {name}")
        lines.append("        try {")
        lines.append(f"            int got = {call};")
        lines.append(f"            boolean pass_ = (got == {exp});")
        lines.append(f'            sb.append(String.format("{{\\"name\\":\\"{name}\\",\\"expected\\":{exp},\\"got\\":%d,\\"passed\\":%s}}", got, pass_));')
        lines.append("        } catch (Exception e) {")
        lines.append(f'            sb.append("{{\\"name\\":\\"{name}\\",\\"expected\\":{exp},\\"got\\":null,\\"passed\\":false,\\"error\\":\\"" + e.toString().replace("\\"", "\'") + "\\"}}");')
        lines.append("        }")
        if i < len(cases) - 1:
            lines.append('        sb.append(",");')
        lines.append("")

    lines.append('        sb.append("]}");')
    lines.append("        System.out.println(sb.toString());")
    lines.append("    }")
    lines.append("}")
    return "\n".join(lines)


def grade_java_file(java_path: Path, harness_src: str) -> dict:
    """Compile and run a single student .java with the harness. Return result dict."""
    sid = java_path.stem
    tmpdir = tempfile.mkdtemp(prefix=f"jgrade_{sid}_")
    try:
        # Copy student file as Solution.java
        sol_path = Path(tmpdir) / "Solution.java"
        shutil.copy2(java_path, sol_path)

        # Write harness
        harness_path = Path(tmpdir) / "Harness.java"
        harness_path.write_text(harness_src, encoding="utf-8")

        # Compile
        comp = subprocess.run(
            ["javac", str(sol_path), str(harness_path)],
            capture_output=True, text=True, timeout=15, cwd=tmpdir
        )
        if comp.returncode != 0:
            return {"student_id": sid, "load_error": f"compile error: {comp.stderr.strip()[:500]}",
                    "results": [], "tests_passed": 0, "tests_failed": 0}

        # Run
        run = subprocess.run(
            ["java", "-cp", tmpdir, "Harness"],
            capture_output=True, text=True, timeout=TIMEOUT_SEC, cwd=tmpdir
        )
        if run.returncode != 0:
            return {"student_id": sid, "load_error": f"runtime error: {run.stderr.strip()[:500]}",
                    "results": [], "tests_passed": 0, "tests_failed": 0}

        data = json.loads(run.stdout.strip().splitlines()[-1])
        data["student_id"] = sid
        data["tests_passed"] = sum(1 for r in data["results"] if r.get("passed"))
        data["tests_failed"] = len(data["results"]) - data["tests_passed"]
        return data

    except subprocess.TimeoutExpired:
        return {"student_id": sid, "load_error": f"timeout after {TIMEOUT_SEC}s",
                "results": [], "tests_passed": 0, "tests_failed": 0}
    except Exception as e:
        return {"student_id": sid, "load_error": str(e)[:300],
                "results": [], "tests_passed": 0, "tests_failed": 0}
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)


def grade_problem(problem: str, fn_name: str):
    pdir = ROOT / problem
    java_dir = pdir / "java"
    results_dir = pdir / "results"
    results_dir.mkdir(exist_ok=True)

    java_files = sorted(java_dir.glob("*.java"))
    if not java_files:
        print(f"=== {problem} === no Java files to grade")
        return

    tc_path = pdir / "test_cases.json"
    test_cases = json.load(open(tc_path, encoding="utf-8"))
    total_cases = len(test_cases["cases"])

    harness = build_harness_java(test_cases, fn_name, problem)

    print(f"=== {problem} ({len(java_files)} Java files) ===")

    # Load existing summary to merge Java results in
    summary_path = results_dir / "summary.csv"
    existing = {}
    if summary_path.exists():
        for r in csv.DictReader(open(summary_path, encoding="utf-8")):
            existing[r["student_id"]] = r

    for jf in java_files:
        sid = jf.stem
        result = grade_java_file(jf, harness)
        (results_dir / f"{sid}_java.json").write_text(
            json.dumps(result, indent=2), encoding="utf-8")

        passed = result["tests_passed"]
        score = round(MAX_SCORE * passed / total_cases, 2) if total_cases else 0
        note = result.get("load_error") or ""
        print(f"  {sid}: {passed}/{total_cases}  {note[:80]}")

        # Update or add to summary
        existing[sid] = {
            "student_id": sid,
            "status": existing.get(sid, {}).get("status", "java-graded"),
            "tests_passed": str(passed),
            "tests_failed": str(result["tests_failed"]),
            "total_score": str(score),
            "note": f"[java] {(note or '').replace(chr(10), ' ')[:180]}",
        }

    # Write merged summary
    fields = ["student_id", "status", "tests_passed", "tests_failed", "total_score", "note"]
    with summary_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for sid in sorted(existing):
            w.writerow(existing[sid])

    print(f"  Summary updated: {summary_path}")


def main():
    # Check Java availability
    try:
        subprocess.run(["javac", "-version"], capture_output=True, timeout=5)
    except (FileNotFoundError, subprocess.TimeoutExpired):
        print("ERROR: javac not found. Install a Java JDK and ensure 'javac' is on PATH.")
        print("Java grader written but cannot execute. Re-run after installing Java.")
        print("\nTo install: download from https://adoptium.net/ or run:")
        print("  winget install EclipseAdoptium.Temurin.21.JDK")
        sys.exit(1)

    grade_problem("problem1", "maxValidWindowSum")
    grade_problem("problem2", "countPairs")


if __name__ == "__main__":
    main()
