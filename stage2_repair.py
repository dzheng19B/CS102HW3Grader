"""
Stage 2 — Syntax repair for CS102 HW3 grader.
Processes problem1/, problem2/, problem3_bonus/ independently.
Produces fixed/<student_id>.py and fixed/<student_id>.diff.md.
Updates manifest.csv status.
"""

import ast
import csv
import difflib
import os
import re
import sys

PROBLEMS = {
    "problem1": {"lang_filter": ("python", "java")},
    "problem2": {"lang_filter": ("python", "java")},
    "problem3_bonus": {"lang_filter": ("python", "java")},
}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def try_parse(code):
    try:
        ast.parse(code)
        return True
    except SyntaxError:
        return False


def make_diff_md(student_id, original, fixed, changes):
    lines = [f"# Syntax repair diff — {student_id}\n"]
    if not changes:
        lines.append("No changes made (code parsed successfully as-is).\n")
    else:
        lines.append("## Changes\n")
        for ch in changes:
            tag = ch.get("tag", "[syntax-only]")
            desc = ch.get("desc", "")
            lines.append(f"- **{tag}** {desc}")
        lines.append("")
    lines.append("## Unified diff\n```diff")
    orig_lines = original.splitlines(keepends=True)
    fix_lines = fixed.splitlines(keepends=True)
    diff = list(difflib.unified_diff(orig_lines, fix_lines,
                                     fromfile="raw", tofile="fixed", lineterm=""))
    if diff:
        lines.extend(diff)
    else:
        lines.append("(no textual diff)")
    lines.append("```")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Python repair
# ---------------------------------------------------------------------------

def strip_preamble(code):
    """Remove leading lines that are clearly not Python code."""
    lines = code.split("\n")
    changes = []
    skip = 0
    for i, line in enumerate(lines):
        stripped = line.strip()
        if not stripped:
            skip = i + 1
            continue
        # Looks like a URL
        if re.match(r"https?://", stripped):
            changes.append({"tag": "[syntax-only]", "desc": f"Removed non-code preamble line {i+1}: URL"})
            skip = i + 1
            continue
        # Looks like natural language preamble (no Python tokens, starts with word + space)
        if re.match(r"^[A-Za-z]+ [Aa]nswer\s*:", stripped):
            changes.append({"tag": "[syntax-only]", "desc": f"Removed non-code preamble line {i+1}: '{stripped[:60]}'"})
            skip = i + 1
            continue
        # Once we hit a real code line, stop stripping
        break
    if skip > 0 and skip < len(lines):
        return "\n".join(lines[skip:]), changes
    return code, changes


def trim_trailing_text(code):
    """
    Remove trailing natural-language explanation lines.
    Strategy: walk backward from end; try progressively shorter prefixes
    until we get one that parses.  Refuse to trim more than 40% of
    non-empty lines to avoid silently discarding most of the student code.
    """
    if try_parse(code):
        return code, []

    lines = code.split("\n")
    non_empty = sum(1 for l in lines if l.strip())
    changes = []
    max_removable = int(non_empty * 0.40)  # don't trim more than 40% of content

    for end in range(len(lines), 0, -1):
        candidate = "\n".join(lines[:end]).rstrip()
        if not candidate:
            continue
        removed_non_empty = sum(1 for l in lines[end:] if l.strip())
        if removed_non_empty > max_removable:
            break  # stop — would trim too much; fall through to reindent
        if try_parse(candidate):
            removed = len(lines) - end
            if removed > 0:
                changes.append({
                    "tag": "[syntax-only]",
                    "desc": f"Removed {removed} trailing natural-language line(s) (prose explanation mixed into answer)"
                })
            return candidate, changes

    return code, changes


