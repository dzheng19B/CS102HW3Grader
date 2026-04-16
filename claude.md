# Auto-Grading Pipeline

Be concise when responding.

You are grading a Brightspace quiz export of LeetCode-style problems for ~74 students. The pipeline extracts code from the CSV, repairs syntax, runs autograders (native Python + native Java), and generates reports.

## Directory layout

```
inputs/
  submissions.csv          — Brightspace export (input)
  questions.md             — quiz questions (input)
  students.csv             — roster (written by stage 1, treated as input afterward)
pipeline/
  stage0_inspect.py        — inspection / sanity check
  stage1_split.py          — split submissions.csv into per-problem raw/
  stage1_override.py       — manual per-student overrides (e.g., use attempt #1)
  stage2_repair.py         — Python syntax repair + force-runnable fallback
  stage3_separate_langs.py — split fixed/ into python/, java/, pseudocode/
  stage4_audit.py          — flag logic-affecting / ambiguous changes
  stage5_breakdown.py      — per-student score breakdown report
  stage6_full_dump.py      — single continuous report with every student's full data
  stage7_split_reports.py  — split the full dump into per-topic reports
  java_grader.py           — native Java grader (javac + java) for java/ subfolders
  verify_tests.py          — sanity-check test_cases.json vs. reference solutions
reports/
  missing_mandatory.csv    — students missing a mandatory problem
  overrides.md             — documented manual overrides
  score_breakdown.md/.csv  — per-student score narrative
  all_students_full.md     — one-file dump of every student's raw/fixed/diff/score
  problem1_report.md       — same, filtered to Problem 1
  problem2_report.md       — same, filtered to Problem 2
  pseudocode_report.md     — all pseudocode submissions (manual grading)
problem1/
  problem_statement.md     — full Q Text
  raw/<sid>.txt            — raw Answer field, untouched
  fixed/<sid>.py           — syntax-repaired Python 3
  fixed/<sid>.diff.md      — per-change log, tabular
  python/<sid>.py          — Python-detected students (grader input)
  java/<sid>.java          — Java-detected students (graded natively)
  java/<sid>.diff.md       — Java repair changelog
  pseudocode/<sid>.txt     — raw pseudocode (manual grade)
  test_cases.json          — graded test cases
  grader.py                — Python subprocess grader
  results/<sid>.json       — Python run result
  results/<sid>_java.json  — Java run result (javac+java)
  results/summary.csv      — merged summary (Python + Java)
  audit/<sid>.md           — logic-change audit
  manifest.csv             — student_id, detected_language, attempt_num, raw_path, status
problem2/                  — same structure
problem3_bonus/            — same structure (no auto-grading; LeetCode POTD varies)
CLAUDE.md                  — this file
```

All pipeline scripts resolve paths via `ROOT = Path(__file__).resolve().parent.parent` so they can be run from anywhere (`py pipeline/stage2_repair.py`).

## Input CSV

`submissions.csv` columns used:

- `Org Defined ID` — canonical student ID (e.g., `B01061084`).
- `Attempt #` — keep only the highest-numbered attempt per (student, problem); tiebreak on `Attempt End`.
- `Q Type` — filter to `WR` only. Ignore `MC`, `M-S`, blanks.
- `Q Text` — identifies the problem by prefix (Q Title is empty for WR rows).
- `Answer` — student's code as plain text. Indentation often broken from textbox paste.
- `Bonus?` — UNRELIABLE. Use Q Text prefix instead.

## Problem set

4 WR rows per attempt. Map by Q Text prefix:

| Problem | Q Text starts with | Type | Goes in |
|---|---|---|---|
| 1 | `Maximum Valid Window Sum:` | mandatory coding | `problem1/` |
| 2 | `Count Valid Pairs With Constraint` | mandatory coding | `problem2/` |
| 3 | `Bonus\nComplete the problem of the day` | bonus coding | `problem3_bonus/` |
| — | `Bonus\nHow are you going to prepare` | written reflection | **SKIP** |

## Core rules

