"""Stage 1: Split submissions.csv into per-problem raw files + manifests.

- keep only the highest-numbered attempt per (student, problem), tiebreak on Attempt End
- do NOT modify the Answer field (preserve whitespace/broken indent)
- write students.csv, problem statements, raw/<id>.txt, manifest.csv, missing_mandatory.csv
"""
import csv
import os
import re
from collections import defaultdict
from datetime import datetime

from pathlib import Path

ROOT = str(Path(__file__).resolve().parent.parent)
INPUTS = os.path.join(ROOT, "inputs")
REPORTS = os.path.join(ROOT, "reports")
CSV_PATH = os.path.join(INPUTS, "submissions.csv")

PROBLEMS = [
    ("Maximum Valid Window Sum", "problem1", True),
    ("Count Valid Pairs With Constraint", "problem2", True),
    ("Bonus\nComplete the problem of the day", "problem3_bonus", False),
]


def classify_qtext(qtext: str) -> str:
    t = (qtext or "").replace("\r\n", "\n").replace("\r", "\n").lstrip()
    for prefix, label, _ in PROBLEMS:
        if t.startswith(prefix):
            return label
    if t.startswith("Bonus\nHow are you going to prepare"):
        return "skip_reflection"
    return "unknown"


def detect_language(answer: str) -> str:
    a = answer or ""
    stripped = a.strip()
    if not stripped:
        return "empty"
    # treat tiny non-answers as empty
    if len(stripped) <= 5 and not any(c.isalpha() for c in stripped):
        return "empty"
    low = stripped.lower()
    if low in {"n/a", "na", "none", "skip", "-", "no", "tbd", "x"}:
        return "empty"
    has_def = bool(re.search(r"\bdef\s+\w+\s*\(", a))
    has_java_sig = bool(re.search(r"public\s+(static\s+)?\w+\s+\w+\s*\(", a))
    has_java_braces = "{" in a and "}" in a
    has_semi = ";" in a
    python_score = 0
    java_score = 0
    if has_def:
        python_score += 3
    if ":" in a and ("if " in a or "for " in a or "while " in a):
        python_score += 1
    if has_java_sig:
        java_score += 3
    if has_java_braces:
        java_score += 1
    if has_semi:
        java_score += 1
    if python_score == 0 and java_score == 0:
        # No code-ish markers: pseudocode vs empty
        # If there are control-flow keywords in english, call it pseudocode
        if any(kw in low for kw in ("for each", "if ", "else", "while ", "return ", "print ", "loop")):
            return "pseudocode"
        return "pseudocode"  # conservative: text with no code markers still counts as submission
    if python_score >= java_score:
        return "python"
    return "java"


def parse_dt(s: str):
    s = (s or "").strip()
    if not s:
        return datetime.min
    # Try a few formats Brightspace uses
    for fmt in ("%m/%d/%Y %I:%M %p", "%m/%d/%Y %H:%M", "%Y-%m-%d %H:%M:%S"):
        try:
            return datetime.strptime(s, fmt)
        except ValueError:
            continue
    return datetime.min


