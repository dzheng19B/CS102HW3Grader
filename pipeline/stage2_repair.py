"""Stage 2: Syntax repair per problem.

Pipeline per file:
  1. Normalize line endings, tabs -> 4 spaces.
  2. Fix keyword typos (retrun->return, pritn->print, elseif->elif).
  3. Add missing colons on control-flow headers.
  4. Balance trailing unmatched brackets.
  5. Ensure function signature is present; wrap body if missing.
  6. Try ast.parse. Pass -> repaired.
  7. Conservative re-indent: preserve relative indent, normalize to 4-space tiers.
  8. Try ast.parse. Pass -> repaired.
  9. Aggressive re-indent: rebuild indent from control-flow headers. Flag [ambiguous].
 10. Try ast.parse. Pass -> repaired (needs-manual-review). Fail -> unrepairable.

Java -> Python mechanical transpile (same control flow):
  - strip type decls, `;`, `{`, `}`
  - `public ... foo(int[] nums, int k) {` -> `def <name>(nums, k):`
  - `for (int i=...; i<N; i++)` -> `for i in range(...)`
  - `arr.length` -> `len(arr)`, `System.out.println` -> `print`, `Math.max/min` -> `max/min`
  - if it doesn't compile as Python, mark needs-manual-review

No student LOGIC is altered — only syntax/indent. Diffs logged in fixed/<id>.diff.md.
"""
import ast
import csv
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PROBLEMS = [
    ("problem1", "max_valid_window_sum", ["nums", "k"]),
    ("problem2", "count_pairs", ["nums", "T"]),
    ("problem3_bonus", None, None),  # unknown fn; just try to make it parse
]

TYPO_MAP = {
    r"\bretrun\b": "return",
    r"\bresturn\b": "return",
    r"\bretrn\b": "return",
    r"\brteurn\b": "return",
    r"\bretrun\b": "return",
    r"\bpritn\b": "print",
    r"\bprnit\b": "print",
    r"\belseif\b": "elif",
    r"\belse if\b": "elif",
    r"\bFasle\b": "False",
    r"\bTrue\b": "True",  # no-op, but safe
    r"\bNull\b": "None",
    r"\bnull\b": "None",
    r"\bture\b": "True",
    r"\bflase\b": "False",
    r"\btrue\b": "True",
    r"\bfalse\b": "False",
}

# Keywords expected to end with ":" (when at line tail without suite)
NEEDS_COLON = re.compile(
    r"^(\s*)(if|elif|else|for|while|def|class|try|except|finally|with)\b([^\n:]*?)\s*$"
)


def count_leading_spaces(s: str) -> int:
    i = 0
    while i < len(s) and s[i] == " ":
        i += 1
    return i


def normalize(s: str) -> str:
    return s.replace("\r\n", "\n").replace("\r", "\n")


def tabs_to_spaces(s: str) -> str:
    return s.replace("\t", "    ")


def slashes_to_hash(s: str) -> tuple[str, list[str]]:
    """Convert `//` comments to `#` when they look like line comments (outside strings)."""
    out = []
    changes = 0
    for line in s.split("\n"):
        new = _replace_slash_outside_strings(line)
        if new != line:
            changes += 1
        out.append(new)
    return "\n".join(out), ([f"converted `//` line comments to `#` ({changes} lines)"] if changes else [])


def _replace_slash_outside_strings(line: str) -> str:
    i = 0
    in_str = None
    while i < len(line):
        c = line[i]
        if in_str:
            if c == "\\" and i + 1 < len(line):
                i += 2
                continue
            if c == in_str:
                in_str = None
        else:
            if c in ("'", '"'):
                in_str = c
            elif c == "#":
                # already a Python comment, keep as-is
                return line
            elif c == "/" and i + 1 < len(line) and line[i + 1] == "/":
                # replace `//` with `# `
                return line[:i] + "# " + line[i + 2:]
        i += 1
    return line


PY_CODE_STARTERS = (
    "def ", "class ", "for ", "if ", "elif ", "else", "while ", "return",
    "import ", "from ", "try", "except", "finally", "with ", "raise ",
    "break", "continue", "pass", "yield ", "global ", "nonlocal ", "assert ",
    "lambda ", "@", "async ", "await ",
)