1. **Latest attempt only.** Group by (`Org Defined ID`, problem). Highest `Attempt #`; tiebreak on `Attempt End`. Manual overrides go in `stage1_override.py` with rationale in `reports/overrides.md`.
2. **Detect language from Answer content.** Heuristics: `def`/`:` → python; `public`/`{`/`;` → java; otherwise pseudocode or empty. Record in manifest.
3. **Empty answers count as missing** for mandatory problems (added to `reports/missing_mandatory.csv`). Pseudocode counts as submitted (manual grade).
4. **Never modify student logic.** Stage 2 only touches tokens that prevent parsing. Preserve wrong logic verbatim.
5. **Every change logged** in `fixed/<sid>.diff.md` (and `java/<sid>.diff.md` for Java), tagged `[syntax-only]`, `[ambiguous]`, or `[logic-affecting]`. Any non-syntax-only change auto-flags for manual review.
6. **Java students are graded natively** (not transpiled to Python). Their `python/<sid>.py` backup is not used for grading.
7. **Force-runnable fallback (stage 2).** If AST parse still fails after repair attempts, inject `pass` into empty blocks; if still unparseable, emit `def <fn_name>(...): return 0` stub. This is tagged `[logic-affecting]` — student will score 0 but pipeline does not break. For P3 bonus (unknown fn), comment out all content instead.
8. **Stages are sequential and idempotent per problem.**

## Stages

### Stage 0 — Inspect
`py pipeline/stage0_inspect.py` — prints WR row counts, per-problem counts, multi-attempt students, language detection samples. STOP for confirmation.

### Stage 1 — Split and extract
`py pipeline/stage1_split.py` — writes `inputs/students.csv`, `problem<N>/raw/<sid>.txt`, `problem<N>/manifest.csv`, `problem<N>/problem_statement.md`, and `reports/missing_mandatory.csv`.
`py pipeline/stage1_override.py` — applies documented manual overrides.

### Stage 2 — Syntax repair
`py pipeline/stage2_repair.py` — produces `problem<N>/fixed/<sid>.py` + diff. Python: normalize whitespace, typo fixes, colon/bracket fixes, signature wrap, conservative re-indent → aggressive re-indent → force-runnable stub. Java: mechanical Java→Python transpile for backup; Java files also separately repaired and graded natively in later stages.

### Stage 3 — Separate by language
`py pipeline/stage3_separate_langs.py` — splits `fixed/` into `python/`, `java/`, `pseudocode/`. For Java, copies raw to `java/<sid>.java` and runs minimal Java syntax repair (strip prose, add semicolons, `.length()`→`.length`, fallback `return 0;` only if no return exists anywhere, balance braces, wrap in `public class Solution { ... }`). Writes `java/<sid>.diff.md` in the same tabular format as Python diffs.

### Stage 3b — Auto-grade
Python: `py problem1/grader.py`, `py problem2/grader.py` — subprocess runner, 5s timeout, writes `results/<sid>.json` and `results/summary.csv`.
Java: `py pipeline/java_grader.py` — generates a `Harness.java` with inlined test data, compiles student `Solution.java` + harness via `javac`, runs with `java`, merges results into `results/summary.csv` with `[java]` prefix.

### Stage 4 — Logic-change audit
`py pipeline/stage4_audit.py` — any `[ambiguous]` / `[logic-affecting]` diff entry downgrades status to `needs-manual-review` and writes `audit/<sid>.md`.

### Stage 5 — Score breakdown
`py pipeline/stage5_breakdown.py` — human-readable narrative at `reports/score_breakdown.md` + flat `reports/score_breakdown.csv`. Prefers Java results for Java-detected students.

### Stage 6 — Full dump
`py pipeline/stage6_full_dump.py` — `reports/all_students_full.md`: one section per student with P1 diff → highlighted changes (collapsed) → raw → fixed, same for P2, P3 raw code, score summary. Sorted by combined score; manual-review students last.

### Stage 7 — Per-topic reports
`py pipeline/stage7_split_reports.py` — splits the full dump into `reports/problem1_report.md`, `reports/problem2_report.md`, `reports/pseudocode_report.md`.

## STOP points

Ask before:
- Continuing past stage 0 (confirm extraction counts and language detection).
- Running stage 3b / auto-graders (confirm function signatures and `test_cases.json`).
- Doing anything destructive.
- Continuing if more than 20% of any problem's submissions end up `needs-manual-review` or `unrepairable`.