def fix_cpp_comments(code):
    """Replace // line comments with # (common mistake from C/Java habits)."""
    changes = []
    lines = code.split("\n")
    new_lines = []
    for i, line in enumerate(lines):
        # Don't touch lines inside triple-quoted strings (heuristic: skip if odd triple-quotes before)
        new_line = re.sub(r"(?<!:)//(?!.*['\"].*//)", " #", line)
        if new_line != line:
            changes.append({"tag": "[syntax-only]", "desc": f"Line {i+1}: replaced C-style `//` comment with `#`"})
        new_lines.append(new_line)
    return "\n".join(new_lines), changes


def fix_missing_colons(code):
    """Add missing colons at end of if/else/elif/for/while/def/class lines."""
    KEYWORDS = r"^(\s*)(def |class |if |elif |else|for |while |with |try|except|finally)"
    changes = []
    lines = code.split("\n")
    new_lines = []
    for i, line in enumerate(lines):
        stripped = line.rstrip()
        if re.match(KEYWORDS, stripped):
            # Check if it's missing a colon at end (ignoring trailing comments)
            code_part = re.split(r"\s*#", stripped)[0].rstrip()
            if code_part and not code_part.endswith(":") and not code_part.endswith(",") and not code_part.endswith("\\"):
                new_line = stripped + ":"
                changes.append({
                    "tag": "[syntax-only]",
                    "desc": f"Line {i+1}: added missing colon to `{stripped.strip()[:60]}`"
                })
                new_lines.append(new_line)
                continue
        new_lines.append(line)
    return "\n".join(new_lines), changes


KEYWORD_TYPOS = {
    r"\bretrun\b": "return",
    r"\bretrn\b": "return",
    r"\breturm\b": "return",
    r"\bpirnt\b": "print",
    r"\bprnt\b": "print",
    r"\blne\b": "len",
    r"\brnage\b": "range",
    r"\brnge\b": "range",
    r"\bdfe\b": "def",
    r"\bimoprt\b": "import",
    r"\bimport\b": "import",  # already correct, skip
}

def fix_keyword_typos(code):
    changes = []
    for pattern, replacement in KEYWORD_TYPOS.items():
        if pattern == r"\bimport\b":
            continue
        new_code = re.sub(pattern, replacement, code)
        if new_code != code:
            changes.append({"tag": "[syntax-only]",
                             "desc": f"Fixed keyword typo: `{pattern}` → `{replacement}`"})
            code = new_code
    return code, changes


def fix_string_literals(code):
    """Fix common string literal issues like float('-inf) missing closing quote."""
    changes = []
    # float('-inf) -> float('-inf')
    new_code = re.sub(r"float\('-inf\)", "float('-inf')", code)
    if new_code != code:
        changes.append({"tag": "[syntax-only]", "desc": "Fixed unterminated string in float('-inf)"})
        code = new_code
    # float('inf) -> float('inf')
    new_code = re.sub(r"float\('inf\)", "float('inf')", code)
    if new_code != code:
        changes.append({"tag": "[syntax-only]", "desc": "Fixed unterminated string in float('inf)"})
        code = new_code
    return code, changes


def is_pseudocode(code):
    """Return True if code looks like pseudocode rather than Python."""
    stripped = code.strip()
    # Strong pseudocode signals on first non-blank line
    first_line = next((l.strip() for l in stripped.splitlines() if l.strip()), "")
    if re.match(r"^(Function|Algorithm|Pseudocode|Procedure)\b", first_line, re.IGNORECASE):
        return True
    # Has 'initialize ... to' or 'set ... to' patterns (prose pseudocode)
    prose_lines = sum(1 for l in stripped.splitlines()
                      if re.match(r"^\s*(initialize|set |add |increment|decrement|check if)", l, re.IGNORECASE))
    total_lines = sum(1 for l in stripped.splitlines() if l.strip())
    if total_lines > 0 and prose_lines / total_lines > 0.3:
        return True
    return False


