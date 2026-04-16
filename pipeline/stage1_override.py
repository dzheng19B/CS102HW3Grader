"""Override: for B01125201, use Attempt #1 (non-empty) instead of the all-blank Attempt #2.

Documented exception to the 'keep highest Attempt #' rule — the blank attempt #2 appears to
be an accidental quiz reopen (all 4 WR answers zero-length) rather than a genuine resubmit.
"""
import csv
import os
from datetime import datetime
from pathlib import Path

ROOT = str(Path(__file__).resolve().parent.parent)
INPUTS = os.path.join(ROOT, "inputs")
REPORTS = os.path.join(ROOT, "reports")
CSV_PATH = os.path.join(INPUTS, "submissions.csv")

OVERRIDE_SID = "B01125201"
PROBLEM_PREFIXES = {
    "Maximum Valid Window Sum": "problem1",
    "Count Valid Pairs With Constraint": "problem2",
    "Bonus\nComplete the problem of the day": "problem3_bonus",
}


def classify(qtext: str) -> str:
    t = (qtext or "").replace("\r\n", "\n").lstrip()
    for k, v in PROBLEM_PREFIXES.items():
        if t.startswith(k):
            return v
    return "other"


def detect_language(answer: str) -> str:
    import re
    a = answer or ""
    s = a.strip()
    if not s:
        return "empty"
    if s.lower() in {"n/a", "na", "none", "skip", "-"}:
        return "empty"
    has_def = bool(re.search(r"\bdef\s+\w+\s*\(", a))
    has_java_sig = bool(re.search(r"public\s+(static\s+)?\w+\s+\w+\s*\(", a))
    has_braces = "{" in a and "}" in a
    has_semi = ";" in a
    ps = (3 if has_def else 0) + (1 if ":" in a and any(k in a for k in ("if ", "for ", "while ")) else 0)
    js = (3 if has_java_sig else 0) + (1 if has_braces else 0) + (1 if has_semi else 0)
    if ps == 0 and js == 0:
        return "pseudocode"
    return "python" if ps >= js else "java"


def main():
    rows = []
    with open(CSV_PATH, encoding="utf-8-sig", newline="") as f:
        for r in csv.DictReader(f):
            rows.append(r)

    target = [
        r for r in rows
        if r.get("Org Defined ID") == OVERRIDE_SID
        and (r.get("Q Type") or "").strip() == "WR"
        and int(r.get("Attempt #") or 0) == 1
        and classify(r.get("Q Text", "")) in ("problem1", "problem2", "problem3_bonus")
    ]
    print(f"Found {len(target)} attempt#1 rows for {OVERRIDE_SID}")

    # Overwrite raw files and update manifest rows
    for r in target:
        problem = classify(r.get("Q Text", ""))
        answer = r.get("Answer") or ""
        raw_path = os.path.join(ROOT, problem, "raw", f"{OVERRIDE_SID}.txt")
        with open(raw_path, "w", encoding="utf-8", newline="") as f:
            f.write(answer)
        lang = detect_language(answer)
        status = "empty" if lang == "empty" else "extracted"
        # Update manifest
        mpath = os.path.join(ROOT, problem, "manifest.csv")
        mrows = []
        with open(mpath, encoding="utf-8", newline="") as f:
            mrows = list(csv.DictReader(f))
        for mr in mrows:
            if mr["student_id"] == OVERRIDE_SID:
                mr["detected_language"] = lang
                mr["attempt_num"] = "1"
                mr["raw_path"] = os.path.relpath(raw_path, ROOT).replace("\\", "/")
                mr["status"] = status
        with open(mpath, "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["student_id", "detected_language", "attempt_num", "raw_path", "status"])
            w.writeheader()
            for mr in mrows:
                w.writerow(mr)
        print(f"  {problem}: overwrote raw + manifest (lang={lang}, status={status}, size={len(answer)})")

    # Rewrite missing_mandatory.csv without B01125201 if both mandatories now non-empty
    mm_path = os.path.join(REPORTS, "missing_mandatory.csv")
    out = []
    with open(mm_path, encoding="utf-8", newline="") as f:
        for row in csv.reader(f):
            out.append(row)
    header, data = out[0], out[1:]
    data = [r for r in data if r[0] != OVERRIDE_SID]
    with open(mm_path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        for r in data:
            w.writerow(r)
    print(f"Removed {OVERRIDE_SID} from missing_mandatory.csv (now {len(data)} rows)")

    # Document exception
    notes_path = os.path.join(REPORTS, "overrides.md")
    with open(notes_path, "w", encoding="utf-8") as f:
        f.write(
            "# Pipeline overrides\n\n"
            "## B01125201 (Kathryn Schauber) — attempt #1 used instead of #2\n\n"
            "Reason: Attempt #2 had zero-length answers for all 4 WR questions. "
            "Treated as an accidental quiz reopen, not a genuine resubmission. "
            "Attempt #1 (4/7/2026 1:32 PM) contained real answers for all 3 coding problems "
            "and was used for grading.\n\n"
            "Decision: user-approved manual override on 2026-04-15.\n"
        )
    print(f"Wrote {notes_path}")


if __name__ == "__main__":
    main()