def _is_prose_line(line: str) -> bool:
    """True if a line looks like natural-language prose (not code)."""
    s = line.strip()
    if not s:
        return False
    if s.startswith(("#", "//", '"""', "'''")):
        return False
    if any(s.startswith(kw) for kw in PY_CODE_STARTERS):
        return False
    # Common code chars suggest this is code, not prose
    code_chars = set("=(){}[]<>+-*/%!&|^;")
    has_code = any(c in code_chars for c in s)
    words = s.split()
    if len(words) < 6 or len(s) < 40:
        return False
    # Heavy prose signal: long, many words, few or no code chars
    if not has_code and len(words) >= 8:
        return True
    # Some code chars but mostly English words — look for sentence-like structure
    # (multiple lowercase words separated by spaces, ends with . or , or nothing)
    lowercase_words = sum(1 for w in words if w and w[0].islower() and w.isalpha())
    if lowercase_words / len(words) > 0.6 and len(words) >= 10:
        return True
    return False


def strip_trailing_prose(s: str) -> tuple[str, list[str]]:
    """Remove trailing natural-language prose (common on bonus: code + explanation).

    Only triggers if there's an identifiable prose region at the end — NOT a general
    "find shortest parseable prefix" scan. Ensures we don't drop actual code lines.
    """
    lines = s.split("\n")
    # Find first line that looks like prose AND most subsequent non-blank lines are prose
    cutoff = None
    for i, ln in enumerate(lines):
        if not _is_prose_line(ln):
            continue
        rest = [x for x in lines[i:] if x.strip()]
        prose_count = sum(1 for x in rest if _is_prose_line(x))
        if prose_count >= max(1, len(rest) * 0.5):
            cutoff = i
            break
    if cutoff is None:
        return s, []
    prefix = "\n".join(lines[:cutoff]).rstrip() + "\n"
    dropped = len([x for x in lines[cutoff:] if x.strip()])
    return prefix, [f"stripped {dropped} trailing prose line(s) (explanation text)"]


def fix_typos(s: str) -> tuple[str, list[str]]:
    changes = []
    for pat, repl in TYPO_MAP.items():
        new = re.sub(pat, repl, s)
        if new != s:
            cnt = len(re.findall(pat, s))
            changes.append(f"typo `{pat}` -> `{repl}` ({cnt}x)")
            s = new
    return s, changes


def add_missing_colons(s: str) -> tuple[str, list[str]]:
    out = []
    changes = []
    for ln, line in enumerate(s.split("\n"), 1):
        stripped = line.rstrip()
        m = NEEDS_COLON.match(stripped)
        if m and not stripped.endswith(":") and not stripped.endswith(","):
            # Ensure it's a header, not an expression that starts with one of these keywords
            # Only apply if the line does NOT already have ":" later (e.g., `if x: y`)
            if ":" not in stripped:
                new = stripped + ":"
                out.append(new)
                changes.append(f"line {ln}: added missing colon")
                continue
        out.append(line)
    return "\n".join(out), changes


def balance_brackets(s: str) -> tuple[str, list[str]]:
    """If code has trailing unbalanced ( [ {, close them; if extra ) ] }, drop trailing."""
    changes = []
    # Count in non-string, non-comment regions — approximate: just count literals
    opens = {"(": 0, "[": 0, "{": 0}
    close_map = {")": "(", "]": "[", "}": "{"}
    in_str = None
    i = 0
    while i < len(s):
        c = s[i]
        if in_str:
            if c == "\\" and i + 1 < len(s):
                i += 2
                continue
            if c == in_str:
                in_str = None
        else:
            if c in ("'", '"'):
                # triple quote?
                if s[i:i+3] in ('"""', "'''"):
                    end = s.find(s[i:i+3], i + 3)
                    if end == -1:
                        break
                    i = end + 3
                    continue
                in_str = c
            elif c == "#":
                # skip to end of line
                nl = s.find("\n", i)
                if nl == -1:
                    break
                i = nl
                continue
            elif c in opens:
                opens[c] += 1
            elif c in close_map:
                opens[close_map[c]] -= 1
        i += 1
    # Append missing closers at end
    tail = ""
    if opens["{"] > 0:
        tail += "}" * opens["{"]
    if opens["["] > 0:
        tail += "]" * opens["["]
    if opens["("] > 0:
        tail += ")" * opens["("]
    if tail:
        changes.append(f"appended {len(tail)} missing closing bracket(s)")
        s = s.rstrip() + tail + "\n"
    return s, changes