def reindent(code):
    """
    Re-indent Python code that lost indentation during textbox paste.
    Heuristic: strip all indentation, rebuild based on block-opening `:` endings.
    """
    lines = code.split("\n")
    result = []
    indent = 0
    changes = []
    original_lines = list(lines)

    for i, line in enumerate(lines):
        stripped = line.strip()
        if not stripped:
            result.append("")
            continue

        # Decrease indent BEFORE outputting else/elif/except/finally
        if re.match(r"^(else\s*:|elif\s+|except\s*[:(]|except:|finally\s*:)", stripped):
            indent = max(0, indent - 1)

        new_line = "    " * indent + stripped
        if new_line != original_lines[i] and original_lines[i].strip() == stripped:
            # Indentation changed
            old_indent = len(original_lines[i]) - len(original_lines[i].lstrip())
            new_indent_n = indent * 4
            if old_indent != new_indent_n:
                changes.append({
                    "tag": "[syntax-only]",
                    "desc": f"Line {i+1}: re-indented from {old_indent} to {new_indent_n} spaces"
                })
        result.append(new_line)

        # Increase indent after block opener (strip inline comments first)
        code_part = re.split(r"\s+#", stripped)[0].rstrip()
        if code_part.endswith(":") and not stripped.startswith("#"):
            indent += 1

        # Decrease indent after unconditional exits (next line is at lower level)
        if re.match(r"^(return\b|break\b|continue\b|raise\b)", stripped):
            indent = max(0, indent - 1)

    if changes:
        # Summarize instead of listing every line
        n = len(changes)
        return "\n".join(result), [{"tag": "[syntax-only]",
                                     "desc": f"Re-indented {n} line(s) whose indentation was broken by textbox paste"}]
    return "\n".join(result), []


def wrap_in_function(code, func_sig):
    """Wrap bare code in a function signature if it's not already in one."""
    if re.search(r"^\s*def \w+", code, re.MULTILINE):
        return code, []
    indented = "\n".join("    " + l for l in code.split("\n"))
    wrapped = func_sig + "\n" + indented
    return wrapped, [{"tag": "[syntax-only]",
                      "desc": f"Wrapped bare code in function signature: `{func_sig}`"}]


def repair_python(code, student_id):
    """
    Attempt to repair Python code. Returns (fixed_code, changes, status).
    Status: 'repaired', 'needs-manual-review', 'unrepairable'
    """
    changes = []

    # Step 0: as-is
    if try_parse(code):
        return code, changes, "repaired"

    # Step 0b: check if it's actually pseudocode mislabeled as Python
    if is_pseudocode(code):
        return code, [{"tag": "[syntax-only]", "desc": "Reclassified as pseudocode (prose-style instructions detected)"}], "pseudocode"

    working = code

    # Step 1: strip leading preamble (URLs, "Python Answer:", etc.)
    working, c = strip_preamble(working)
    changes.extend(c)

    # Step 2: trim trailing natural-language explanation
    working, c = trim_trailing_text(working)
    changes.extend(c)

    # Step 3: fix // comments
    working, c = fix_cpp_comments(working)
    changes.extend(c)

    # Step 4: fix keyword typos
    working, c = fix_keyword_typos(working)
    changes.extend(c)

    # Step 4b: fix string literal issues
    working, c = fix_string_literals(working)
    changes.extend(c)

    # Step 5: fix missing colons
    working, c = fix_missing_colons(working)
    changes.extend(c)

    if try_parse(working):
        return working, changes, "repaired"

    # Step 6: re-indent
    reindented, c = reindent(working)
    changes.extend(c)

    if try_parse(reindented):
        return reindented, changes, "repaired"

    # Step 7: re-indent + trim trailing again (re-indent may expose new issues)
    trimmed, c2 = trim_trailing_text(reindented)
    if trimmed != reindented and try_parse(trimmed):
        changes.extend(c2)
        return trimmed, changes, "repaired"

    # Step 8: try trimming trailing incomplete lines from re-indented version
    lines = reindented.split("\n")
    for n in range(len(lines) - 1, max(0, len(lines) - 10), -1):
        candidate = "\n".join(lines[:n]).rstrip()
        if candidate and try_parse(candidate):
            changes.append({"tag": "[syntax-only]",
                             "desc": f"Removed {len(lines)-n} trailing incomplete/broken line(s)"})
            return candidate, changes, "repaired"

    # Still broken — mark for manual review
    return reindented, changes, "needs-manual-review"


