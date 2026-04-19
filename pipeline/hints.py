"""Heuristic feedback generator: given a student's test results + fixed source,
produce a short "likely mistake / suggested fix" markdown section.

Rule-based, no LLM. Designed to be wrong sometimes — the report header says
"potential" mistake so a human grader can skim and override.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def _load_result(problem: str, sid: str, lang: str) -> dict | None:
    if lang == "java":
        p = ROOT / problem / "results" / f"{sid}_java.json"
        if p.exists():
            return json.load(open(p, encoding="utf-8"))
    p = ROOT / problem / "results" / f"{sid}.json"
    if p.exists():
        return json.load(open(p, encoding="utf-8"))
    return None


def _load_source(problem: str, sid: str, lang: str) -> str:
    if lang == "java":
        p = ROOT / problem / "java" / f"{sid}.java"
    else:
        p = ROOT / problem / "fixed" / f"{sid}.py"
    if p.exists():
        return p.read_text(encoding="utf-8", errors="replace")
    return ""


def _failed_names(res: dict) -> set[str]:
    return {r["name"] for r in res.get("results", []) if not r.get("passed")}


def _passed_names(res: dict) -> set[str]:
    return {r["name"] for r in res.get("results", []) if r.get("passed")}


# ------------------------------ Problem 1 ------------------------------

P1_ZERO_CASES = {"zeros_do_not_count_as_negative", "window_all_have_one_negative",
                 "large_array_all_valid"}
P1_NO_VALID_CASES = {"spec_example_2_no_valid", "k_equals_n_two_negs",
                     "all_negatives_k2", "two_negatives_adjacent_invalidate"}
P1_WITH_NEG_CASES = {"spec_example_1", "single_negative_anywhere",
                     "window_with_neg_still_best", "large_positive_overwhelms",
                     "negative_makes_sum_smaller_than_zero", "boundary_tie_k3",
                     "alternating_k3_invalid_half", "k_equals_n_one_neg",
                     "large_k_equals_len", "negative_at_end_valid"}
P1_K1_CASES = {"k_1_picks_max", "k_1_picks_max_including_negative_if_all_neg",
               "all_positive_k1", "single_element_array", "single_element_negative"}


def _hint_p1(res: dict, src: str) -> str:
    failed = _failed_names(res)
    passed = _passed_names(res)
    total = len(failed) + len(passed)
    err = (res.get("load_error") or "").strip()

    if err:
        first = err.splitlines()[0][:200]
        return (f"**Load error:** `{first}`\n\n"
                f"**Suggestion:** The function couldn't be imported — usually a syntax error or a "
                f"missing/misnamed `max_valid_window_sum(nums, k)` function. Check the signature matches exactly.")

    if not failed:
        return ""

    if len(passed) == 0:
        # Inspect source for clues
        if "def max_valid_window_sum" not in src and "max_valid_window_sum" not in src:
            return ("**Likely mistake:** The function is not named `max_valid_window_sum(nums, k)`, "
                    "so the grader could not find it.\n\n"
                    "**Suggestion:** Rename the function to `max_valid_window_sum(nums, k)` and make sure "
                    "it `return`s (not `print`s) the answer.")
        if re.search(r"\bprint\s*\(", src) and not re.search(r"\breturn\b", src):
            return ("**Likely mistake:** Uses `print(...)` instead of `return`, so the grader always sees `None`.\n\n"
                    "**Suggestion:** Replace the final `print(...)` with `return ...`.")
        return ("**Likely mistake:** Every test returned the wrong value — the core window logic is off.\n\n"
                "**Suggestion:** Re-read the spec: slide a window of size `k`, count how many elements are "
                "strictly negative (`x < 0`, not `<= 0`), keep windows with at most one negative, and track "
                "the maximum sum. Return `0` only when no valid window exists.")

    hints = []

    zero_fails = failed & P1_ZERO_CASES
    if zero_fails and not (passed & P1_ZERO_CASES) == P1_ZERO_CASES:
        if re.search(r"<\s*=\s*0", src) or re.search(r"\bif\s+\w+\s*<=\s*0", src):
            hints.append(("Treats `0` as negative (uses `<= 0` when counting negatives).",
                          "Change the negative check to `x < 0` — zero is not negative per the spec."))
        elif zero_fails:
            hints.append(("Likely miscounts zero as negative in the per-window negative count.",
                          "Use a strict `x < 0` check when counting negatives in each window."))

    nv_fails = failed & P1_NO_VALID_CASES
    if nv_fails:
        if re.search(r"=\s*float\(['\"]-inf", src) or "-inf" in src or "-math.inf" in src.lower():
            hints.append(("Initializes the running max to `-inf` and returns it directly, so when no valid "
                          "window exists the function returns `-inf` (or a negative number) instead of `0`.",
                          "After the loop, if the max was never updated, return `0` instead of the sentinel."))
        else:
            hints.append(("When no valid window exists, the function doesn't return `0` as required.",
                          "Track whether any valid window was seen; if none, `return 0`."))

    wn_fails = failed & P1_WITH_NEG_CASES
    if wn_fails and len(wn_fails) >= 3:
        # Student probably rejects any window with a negative
        if re.search(r"if\s+[^\n]*<\s*0[^\n]*:\s*\n\s*continue", src) or \
           re.search(r"all\s*\(\s*\w+\s*>=?\s*0", src):
            hints.append(("Rejects every window that contains any negative number.",
                          "The spec allows **at most one** negative per window — count negatives "
                          "and accept windows with `count <= 1`, not `count == 0`."))
        elif re.search(r"<\s*1\b", src) and "negative" not in src.lower():
            hints.append(("The negative-count threshold may be `< 1` (i.e., zero negatives) instead of `<= 1`.",
                          "Change the window-validity check to `neg_count <= 1`."))

    k1_fails = failed & P1_K1_CASES
    if k1_fails and len(k1_fails) >= 2 and not hints:
        hints.append(("Edge cases with `k == 1` or single-element arrays fail.",
                      "A window of size 1 always has at most one negative, so it is always valid; "
                      "make sure your logic handles `k = 1` and never skips the last window."))

    # Off-by-one on window iteration
    if re.search(r"for\s+\w+\s+in\s+range\s*\(\s*len\s*\([^)]+\)\s*-\s*k\s*\)", src):
        hints.append(("Window loop uses `range(len(nums) - k)` which skips the last window.",
                      "Use `range(len(nums) - k + 1)` so the final window starting at index `n-k` is included."))

    if not hints:
        # Generic: pick the first failing case
        first = next(iter(failed))
        r = next((x for x in res["results"] if x["name"] == first), None)
        if r:
            hints.append((f"First failing case `{first}`: expected `{r['expected']}`, got `{r['got']}`.",
                          "Trace through this case by hand to spot where your logic diverges."))

    out = [f"- **Possible issue:** {h}\n  **Suggestion:** {s}" for h, s in hints[:3]]
    return "\n".join(out)


# ------------------------------ Problem 2 ------------------------------

P2_DUPLICATE_CASES = {"duplicates", "all_pairs_valid", "large_array_all_valid",
                      "all_same_value_large", "duplicates_boundary"}
P2_NEGATIVE_CASES = {"negatives_sorted", "all_negatives", "zero_target_with_negatives",
                     "mixed_neg_pos", "negative_T"}
P2_BOUNDARY_CASES = {"two_elements_equal_T", "spec_example_1", "duplicates_boundary",
                     "exact_target_hit"}


def _hint_p2(res: dict, src: str) -> str:
    failed = _failed_names(res)
    passed = _passed_names(res)
    err = (res.get("load_error") or "").strip()

    if err:
        first = err.splitlines()[0][:200]
        return (f"**Load error:** `{first}`\n\n"
                f"**Suggestion:** The function couldn't be imported — check the signature is exactly "
                f"`count_pairs(nums, T)` and that there's no stray top-level code causing an error.")

    if not failed:
        return ""

    if len(passed) == 0:
        if "count_pairs" not in src:
            return ("**Likely mistake:** The function is not named `count_pairs(nums, T)`.\n\n"
                    "**Suggestion:** Rename to `count_pairs(nums, T)` and `return` (not `print`) the count.")
        if re.search(r"\bprint\s*\(", src) and not re.search(r"\breturn\b", src):
            return ("**Likely mistake:** Uses `print(...)` instead of `return`, so the grader sees `None`.\n\n"
                    "**Suggestion:** Replace `print(...)` with `return ...`.")
        return ("**Likely mistake:** Every case returned the wrong count.\n\n"
                "**Suggestion:** Count index pairs `(i, j)` with `i < j` where `nums[i] + nums[j] <= T`. "
                "A simple double loop `for i in range(n): for j in range(i+1, n)` is fine.")

    hints = []

    # Off-by-one / strict inequality
    bd = failed & P2_BOUNDARY_CASES
    if bd and re.search(r"<\s*T\b|<\s*t\b", src) and not re.search(r"<=\s*T\b|<=\s*t\b", src):
        hints.append(("Uses strict `<` against `T` instead of `<=`, so pairs that sum exactly to `T` are missed.",
                      "Change the condition to `nums[i] + nums[j] <= T`."))

    # Duplicates - using set
    dup = failed & P2_DUPLICATE_CASES
    if dup:
        if re.search(r"\bset\s*\(", src):
            hints.append(("Uses a `set(...)` which drops duplicate values, so arrays like `[2,2,2,2]` "
                          "are undercounted.",
                          "Count by **index pairs**, not value pairs. Iterate `i` from `0..n-1` and "
                          "`j` from `i+1..n-1` over the original list."))
        elif re.search(r"\.count\s*\(", src) or "combinations" in src:
            hints.append(("Counts by distinct values instead of index pairs, so duplicates collapse.",
                          "Iterate over indices `(i, j)` with `i < j` on the original list."))

    # Double counting
    if not dup and failed:
        # Check if student's output is 2x expected for first failed case
        doubled = 0
        for r in res.get("results", []):
            if not r.get("passed") and isinstance(r.get("got"), int) and isinstance(r.get("expected"), int):
                if r["expected"] > 0 and r["got"] == 2 * r["expected"]:
                    doubled += 1
        if doubled >= 2:
            hints.append(("Results are exactly double the expected count — both `(i, j)` and `(j, i)` "
                          "are being counted.",
                          "Restrict the inner loop to `j in range(i+1, n)` so each unordered pair is counted once."))

    # Negative handling
    neg = failed & P2_NEGATIVE_CASES
    if neg and len(neg) >= 2 and not any("negative" in h.lower() for h, _ in hints):
        if re.search(r">\s*0|>=\s*0", src):
            hints.append(("Assumes positive values (filters with `> 0` / `>= 0`), so negative inputs and "
                          "negative `T` fail.",
                          "Remove the positivity filter — the spec allows any integers."))
        else:
            hints.append(("Test cases involving negative numbers or a negative `T` fail.",
                          "Check that the comparison `nums[i] + nums[j] <= T` works for negative sums; "
                          "don't assume values are non-negative."))

    # Index bounds
    if re.search(r"for\s+j\s+in\s+range\s*\(\s*i\s*\)", src):
        hints.append(("Inner loop uses `range(i)` so it only pairs earlier indices, potentially missing pairs.",
                      "Use `for j in range(i+1, len(nums))` to pair each `i` with every later index."))

    if not hints:
        first = next(iter(failed))
        r = next((x for x in res["results"] if x["name"] == first), None)
        if r:
            hints.append((f"First failing case `{first}`: expected `{r['expected']}`, got `{r['got']}`.",
                          "Hand-trace this case and check your loop bounds and comparison."))

    out = [f"- **Possible issue:** {h}\n  **Suggestion:** {s}" for h, s in hints[:3]]
    return "\n".join(out)


# ------------------------------ entry point ------------------------------

_CASES_CACHE: dict[str, dict] = {}


def _case_args(problem: str, name: str):
    if problem not in _CASES_CACHE:
        p = ROOT / problem / "test_cases.json"
        if p.exists():
            data = json.load(open(p, encoding="utf-8"))
            _CASES_CACHE[problem] = {c["name"]: c for c in data.get("cases", [])}
        else:
            _CASES_CACHE[problem] = {}
    return _CASES_CACHE[problem].get(name, {}).get("args")


def _failed_block(problem: str, res: dict) -> str:
    rows = [r for r in res.get("results", []) if not r.get("passed")]
    if not rows:
        return ""
    lines = ["**Failed cases:**", ""]
    for r in rows:
        args = _case_args(problem, r["name"])
        args_s = f"input={json.dumps(args)}" if args is not None else "input=?"
        lines.append(
            f"- `{r['name']}`: {args_s}, expected `{r.get('expected')!r}`, got `{r.get('got')!r}`"
        )
    return "\n".join(lines)


def hint_for(problem: str, sid: str, lang: str) -> str:
    """Return a markdown block (no leading heading) describing the likely mistake.
    Empty string if everything passed or no result available.
    """
    if lang == "pseudocode":
        return "_Pseudocode submission — manual grading; no auto-analysis._"
    res = _load_result(problem, sid, lang)
    if res is None:
        return ""
    src = _load_source(problem, sid, lang)
    if problem == "problem1":
        body = _hint_p1(res, src)
    elif problem == "problem2":
        body = _hint_p2(res, src)
    else:
        return ""
    if not body:
        return ""
    failed = _failed_block(problem, res)
    return f"{failed}\n\n{body}" if failed else body