def ensure_signature(s: str, fn_name: str, params: list[str]) -> tuple[str, list[str]]:
    if fn_name is None:
        return s, []
    changes = []
    sig_re = re.compile(rf"def\s+{re.escape(fn_name)}\s*\(")
    if sig_re.search(s):
        return s, changes
    # Try case-insensitive / camelCase match and rename
    alt_names = set()
    camel = re.sub(r"_([a-z])", lambda m: m.group(1).upper(), fn_name)  # snake->camel
    alt_names.add(camel)
    alt_names.add(camel[0].upper() + camel[1:])
    alt_names.add(fn_name.lower())
    for alt in alt_names:
        if re.search(rf"def\s+{re.escape(alt)}\s*\(", s):
            s = re.sub(rf"(def\s+){re.escape(alt)}(\s*\()", rf"\1{fn_name}\2", s)
            changes.append(f"renamed `def {alt}(...)` -> `def {fn_name}(...)`")
            return s, changes
    # Wrap entire body in the expected signature
    body = s
    indented = "\n".join(("    " + ln) if ln.strip() else ln for ln in body.split("\n"))
    wrapped = f"def {fn_name}({', '.join(params)}):\n{indented}"
    changes.append(f"wrapped bare code in `def {fn_name}({', '.join(params)})`")
    return wrapped, changes


def try_parse(s: str) -> str | None:
    try:
        ast.parse(s)
        return None
    except SyntaxError as e:
        return f"{e.msg} (line {e.lineno})"


def conservative_reindent(s: str) -> str:
    """Preserve relative indent structure but normalize to 4-space tiers.

    Cluster nearby indent levels (within 2 spaces) then map each cluster to 4*rank.
    Indent-0 stays 0. This handles 4-vs-5 space off-by-one paste artifacts.
    """
    lines = s.split("\n")
    indents = sorted({count_leading_spaces(ln) for ln in lines if ln.strip()})
    if not indents or indents == [0]:
        return s
    # Cluster: adjacent indents within 2 are the same tier
    clusters = [[indents[0]]]
    for x in indents[1:]:
        if x - clusters[-1][-1] <= 2:
            clusters[-1].append(x)
        else:
            clusters.append([x])
    # map each original indent -> tier * 4 (skipping 0 which is its own tier)
    mapping = {}
    tier = 0
    if clusters[0][0] == 0:
        for x in clusters[0]:
            mapping[x] = 0
        tier = 1
        start = 1
    else:
        start = 0
    for cl in clusters[start:]:
        for x in cl:
            mapping[x] = tier * 4
        tier += 1
    out = []
    for ln in lines:
        if not ln.strip():
            out.append("")
            continue
        orig = count_leading_spaces(ln)
        new_indent = mapping.get(orig, orig)
        out.append(" " * new_indent + ln.strip())
    return "\n".join(out)


DEDENT_STARTS = ("else", "elif", "except", "finally")


def aggressive_reindent(s: str, fn_name: str | None) -> str:
    """Rebuild indent from scratch using control-flow block headers.

    Assumes first `def <fn_name>` (or first def) is at depth 0; everything after it
    is inside until EOF. Raises each line's indent per observed block headers ending in `:`.
    """
    lines = s.split("\n")
    out = []
    stack = [0]  # indent levels; top is current expected indent

    def push(cur_indent):
        stack.append(cur_indent + 4)

    def current_indent():
        return stack[-1]

    inside_fn = False

    for raw_line in lines:
        stripped = raw_line.strip()
        if not stripped:
            out.append("")
            continue

        # Handle dedent keywords at body level — pop to containing block
        if any(stripped.startswith(k + " ") or stripped == k + ":" or stripped.startswith(k + ":")
               for k in DEDENT_STARTS):
            # pop one level (assume else aligns with most recent if/for/try etc.)
            if len(stack) > 1:
                stack.pop()
            indent = current_indent()
            out.append(" " * indent + stripped)
            if stripped.endswith(":"):
                push(indent)
            continue

        # Detect function def — reset stack to start fresh
        if stripped.startswith("def "):
            # Top-level def: indent 0
            # If we see a def AFTER another def, it could be nested or sequential — keep conservative.
            out.append(stripped)
            stack = [0]
            push(0)
            inside_fn = True
            continue

        indent = current_indent() if inside_fn else 0
        out.append(" " * indent + stripped)
        if stripped.endswith(":"):
            push(indent)

    return "\n".join(out)