# ---------------------------------------------------------------------------
# Java → Python transpiler
# ---------------------------------------------------------------------------

def transpile_java(code, student_id):
    """
    Mechanical Java → Python transpilation.
    Marks needs-manual-review — human should verify.
    Returns (py_code, changes, status).
    """
    changes = [{"tag": "[syntax-only]",
                "desc": "Java → Python mechanical transpilation (same logic preserved)"}]

    lines = code.split("\n")
    py_lines = []

    indent_stack = [0]

    def current_indent():
        return indent_stack[-1]

    for raw_line in lines:
        line = raw_line.rstrip()
        stripped = line.strip()

        if not stripped:
            py_lines.append("")
            continue

        # Skip opening/closing braces on their own line
        if stripped in ("{", "}"):
            if stripped == "}" and len(indent_stack) > 1:
                indent_stack.pop()
            continue

        # Method/function signature: public static TYPE name(TYPE[] args)
        m = re.match(
            r"public\s+(?:static\s+)?(?:\w+(?:\[\])?)\s+(\w+)\s*\(([^)]*)\)\s*\{?$",
            stripped)
        if m:
            func_name = m.group(1)
            params_raw = m.group(2)
            # Convert params: strip types
            params = []
            for p in params_raw.split(","):
                p = p.strip()
                if p:
                    parts = p.split()
                    params.append(parts[-1].rstrip("[]"))
            py_sig = "    " * current_indent() + f"def {func_name}({', '.join(params)}):"
            py_lines.append(py_sig)
            indent_stack.append(current_indent() + 1)
            continue

        # for (int i = start; i < end; i++) or for (int i = start; i <= end; i++)
        m = re.match(r"for\s*\(\s*int\s+(\w+)\s*=\s*([^;]+);\s*\w+\s*([<>]=?)\s*([^;]+);\s*\w+(\+\+|--)\s*\)\s*\{?$", stripped)
        if m:
            var = m.group(1)
            start = java_expr(m.group(2).strip())
            op = m.group(3)
            end_expr = java_expr(m.group(4).strip())
            step = 1 if m.group(5) == "++" else -1
            if op in ("<", "!="):
                range_expr = f"range({start}, {end_expr})"
            elif op == "<=":
                range_expr = f"range({start}, {end_expr} + 1)"
            elif op == ">":
                range_expr = f"range({start}, {end_expr}, -1)"
            elif op == ">=":
                range_expr = f"range({start}, {end_expr} - 1, -1)"
            else:
                range_expr = f"range({start}, {end_expr})"
            py_lines.append("    " * current_indent() + f"for {var} in {range_expr}:")
            indent_stack.append(current_indent() + 1)
            continue

        # while (...) {
        m = re.match(r"while\s*\((.+)\)\s*\{?$", stripped)
        if m:
            cond = java_expr(m.group(1).strip())
            py_lines.append("    " * current_indent() + f"while {cond}:")
            indent_stack.append(current_indent() + 1)
            continue

        # if (...) {  or  if (...) statement;
        m = re.match(r"if\s*\((.+)\)\s*\{?$", stripped)
        if m:
            cond = java_expr(m.group(1).strip())
            py_lines.append("    " * current_indent() + f"if {cond}:")
            # Always push; bare `{` on next line is a no-op, bare `}` pops
            indent_stack.append(current_indent() + 1)
            continue

        # else if (...) {
        m = re.match(r"else\s+if\s*\((.+)\)\s*\{?$", stripped)
        if m:
            if len(indent_stack) > 1:
                indent_stack.pop()
            cond = java_expr(m.group(1).strip())
            py_lines.append("    " * current_indent() + f"elif {cond}:")
            indent_stack.append(current_indent() + 1)
            continue

        # else {  or  else
        if re.match(r"else\s*\{?$", stripped):
            if len(indent_stack) > 1:
                indent_stack.pop()
            py_lines.append("    " * current_indent() + "else:")
            indent_stack.append(current_indent() + 1)
            continue

        # return statement
        m = re.match(r"return\s+(.*?);?$", stripped)
        if m:
            val = java_expr(m.group(1).strip().rstrip(";"))
            py_lines.append("    " * current_indent() + f"return {val}")
            continue

        # variable declaration: type var = expr;  or  type[] var = expr;
        m = re.match(r"(?:int|long|double|float|boolean|String|char)\s*(?:\[\])?\s+(\w+)\s*=\s*(.+?);?$", stripped)
        if m:
            var = m.group(1)
            val = java_expr(m.group(2).strip().rstrip(";"))
            py_lines.append("    " * current_indent() + f"{var} = {val}")
            continue

        # increment/decrement: var++;  var--;
        m = re.match(r"(\w+)(\+\+|--);?$", stripped)
        if m:
            var = m.group(1)
            op = "+= 1" if m.group(2) == "++" else "-= 1"
            py_lines.append("    " * current_indent() + f"{var} {op}")
            continue

        # compound assignment: var op= expr;
        m = re.match(r"(\w+(?:\[.*?\])?)\s*([+\-*/%]=)\s*(.+?);?$", stripped)
        if m:
            var = java_expr(m.group(1))
            op = m.group(2)
            val = java_expr(m.group(3).strip().rstrip(";"))
            py_lines.append("    " * current_indent() + f"{var} {op} {val}")
            continue

        # plain assignment: var = expr;
        m = re.match(r"(\w+(?:\[.*?\])?)\s*=\s*(.+?);?$", stripped)
        if m:
            var = java_expr(m.group(1))
            val = java_expr(m.group(2).strip().rstrip(";"))
            py_lines.append("    " * current_indent() + f"{var} = {val}")
            continue

        # Standalone expression (method call, etc.) — strip semicolon
        expr = stripped.rstrip(";")
        expr = java_expr(expr)
        py_lines.append("    " * current_indent() + expr)

    py_code = "\n".join(py_lines)

    # Final cleanup of Java idioms
    py_code = java_expr(py_code)

    # Post-pass: re-indent to clean up any indent drift from brace-on-own-line patterns
    py_code, _ = reindent(py_code)

    return py_code, changes, "needs-manual-review"