def main():
    rows = []
    with open(CSV_PATH, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)

    wr_rows = [r for r in rows if (r.get("Q Type") or "").strip() == "WR"]

    # ---------- students.csv ----------
    students = {}
    for r in rows:
        sid = (r.get("Org Defined ID") or "").strip()
        if not sid:
            continue
        if sid not in students:
            students[sid] = (r.get("FirstName", "").strip(), r.get("LastName", "").strip())
    os.makedirs(INPUTS, exist_ok=True)
    os.makedirs(REPORTS, exist_ok=True)
    students_path = os.path.join(INPUTS, "students.csv")
    with open(students_path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["student_id", "FirstName", "LastName"])
        for sid in sorted(students):
            fn, ln = students[sid]
            w.writerow([sid, fn, ln])
    print(f"Wrote {students_path} ({len(students)} students)")

    # ---------- group by (student, problem), pick latest ----------
    groups = defaultdict(list)
    qtext_by_problem = {}
    for r in wr_rows:
        problem = classify_qtext(r.get("Q Text") or "")
        if problem not in ("problem1", "problem2", "problem3_bonus"):
            continue
        sid = (r.get("Org Defined ID") or "").strip()
        if not sid:
            continue
        try:
            att = int((r.get("Attempt #") or "0").strip() or 0)
        except ValueError:
            att = 0
        end = parse_dt(r.get("Attempt End") or "")
        groups[(sid, problem)].append((att, end, r))
        # store one canonical Q Text per problem (take the first seen, stripped of leading \r\n)
        if problem not in qtext_by_problem:
            qtext_by_problem[problem] = r.get("Q Text") or ""

    # ---------- per-problem output ----------
    missing_mandatory = defaultdict(list)  # sid -> list of missing mandatory problem labels
    for prefix, label, mandatory in PROBLEMS:
        pdir = os.path.join(ROOT, label)
        raw_dir = os.path.join(pdir, "raw")
        fixed_dir = os.path.join(pdir, "fixed")
        results_dir = os.path.join(pdir, "results")
        audit_dir = os.path.join(pdir, "audit")
        for d in (pdir, raw_dir, fixed_dir, results_dir, audit_dir):
            os.makedirs(d, exist_ok=True)

        # problem_statement.md
        stmt = qtext_by_problem.get(label, "")
        stmt_path = os.path.join(pdir, "problem_statement.md")
        with open(stmt_path, "w", encoding="utf-8") as f:
            f.write(stmt)
        print(f"Wrote {stmt_path}")

        # manifest
        manifest_path = os.path.join(pdir, "manifest.csv")
        manifest_rows = []
        for sid in sorted(students):
            key = (sid, label)
            candidates = groups.get(key)
            if not candidates:
                # student has no row for this problem at all
                if mandatory:
                    missing_mandatory[sid].append(label)
                manifest_rows.append({
                    "student_id": sid,
                    "detected_language": "missing",
                    "attempt_num": "",
                    "raw_path": "",
                    "status": "missing",
                })
                continue
            # pick latest attempt
            candidates.sort(key=lambda x: (x[0], x[1]))
            attempt_num, _end, row = candidates[-1]
            answer = row.get("Answer") or ""
            lang = detect_language(answer)

            raw_path = os.path.join(raw_dir, f"{sid}.txt")
            with open(raw_path, "w", encoding="utf-8", newline="") as f:
                f.write(answer)

            if lang == "empty":
                status = "empty"
                if mandatory:
                    missing_mandatory[sid].append(label)
            else:
                status = "extracted"

            manifest_rows.append({
                "student_id": sid,
                "detected_language": lang,
                "attempt_num": attempt_num,
                "raw_path": os.path.relpath(raw_path, ROOT).replace("\\", "/"),
                "status": status,
            })

        with open(manifest_path, "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["student_id", "detected_language", "attempt_num", "raw_path", "status"])
            w.writeheader()
            for mr in manifest_rows:
                w.writerow(mr)
        print(f"Wrote {manifest_path} ({len(manifest_rows)} rows)")

    # ---------- missing_mandatory.csv ----------
    mm_path = os.path.join(REPORTS, "missing_mandatory.csv")
    with open(mm_path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["student_id", "name", "missing_problems"])
        for sid in sorted(missing_mandatory):
            fn, ln = students.get(sid, ("", ""))
            w.writerow([sid, f"{fn} {ln}".strip(), ";".join(missing_mandatory[sid])])
    print(f"Wrote {mm_path} ({len(missing_mandatory)} students)")

    # summary
    print("\n--- Stage 1 summary ---")
    for _prefix, label, _mand in PROBLEMS:
        mpath = os.path.join(ROOT, label, "manifest.csv")
        with open(mpath, encoding="utf-8") as f:
            mreader = csv.DictReader(f)
            c = defaultdict(int)
            for r in mreader:
                c[(r["detected_language"], r["status"])] += 1
        print(f"\n{label}:")
        for (lang, st), n in sorted(c.items()):
            print(f"  {lang:10s} {st:20s}: {n}")


if __name__ == "__main__":
    main()