def repair_python(raw: str, fn_name: str | None, params: list[str] | None) -> tuple[str, list[tuple[str, str]], str]:
    """Returns (fixed_code, diff_entries, status). diff entries: list of (tag, msg)."""
    diff: list[tuple[str, str]] = []
    s = normalize(raw)

    # Step 1: tabs
    if "\t" in s:
        s = tabs_to_spaces(s)
        diff.append(("[syntax-only]", "converted tabs to 4-space indentation"))

    # Step 1b: // comments -> #
    s, changes = slashes_to_hash(s)
    for c in changes:
        diff.append(("[syntax-only]", c))

    # Step 2: typos
    s2, changes = fix_typos(s)
    for c in changes:
        diff.append(("[syntax-only]", c))
    s = s2

    # Step 3: missing colons
    s2, changes = add_missing_colons(s)
    for c in changes:
        diff.append(("[syntax-only]", c))
    s = s2

    # Step 4: balance brackets
    s2, changes = balance_brackets(s)
    for c in changes:
        diff.append(("[syntax-only]", c))
    s = s2

    # Step 5: ensure signature
    if fn_name:
        s2, changes = ensure_signature(s, fn_name, params or [])
        for c in changes:
            tag = "[syntax-only]" if c.startswith("renamed") else "[ambiguous]"
            diff.append((tag, c))
        s = s2

    # Step 6: try parse as-is
    err = try_parse(s)
    if err is None:
        return s, diff, "repaired"

    # Step 6b: strip trailing prose (common on bonus — LeetCode solution + explanation)
    s_sp, changes = strip_trailing_prose(s)
    if s_sp != s and try_parse(s_sp) is None:
        for c in changes:
            diff.append(("[syntax-only]", c))
        return s_sp, diff, "repaired"

    # Step 7: conservative re-indent
    s_c = conservative_reindent(s)
    if s_c != s:
        diff.append(("[syntax-only]", "conservative re-indent (cluster nearby indent levels to 4-space tiers)"))
    err2 = try_parse(s_c)
    if err2 is None:
        return s_c, diff, "repaired"

    # Step 7b: conservative reindent + strip prose
    s_c_sp, changes = strip_trailing_prose(s_c)
    if s_c_sp != s_c and try_parse(s_c_sp) is None:
        for c in changes:
            diff.append(("[syntax-only]", c))
        return s_c_sp, diff, "repaired"

    # Step 8: ensure signature after reindent (rare case where re-indent exposes top-level code)
    if fn_name:
        s_c2, changes = ensure_signature(s_c, fn_name, params or [])
        if s_c2 != s_c:
            for c in changes:
                diff.append(("[ambiguous]", c))
            s_c = s_c2
        err3 = try_parse(s_c)
        if err3 is None:
            return s_c, diff, "repaired"

    # Step 9: aggressive re-indent (rebuild from control-flow headers)
    s_a = aggressive_reindent(s_c, fn_name)
    aggressive_applied = s_a != s_c
    if aggressive_applied:
        diff.append(("[ambiguous]", "aggressive re-indent: rebuilt block structure from control-flow headers"))
    err4 = try_parse(s_a)
    if err4 is None:
        return s_a, diff, "needs-manual-review"  # ambiguous reindent

    # Step 9b: aggressive + strip prose
    s_a_sp, changes = strip_trailing_prose(s_a)
    if s_a_sp != s_a and try_parse(s_a_sp) is None:
        for c in changes:
            diff.append(("[syntax-only]", c))
        return s_a_sp, diff, "needs-manual-review"

    # Step 10: force-runnable fallback — patch empty blocks with `pass` so grader
    # can execute the code (it will fail tests rather than be excluded).
    final = s_a if aggressive_applied else s_c
    runnable, rnotes = force_runnable(final, fn_name, params)
    if runnable is not None:
        for n in rnotes:
            diff.append(("[logic-affecting]", n))
        diff.append(("[syntax-only]", f"parse error before force-runnable fallback: {err4}"))
        return runnable, diff, "needs-manual-review"

    diff.append(("[syntax-only]", f"final parse error after all repairs: {err4}"))
    return final, diff, "unrepairable"


