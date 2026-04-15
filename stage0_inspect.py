"""Stage 0: Inspect submissions.csv and print stats. Does not modify anything."""
import csv
import sys
from collections import defaultdict, Counter

CSV_PATH = r"C:\Users\danz3\Downloads\CS102HW3Grader\submissions.csv"

# Q Text prefix -> problem label
PROBLEM_PREFIXES = [
    ("Maximum Valid Window Sum", "problem1"),
    ("Count Valid Pairs With Constraint", "problem2"),
    ("Bonus\nComplete the problem of the day", "problem3_bonus"),
    ("Bonus\nHow are you going to prepare", "skip_reflection"),
]


def classify_qtext(qtext: str) -> str:
    # Normalize \r\n to \n
    t = qtext.replace("\r\n", "\n").replace("\r", "\n")
    stripped = t.lstrip()
    for prefix, label in PROBLEM_PREFIXES:
        if stripped.startswith(prefix):
            return label
    return "unknown"


def detect_language(answer: str) -> str:
    if not answer or not answer.strip():
        return "empty"
    a = answer
    has_def = ("def " in a) and (":" in a)
    has_java = ("public " in a) or ("System.out" in a) or (";" in a and "{" in a)
    # Priority: explicit def -> python; then java markers; then pseudocode
    if has_def and not has_java:
        return "python"
    if has_java and not has_def:
        return "java"
    if has_def and has_java:
        # mixed — pick python if def ...(): appears first
        return "python" if a.find("def ") < a.find("{") else "java"
    # No strong language markers
    # Check for common natural-language indicators
    lowered = a.lower()
    if any(kw in lowered for kw in ("for each", "if number", "return ", "loop through", "else:", "print ")):
        return "pseudocode"
    return "pseudocode"


def main():
    rows = []
    with open(CSV_PATH, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)

    wr_rows = [r for r in rows if (r.get("Q Type") or "").strip() == "WR"]

    print(f"Total rows in CSV: {len(rows)}")
    print(f"Total WR rows: {len(wr_rows)}")

    unique_students_all = set(r["Org Defined ID"] for r in rows if r.get("Org Defined ID"))
    unique_students_wr = set(r["Org Defined ID"] for r in wr_rows if r.get("Org Defined ID"))
    print(f"Unique students (all rows): {len(unique_students_all)}")
    print(f"Unique students (WR rows): {len(unique_students_wr)}")

    # Count rows per problem via Q Text prefix
    per_problem = Counter()
    per_problem_rows = defaultdict(list)
    for r in wr_rows:
        label = classify_qtext(r.get("Q Text") or "")
        per_problem[label] += 1
        per_problem_rows[label].append(r)

    print("\nWR rows per problem (by Q Text prefix):")
    for label, cnt in sorted(per_problem.items(), key=lambda kv: kv[0]):
        print(f"  {label}: {cnt}")

    # Multiple attempts: count (student, problem) pairs with >1 attempt
    sp_attempts = defaultdict(list)  # (student, problem) -> list of (attempt_num, attempt_end, row)
    for r in wr_rows:
        sid = r.get("Org Defined ID") or ""
        problem = classify_qtext(r.get("Q Text") or "")
        if problem in ("skip_reflection", "unknown"):
            continue
        try:
            att = int(r.get("Attempt #") or 0)
        except ValueError:
            att = 0
        sp_attempts[(sid, problem)].append((att, r.get("Attempt End") or "", r))

    multi_attempt_pairs = {k: v for k, v in sp_attempts.items() if len(v) > 1}
    multi_attempt_students = set(k[0] for k in multi_attempt_pairs.keys())
    print(f"\nStudents with multiple attempts on any coding problem: {len(multi_attempt_students)}")
    for sid in sorted(multi_attempt_students):
        pbs = [p for (s, p), v in multi_attempt_pairs.items() if s == sid]
        attempt_counts = {p: len([x for (s, pp), vv in sp_attempts.items() if s == sid and pp == p for x in vv]) for p in pbs}
        print(f"  {sid}: {attempt_counts}")

    # Sample 2 answers per coding problem
    print("\nSample Answer fields (truncated to 300 chars):")
    for label in ("problem1", "problem2", "problem3_bonus"):
        print(f"\n--- {label} samples ---")
        samples = per_problem_rows[label][:2]
        for i, r in enumerate(samples, 1):
            ans = (r.get("Answer") or "").strip()
            lang = detect_language(r.get("Answer") or "")
            print(f"[{label} sample {i}] student={r.get('Org Defined ID')} attempt={r.get('Attempt #')} detected={lang}")
            print(repr(ans[:300]))
            print()

    # Language distribution on the latest-attempt answers
    print("\nLanguage detection distribution (latest attempt only):")
    for problem in ("problem1", "problem2", "problem3_bonus"):
        lang_counter = Counter()
        for (sid, p), lst in sp_attempts.items():
            if p != problem:
                continue
            # pick latest
            lst_sorted = sorted(lst, key=lambda x: (x[0], x[1]))
            _, _, row = lst_sorted[-1]
            lang = detect_language(row.get("Answer") or "")
            lang_counter[lang] += 1
        print(f"  {problem}: {dict(lang_counter)}")

    # Problem-level participation (latest attempt per student)
    print("\nLatest-attempt participation per coding problem:")
    for problem in ("problem1", "problem2", "problem3_bonus"):
        students = set(s for (s, p) in sp_attempts.keys() if p == problem)
        print(f"  {problem}: {len(students)} unique students")

    # Mandatory-missing check
    p1_students = set(s for (s, p) in sp_attempts.keys() if p == "problem1")
    p2_students = set(s for (s, p) in sp_attempts.keys() if p == "problem2")
    p3_students = set(s for (s, p) in sp_attempts.keys() if p == "problem3_bonus")
    missing_p1 = unique_students_wr - p1_students
    missing_p2 = unique_students_wr - p2_students
    print(f"\nWR students missing problem1 row entirely: {len(missing_p1)} -> {sorted(missing_p1)}")
    print(f"WR students missing problem2 row entirely: {len(missing_p2)} -> {sorted(missing_p2)}")
    print(f"WR students who attempted bonus problem3: {len(p3_students)}")


if __name__ == "__main__":
    main()
