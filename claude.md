# Mock Technical Interview Grading Pipeline

Be concise when responding.

You are grading Brightspace file-upload submissions from a paired mock technical interview for ~80 students. Each student solved one LeetCode-style problem and submitted their code + interviewer evaluation as uploaded files (txt, py, pdf, doc, etc). The pipeline extracts code, detects the problem, repairs syntax, and generates reports.

## Directory layout

```
mock_raw_unzipped/         — unzipped Brightspace file-upload download (input)
inputs/
  students.csv             — roster (written by stage 1)
  manifest.csv             — global manifest: student, problem, language, status
pipeline/
  stage0_inspect.py        — inspection / sanity check of unzipped submissions
  stage1_split.py          — extract code from uploads into per-problem folders
  stage2_repair.py         — Python syntax repair + force-runnable fallback
  stage3_separate_langs.py — split fixed/ into python/, java/, pseudocode/
  stage4_audit.py          — flag logic-affecting / ambiguous changes
  stage5_breakdown.py      — per-student score breakdown report
  stage6_full_dump.py      — single continuous report with every student's full data
  stage7_split_reports.py  — split the full dump into per-topic reports
  java_grader.py           — native Java grader (javac + java)
  verify_tests.py          — sanity-check test_cases.json vs. reference solutions
reports/                   — generated reports
<problem_name>/            — per-problem folders (auto-created by stage 1)
  raw/<bid>.txt            — full document text, untouched
  code/<bid>.py|.java      — extracted candidate code with indentation repair
  manifest.csv             — per-problem manifest
CLAUDE.md                  — this file
```

Problem folders created by stage 1:
- `guess_number/` — Guess Number Higher or Lower (binary search)
- `longest_substring/` — Longest Substring Without Repeating Characters (sliding window)
- `contains_nearby_duplicate/` — Contains Nearby Duplicate (hash map)
- `merge_two_sorted_lists/` — Merge Two Sorted Lists (linked list)
- `eval_rpn/` — Evaluate Reverse Polish Notation (stack)
- `unknown_problem/` — undetectable problem (DOC failures, image-only, etc.)

All pipeline scripts resolve paths via `ROOT = Path(__file__).resolve().parent.parent`.

## Input format

Brightspace file-upload zip. Folder structure:
`{brightspace_id}-241554 - {LastName}, {FirstName} - {Month} {Day}, {Year} {Time}/`

Each folder contains uploaded files: .txt, .py, .pdf, .doc, .docx, .rtf, .ipynb, .jpeg, .heic, etc.

Files typically contain BOTH an interviewer evaluation form AND candidate code. Stage 1 extracts only the candidate code section.

## Problem set

Each student solved ONE of these problems (assigned by their partner pair):

| Problem | Folder | Expected function | Params |
|---|---|---|---|
| Guess Number Higher or Lower | `guess_number/` | `guessNumber` | `n` |
| Longest Substring Without Repeating Characters | `longest_substring/` | `lengthOfLongestSubstring` | `s` |
| Contains Nearby Duplicate | `contains_nearby_duplicate/` | `containsNearbyDuplicate` | `nums, k` |
| Merge Two Sorted Lists | `merge_two_sorted_lists/` | `mergeTwoLists` | `list1, list2` |
| Evaluate Reverse Polish Notation | `eval_rpn/` | `evalRPN` | `tokens` |

## Core rules

1. **Latest submission only.** Multiple uploads per student → pick folder with latest timestamp.
2. **Detect problem from code content.** Function name patterns + title patterns. Fall back to full document text if code-only detection fails.
3. **Extract candidate code, not interviewer form.** Look for "Candidate Form" markers, then find code. Strip leading prose, problem descriptions, docstrings.
4. **Indentation repair on extraction.** Handle: tabs→4spaces, flat code (def body at col 0), mixed indentation. Preserve existing relative indent when present.
5. **Never modify student logic.** Only touch tokens that prevent parsing.
6. **Every change logged** with tags: `[syntax-only]`, `[ambiguous]`, `[logic-affecting]`.
7. **Non-text files (images, failed DOC extraction) → manual-review.**
8. **Stages are sequential and idempotent.**

## Stages

### Stage 0 — Inspect
`py pipeline/stage0_inspect.py` — parses folder names, counts students/file types, detects problems/languages, lists multi-submission students and image-only submissions. STOP for confirmation.

### Stage 1 — Extract and split
`py pipeline/stage1_split.py` — reads all file types (txt/py direct, docx/pdf/rtf via libraries, images flagged), extracts candidate code, repairs indentation, organizes into per-problem folders with raw/ and code/ subdirs. Writes manifests and students.csv.

### Stage 2+ — Same as HW4 pipeline
Syntax repair, language separation, auto-grading, audit, score breakdown, reports. These stages need adaptation for the new problem set and directory structure.

## STOP points

Ask before:
- Continuing past stage 0 (confirm extraction counts and problem detection).
- Running auto-graders (confirm function signatures and test_cases.json).
- Doing anything destructive.
- Continuing if more than 20% of any problem's submissions need manual review.