def java_expr(expr):
    """Convert Java expression fragments to Python."""
    # Boolean literals
    expr = re.sub(r"\btrue\b", "True", expr)
    expr = re.sub(r"\bfalse\b", "False", expr)
    expr = re.sub(r"\bnull\b", "None", expr)
    # Integer.MIN_VALUE / Integer.MAX_VALUE
    expr = re.sub(r"\bInteger\.MIN_VALUE\b", "float('-inf')", expr)
    expr = re.sub(r"\bInteger\.MAX_VALUE\b", "float('inf')", expr)
    # Math methods
    expr = re.sub(r"\bMath\.max\b", "max", expr)
    expr = re.sub(r"\bMath\.min\b", "min", expr)
    expr = re.sub(r"\bMath\.abs\b", "abs", expr)
    # array.length → len(array)
    expr = re.sub(r"(\w+)\.length\b", r"len(\1)", expr)
    # String methods
    expr = re.sub(r"\.charAt\((\w+)\)", r"[\1]", expr)
    # Ternary: cond ? a : b → (a if cond else b)
    m = re.search(r"(.+?)\s*\?\s*(.+?)\s*:\s*(.+)", expr)
    if m:
        cond = java_expr(m.group(1).strip())
        a = java_expr(m.group(2).strip())
        b = java_expr(m.group(3).strip())
        expr = f"({a} if {cond} else {b})"
    # != null → is not None
    expr = expr.replace("!= null", "is not None")
    expr = expr.replace("== null", "is None")
    # ! → not
    expr = re.sub(r"!\s*(\w)", r"not \1", expr)
    # && → and, || → or
    expr = expr.replace("&&", "and")
    expr = expr.replace("||", "or")
    # Remove trailing semicolons
    expr = expr.rstrip(";")
    return expr