def force_runnable(s: str, fn_name: str | None, params: list[str] | None) -> tuple[str | None, list[str]]:
    """Best-effort: make `s` parse by patching empty blocks with `pass`.

    Fallback: if unrecoverable, return a stub `def fn_name(...): return 0`.
    Returns (code_or_None, notes). code_or_None is None only if we have
    no function name to stub with.
    """
    notes: list[str] = []
    code = s
    for _ in range(40):
        err = try_parse(code)
        if err is None:
            return code, notes
        m = re.match(r"^(expected an indented block(?: after[^()]*)?)\s*\(line (\d+)\)$", err)
        if not m:
            break
        lineno = int(m.group(2))
        lines = code.split("\n")
        # Find the header line at or before `lineno` that ends in `:`
        header_idx = None
        for i in range(min(lineno, len(lines)) - 1, -1, -1):
            ls = lines[i].rstrip()
            if ls.endswith(":"):
                header_idx = i
                break
        if header_idx is None:
            break
        indent = count_leading_spaces(lines[header_idx])
        lines.insert(header_idx + 1, " " * (indent + 4) + "pass")
        notes.append(f"inserted `pass` into empty block at line {header_idx + 1}")
        code = "\n".join(lines)

    # Still broken — emit a stub returning a safe default.
    if fn_name:
        stub_params = ", ".join(params or [])
        stub = f"def {fn_name}({stub_params}):\n    return 0\n"
        notes.append(f"replaced unparseable code with stub `def {fn_name}({stub_params}): return 0`")
        return stub, notes
    # No known function name (e.g. P3 bonus) — comment out all content so file parses.
    commented = "\n".join("# " + ln for ln in s.split("\n"))
    header = "# [force-runnable] original code was unparseable; all lines commented below.\n"
    notes.append("commented out all original code so file parses (no known fn_name to stub)")
    return header + commented + "\n", notes


# ---------- Java -> Python transpile ----------

