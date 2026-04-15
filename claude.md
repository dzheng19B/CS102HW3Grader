# Auto-Grading Pipeline

Be concise when responding

You are grading a Brightspace quiz export of LeetCode-style problems for ~73 students. The pipeline extracts code from the CSV, repairs syntax, runs an autograder, and audits any changes.

## Input

`questions.md` is a copy and paste of the questions for the quiz. Use this to make sure you do not part of a student response as part of the question and vice versa.

`submissions.csv` is a Brightspace export. Relevant columns:

- `Org Defined ID` — student ID (e.g., `B01061084`). Use this as the canonical student ID.
- `Attempt #` — 1, 2, etc. Some students have multiple attempts; **keep only the highest-numbered attempt per student per problem**.
- `Attempt End` — timestamp, use as tiebreaker if Attempt # ties.
- `Q Type` — filter to `WR` only. Ignore `MC`, `M-S`, and blank rows.
- `Q Text` — identifies which problem the row belongs to (Q Title is empty for WR rows, do not rely on it).
- `Answer` — the student's code as plain text. Indentation is often broken from textbox pasting.
- `Bonus?` — UNRELIABLE. Do not use it to identify the bonus problem. Use Q Text prefix instead.

## Problem set

There are 4 WR rows per attempt. Map them by Q Text prefix:

| Problem | Q Text starts with | Type | Goes in |
|---|---|---|---|
| 1 | `Maximum Valid Window Sum:` | mandatory coding | `problem1/` |
| 2 | `Count Valid Pairs With Constraint` | mandatory coding | `problem2/` |
| 3 | `Bonus\nComplete the problem of the day` | bonus coding | `problem3_bonus/` |
| — | `Bonus\nHow are you going to prepare` | written reflection | **SKIP — do not extract** |

Run the full pipeline (stages 1–4) independently for each of the 3 coding problems.

## Directory layout (per problem)

```
problem1/
  problem_statement.md     — full Q Text from any one row
  raw/<student_id>.txt     — raw Answer field, untouched
  fixed/<student_id>.py    — syntax-repaired Python 3
  fixed/<student_id>.diff.md
  grader.py
  test_cases.json          — TODO: I will provide before stage 3
  results/
  audit/
  manifest.csv             — student_id, detected_language, attempt_num, status
```

Top-level files:
- `missing_mandatory.csv` — students missing problem 1 or problem 2 entirely.
- `students.csv` — roster of all 73 student IDs seen in the file with name (FirstName, LastName).

## Core rules

1. **Latest attempt only.** Group by (`Org Defined ID`, problem). Keep the row with the highest `Attempt #`; if tied, the latest `Attempt End`. Discard older attempts.
2. **Detect language from Answer content,** since there is no language column. Heuristic: presence of `def `/`:` → Python; `public `/`{`/`;` → Java; everything else or mixed natural language → pseudocode. Record the detection in the manifest.
3. **Empty answers count as missing.** A student whose Answer is blank or whitespace-only for a mandatory problem goes into `missing_mandatory.csv`.
4. **Never modify student logic.** Stage 2 only touches tokens that prevent parsing. Preserve wrong logic verbatim. Mark `needs-manual-review` if you cannot repair without guessing intent.
5. **Pseudocode is not auto-graded.** Mark status `pseudocode`, skip stages 2–3 for that student. For mandatory problems pseudocode still counts as "submitted" — do NOT add to `missing_mandatory.csv`.
6. **Every change logged** in the diff file, tagged `[syntax-only]`, `[ambiguous]`, or `[logic-affecting]`. Any non-syntax-only change auto-flags for manual review.
7. **Stages are sequential and idempotent per problem.**

## Stage 0 — Inspect and confirm

Open `submissions.csv`. Filter to `Q Type == 'WR'`. Print:
- Total WR row count and number of unique students.
- Count of rows per problem (by Q Text prefix above).
- Number of students with multiple attempts and their IDs.
- 2 sample Answer fields per problem (truncated to 300 chars) so I can sanity-check the language-detection heuristic.

Then STOP and wait for my confirmation before continuing.

## Stage 1 — Split and extract

After I confirm:

- Write `students.csv` with all unique (Org Defined ID, FirstName, LastName) tuples.
- For each of the 3 coding problems, extract its full Q Text to `problem<N>/problem_statement.md`.
- For each (student, problem) pair, keep only the latest attempt and write the raw Answer to `problem<N>/raw/<student_id>.txt`.
- Append to `problem<N>/manifest.csv`: `student_id`, `detected_language`, `attempt_num`, `raw_path`, `status` (initially `extracted` or `empty`).
- After all 3 problems are split, write `missing_mandatory.csv` with columns `student_id`, `name`, `missing_problems`.

Do not modify Answer text in this stage — preserve whitespace, broken indentation, everything.

## Stage 2 — Syntax repair (per problem)

For each manifest row with `detected_language` in `python` or `java` and status `extracted`:

- Produce `problem<N>/fixed/<student_id>.py`, runnable Python 3.
- Common fixes you can make freely as `[syntax-only]`: re-indenting code that lost indentation in the textbox paste, adding missing colons, closing brackets, fixing obvious typos in keywords (`retrun` → `return`), wrapping bare statements in the expected function signature.
- For Java, mechanical transpile only (same control flow, same data structures). Otherwise mark `needs-manual-review`.
- Produce `fixed/<student_id>.diff.md` listing every change with a tag and one-sentence reason.
- Update manifest `status`: `repaired`, `needs-manual-review`, or `unrepairable`.

Pseudocode rows: set status `pseudocode` and skip.

## Stage 3 — Auto-grader (per problem)

Write `problem<N>/grader.py` as a deterministic Python script. It must:

- Load `test_cases.json`.
- For each file in `fixed/`, run it in a subprocess with a 5-second timeout, calling the expected solution function (TODO: I will give you the function name and signature for each problem before this stage runs).
- Record per-test pass/fail, errors, timeouts.
- Write `results/<student_id>.json` and `results/summary.csv` with columns: `student_id`, `tests_passed`, `tests_failed`, `total_score` (out of 20, scaled from test pass rate).

Run the grader after writing it. Do not modify student files in this stage.

## Stage 4 — Logic-change audit (per problem)

For each student with status `repaired`, compare `raw/<student_id>.txt` against `fixed/<student_id>.py` and the diff. If any change actually altered control flow, conditions, return values, or data structures, write `audit/<student_id>.md` and downgrade status to `needs-manual-review`. Otherwise write a short audit confirming no logic changes.

## Final output

Print a per-problem summary plus an overall summary:

- Per problem: total students, count by final status, path to `results/summary.csv`, list of flagged IDs.
- Overall: students missing one or both mandatory problems, students who attempted the bonus problem (problem 3).

STOP and ask me before:
- Continuing past stage 0 (confirm extraction counts and language detection).
- Running stage 3 (I need to give you function signatures and `test_cases.json`).
- Doing anything destructive.
- Continuing if more than 20% of any problem's submissions end up flagged for manual review.