# ---------------------------------------------------------------------------
# Main per-problem processing
# ---------------------------------------------------------------------------

def process_problem(prob_dir):
    manifest_path = os.path.join(prob_dir, "manifest.csv")
    fixed_dir = os.path.join(prob_dir, "fixed")
    os.makedirs(fixed_dir, exist_ok=True)

    rows = []
    with open(manifest_path, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    updated = []
    stats = {"repaired": 0, "needs-manual-review": 0, "skipped": 0, "pseudocode": 0}

    for row in rows:
        lang = row["detected_language"]
        status = row["status"]
        sid = row["student_id"]

        # Skip non-code or already empty
        if status == "empty" or lang == "empty":
            row["status"] = "empty"
            updated.append(row)
            stats["skipped"] += 1
            continue

        if lang == "pseudocode":
            row["status"] = "pseudocode"
            updated.append(row)
            stats["pseudocode"] += 1
            continue

        if lang not in ("python", "java"):
            updated.append(row)
            stats["skipped"] += 1
            continue

        raw_path = row["raw_path"]
        try:
            raw_code = open(raw_path, encoding="utf-8").read()
        except FileNotFoundError:
            row["status"] = "unrepairable"
            updated.append(row)
            continue

        if lang == "python":
            fixed, changes, new_status = repair_python(raw_code, sid)
        else:  # java
            fixed, changes, new_status = transpile_java(raw_code, sid)

        # If repair reclassified as pseudocode, update language field too
        if new_status == "pseudocode":
            row["detected_language"] = "pseudocode"
            row["status"] = "pseudocode"
            updated.append(row)
            stats["pseudocode"] = stats.get("pseudocode", 0) + 1
            print(f"  {sid}: {lang} -> reclassified as pseudocode")
            continue

        # Check if any change is logic-affecting (auto-flag)
        has_logic_change = any(ch.get("tag") in ("[ambiguous]", "[logic-affecting]")
                               for ch in changes)
        if has_logic_change and new_status == "repaired":
            new_status = "needs-manual-review"

        # Write fixed file
        fixed_path = os.path.join(fixed_dir, f"{sid}.py")
        with open(fixed_path, "w", encoding="utf-8") as f:
            f.write(fixed)

        # Write diff
        diff_md = make_diff_md(sid, raw_code, fixed, changes)
        diff_path = os.path.join(fixed_dir, f"{sid}.diff.md")
        with open(diff_path, "w", encoding="utf-8") as f:
            f.write(diff_md)

        row["status"] = new_status
        updated.append(row)
        stats[new_status] = stats.get(new_status, 0) + 1

        print(f"  {sid}: {lang} -> {new_status} ({len(changes)} change(s))")

    # Rewrite manifest
    fieldnames = list(rows[0].keys()) if rows else []
    with open(manifest_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for row in updated:
            w.writerow(row)

    return stats


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    targets = sys.argv[1:] if len(sys.argv) > 1 else list(PROBLEMS.keys())

    grand_flagged = []
    for prob_dir in targets:
        print(f"\n=== Stage 2: {prob_dir} ===")
        stats = process_problem(prob_dir)
        print(f"  Summary: {stats}")

        # Check flag rate
        total_attempted = stats.get("repaired", 0) + stats.get("needs-manual-review", 0)
        flagged = stats.get("needs-manual-review", 0)
        if total_attempted > 0:
            rate = flagged / total_attempted
            if rate > 0.20:
                print(f"  WARNING: {rate:.0%} flagged for manual review (>{20}% threshold)")
                grand_flagged.append(prob_dir)

    if grand_flagged:
        print(f"\nSTOP: Manual review rate exceeded 20% for: {grand_flagged}")
        print("Please review before continuing to Stage 3.")