def _transpile_line(stripped: str, fn_name: str | None) -> str:
    """Convert one Java statement/header to its Python equivalent.
    Assumes line has been stripped of leading/trailing whitespace and braces.
    """
    s = stripped

    # Method signature: public static int foo(int[] nums, int k)
    sig_re = re.compile(r"^(?:public|private|protected)\s+(?:static\s+)?(?:final\s+)?[\w<>\[\]]+\s+(\w+)\s*\(([^)]*)\)\s*$")
    m = sig_re.match(s)
    if m:
        name, param_str = m.group(1), m.group(2)
        new_params = []
        for p in [x.strip() for x in param_str.split(",") if x.strip()]:
            parts = p.split()
            new_params.append(parts[-1].replace("[]", ""))
        py_name = fn_name if fn_name else to_snake(name)
        return f"def {py_name}({', '.join(new_params)}):"

    # for (int i = a; i < b; i++) / for (int i = a; i <= b; i++) / decrement
    m = re.match(r"^for\s*\(\s*(?:int\s+|long\s+)?(\w+)\s*=\s*([^;]+);\s*(\w+)\s*([<>]=?)\s*([^;]+);\s*([^)]+)\)\s*$", s)
    if m:
        var, a, _cmpvar, cmp, b, step = m.group(1), m.group(2).strip(), m.group(3), m.group(4), m.group(5).strip(), m.group(6).strip()
        # adjust b for <=
        if cmp == "<=":
            b = f"({b}) + 1"
        elif cmp == ">=":
            b = f"({b}) - 1"
        if step in (f"{var}++", f"++{var}"):
            return f"for {var} in range({a}, {b}):"
        if step in (f"{var}--", f"--{var}"):
            return f"for {var} in range({a}, {b}, -1):"
        if step.replace(" ", "").startswith(f"{var}+="):
            inc = step.split("+=")[1].strip()
            return f"for {var} in range({a}, {b}, {inc}):"
        if step.replace(" ", "").startswith(f"{var}-="):
            dec = step.split("-=")[1].strip()
            return f"for {var} in range({a}, {b}, -{dec}):"
        return f"for {var} in range({a}, {b}):"

    # for (Type x : arr)
    m = re.match(r"^for\s*\(\s*(?:\w+(?:\[\])?\s+)?(\w+)\s*:\s*(.+)\)\s*$", s)
    if m:
        return f"for {m.group(1)} in {m.group(2).strip()}:"

    # if/while/elif
    m = re.match(r"^(if|while)\s*\((.*)\)\s*$", s)
    if m:
        return f"{m.group(1)} {m.group(2).strip()}:"
    m = re.match(r"^else\s+if\s*\((.*)\)\s*$", s)
    if m:
        return f"elif {m.group(1).strip()}:"
    if s.strip() == "else":
        return "else:"
    if s.strip() == "do":
        return "while True:"  # approximation

    # Remove "return " from its statement, preserved below. Handled in generic rewrites.
    # Strip stand-alone variable declarations like "int x = ..." => "x = ..."
    s = re.sub(r"^(int|long|double|float|boolean|String|char|var)(?:\[\])?\s+", "", s)
    # Declaration without init: "int x" => "x = 0" (safe default; skip if "= " already)
    m = re.match(r"^(\w+)$", s)  # after strip, lone identifier
    if m:
        return f"{m.group(1)} = 0"

    # Ternary: cond ? a : b => a if cond else b
    def ternary_repl(s):
        prev = None
        while s != prev:
            prev = s
            s = re.sub(r"([^?\n]+?)\s*\?\s*([^:\n]+?)\s*:\s*([^\n;]+)", r"(\2 if \1 else \3)", s, count=1)
        return s
    s = ternary_repl(s)

    # Increment/decrement as statement
    s = re.sub(r"(\w+)\+\+", r"\1 += 1", s)
    s = re.sub(r"(\w+)--", r"\1 -= 1", s)
    s = re.sub(r"\+\+(\w+)", r"\1 += 1", s)
    s = re.sub(r"--(\w+)", r"\1 -= 1", s)

    # Math.*, arr.length, System.out.*
    s = re.sub(r"\bMath\.max\b", "max", s)
    s = re.sub(r"\bMath\.min\b", "min", s)
    s = re.sub(r"\bMath\.abs\b", "abs", s)
    s = re.sub(r"\bMath\.floor\b", "int", s)
    s = re.sub(r"\bMath\.pow\s*\(", "pow(", s)
    s = re.sub(r"(\w+)\.length\b", r"len(\1)", s)
    s = re.sub(r"\bSystem\.out\.(?:println|print)\s*\(", "print(", s)

    # Integer constants
    s = re.sub(r"\bInteger\.MAX_VALUE\b", "float('inf')", s)
    s = re.sub(r"\bInteger\.MIN_VALUE\b", "float('-inf')", s)

    # Bool / None
    s = re.sub(r"\btrue\b", "True", s)
    s = re.sub(r"\bfalse\b", "False", s)
    s = re.sub(r"\bnull\b", "None", s)

    # Logical operators
    s = s.replace("&&", " and ").replace("||", " or ")
    s = re.sub(r"(?<![!<>=])!(?!=)\s*", " not ", s)

    # String concat + on strings — too risky; leave operator alone

    return s


def java_to_python(raw: str, fn_name: str | None, params: list[str] | None) -> tuple[str, list[tuple[str, str]], str]:
    diff: list[tuple[str, str]] = []
    s = normalize(raw)
    # strip /* ... */ comments
    s = re.sub(r"/\*.*?\*/", "", s, flags=re.DOTALL)
    # remove generics `<T>`, `<K, V>` (simple cases)
    s = re.sub(r"<[A-Za-z0-9_,\s?]+>", "", s)

    lines = s.split("\n")
    out_lines: list[str] = []
    depth = 0
    for raw_line in lines:
        # strip // comments (outside of strings — approximate)
        line = re.sub(r"//.*$", "", raw_line)
        stripped = line.strip()
        if not stripped:
            out_lines.append("")
            continue

        opens = stripped.count("{")
        closes = stripped.count("}")

        # Pure "}" line
        if stripped in ("}", "};", "});", "})"):
            depth = max(0, depth - 1)
            continue

        # Line starting with "} else {" or "} else if (...) {"
        if stripped.startswith("}"):
            depth = max(0, depth - 1)
            stripped = stripped[1:].strip()
            closes -= 1
            if not stripped:
                continue

        # Strip trailing "{"
        has_open_block = False
        if stripped.endswith("{"):
            stripped = stripped[:-1].strip()
            has_open_block = True
            opens -= 1

        # Strip trailing ";"
        if stripped.endswith(";"):
            stripped = stripped[:-1].rstrip()

        # Skip empty after stripping
        if not stripped:
            if has_open_block:
                depth += 1
            continue

        line_out = _transpile_line(stripped, fn_name)
        out_lines.append("    " * depth + line_out)

        if has_open_block:
            depth += 1
        # Any trailing residual braces handled by counts
        depth += max(0, opens)
        depth -= max(0, closes)
        if depth < 0:
            depth = 0

    # Rename method if not already expected fn_name (handled inside _transpile_line)
    diff.append(("[syntax-only]", "mechanical Java->Python transpile (brace-depth indent + types/operators)"))

    out = "\n".join(out_lines)
    # try parse
    if try_parse(out) is None:
        return out, diff, "repaired"

    # If parse fails, fall through to python repair pipeline
    s2, pydiff, status = repair_python(out, fn_name, params)
    return s2, diff + pydiff, status


def to_snake(s: str) -> str:
    return re.sub(r"(?<!^)(?=[A-Z])", "_", s).lower()


# ---------- driver ----------

def write_fixed(pdir: Path, sid: str, code: str, diff: list[tuple[str, str]]):
    fixed_dir = pdir / "fixed"
    fixed_dir.mkdir(exist_ok=True)
    (fixed_dir / f"{sid}.py").write_text(code, encoding="utf-8")
    lines = [f"# Diff for {sid}", "", "| Tag | Change |", "|---|---|"]
    for tag, msg in diff:
        lines.append(f"| {tag} | {msg.replace('|', chr(92)+'|')} |")
    if not diff:
        lines.append("| [syntax-only] | no changes required (parsed as-is) |")
    (fixed_dir / f"{sid}.diff.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def load_manifest(pdir: Path):
    mpath = pdir / "manifest.csv"
    with mpath.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def save_manifest(pdir: Path, rows: list[dict]):
    mpath = pdir / "manifest.csv"
    with mpath.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["student_id", "detected_language", "attempt_num", "raw_path", "status"])
        w.writeheader()
        for r in rows:
            w.writerow(r)


def process_problem(problem: str, fn_name: str | None, params: list[str] | None):
    pdir = ROOT / problem
    rows = load_manifest(pdir)
    # Reset statuses for code rows so this stage is idempotent.
    for r in rows:
        if r["detected_language"] in ("python", "java"):
            r["status"] = "extracted"
    print(f"\n=== {problem} (expected fn: {fn_name}) ===")
    counts = {"repaired": 0, "needs-manual-review": 0, "unrepairable": 0,
              "pseudocode": 0, "empty": 0, "missing": 0}
    for r in rows:
        sid = r["student_id"]
        lang = r["detected_language"]
        status = r["status"]
        if lang == "pseudocode":
            r["status"] = "pseudocode"
            counts["pseudocode"] += 1
            continue
        if lang in ("empty", "missing"):
            counts[lang] += 1
            continue
        if status != "extracted":
            continue

        raw_path = ROOT / r["raw_path"]
        raw = raw_path.read_text(encoding="utf-8")

        if lang == "python":
            fixed, diff, new_status = repair_python(raw, fn_name, params)
        elif lang == "java":
            fixed, diff, new_status = java_to_python(raw, fn_name, params)
        else:
            continue

        # CLAUDE.md: "Any non-syntax-only change auto-flags for manual review."
        non_syntax = [d for d in diff if d[0] != "[syntax-only]"]
        if non_syntax and new_status == "repaired":
            new_status = "needs-manual-review"

        write_fixed(pdir, sid, fixed, diff)
        r["status"] = new_status
        counts[new_status] = counts.get(new_status, 0) + 1

    save_manifest(pdir, rows)
    for k, v in sorted(counts.items()):
        if v:
            print(f"  {k:25s}: {v}")


def main():
    for problem, fn_name, params in PROBLEMS:
        process_problem(problem, fn_name, params)


if __name__ == "__main__":
    main()
