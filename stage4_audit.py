"""
Stage 4 — Logic-change audit.
For each student with status 'repaired', compare raw vs fixed and classify
whether any change actually altered control flow, conditions, return values,
or data structures. Writes audit/<student_id>.md and updates manifest status
to 'needs-manual-review' if a logic change is found.
"""

import ast
import csv
import difflib
import os
import re
import sys

PROBLEMS = ["problem1", "problem2", "problem3_bonus"]

# AST node types that represent logic / control flow
LOGIC_NODES = (
    ast.If, ast.For, ast.While, ast.Return, ast.Break, ast.Continue,
    ast.Try, ast.Raise, ast.Assert, ast.BoolOp, ast.Compare,
    ast.ListComp, ast.DictComp, ast.SetComp, ast.GeneratorExp,
    ast.Lambda, ast.IfExp,
)


def ast_fingerprint(code):
    """
    Return a tuple of (node_type, relevant_fields) for every AST node.
    Used to detect structural / logical changes.
    """
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return None

    fingerprints = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant):
            fingerprints.append(("Constant", node.value))
        elif isinstance(node, ast.Name):
            fingerprints.append(("Name", node.id))
        elif isinstance(node, ast.BinOp):
            fingerprints.append(("BinOp", type(node.op).__name__))
        elif isinstance(node, ast.Compare):
            fingerprints.append(("Compare", [type(o).__name__ for o in node.ops]))
        elif isinstance(node, ast.BoolOp):
            fingerprints.append(("BoolOp", type(node.op).__name__))
        elif isinstance(node, ast.Return):
            fingerprints.append(("Return",))
        elif isinstance(node, ast.If):
            fingerprints.append(("If",))
        elif isinstance(node, ast.For):
            fingerprints.append(("For",))
        elif isinstance(node, ast.While):
            fingerprints.append(("While",))
        elif isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                fingerprints.append(("Call", node.func.id))
            elif isinstance(node.func, ast.Attribute):
                fingerprints.append(("Call", node.func.attr))
    return tuple(fingerprints)


def diff_lines(raw, fixed):
    """Return unified diff lines between raw and fixed."""
    return list(difflib.unified_diff(
        raw.splitlines(keepends=True),
        fixed.splitlines(keepends=True),
        fromfile="raw", tofile="fixed",
    ))


def classify_changes(raw, fixed):
    """
    Classify what changed between raw and fixed.
    Primary signal: AST fingerprint comparison (when raw parses).
    Secondary signal: token-level diff (ignoring whitespace).
    Returns (has_logic_change, findings).
    """
    findings = []
    has_logic = False

    # 1. AST fingerprint comparison — most reliable signal
    raw_fp  = ast_fingerprint(raw)
    fix_fp  = ast_fingerprint(fixed)

    if raw_fp is not None and fix_fp is not None:
        if raw_fp == fix_fp:
            findings.append("  [ok] AST fingerprint unchanged — no logic nodes added/removed/reordered.")
            return False, findings  # definitive: no logic change
        else:
            findings.append("  [warning] AST fingerprint differs — logic structure may have changed.")
            has_logic = True
            # Fall through to line-level for detail

    elif raw_fp is None and fix_fp is not None:
        # Raw didn't parse. Use token comparison: if stripped tokens match, it's whitespace-only.
        raw_tokens  = re.sub(r"\s+", " ", raw.strip())
        fix_tokens  = re.sub(r"\s+", " ", fixed.strip())
        # Normalise common syntax fixes that are definitely not logic changes
        raw_norm = re.sub(r"//", "#", raw_tokens)   # // -> # (cpp comment fix)
        raw_norm = re.sub(r"\bretrun\b|\bretrn\b|\breturm\b", "return", raw_norm)
        # Strip colons added to keyword lines (missing colon fix)
        raw_norm = re.sub(r"(\b(?:if|for|while|elif|else|def|class)\b[^:\n]*?)\s*(?=\n|$)", r"\1:", raw_norm)

        if re.sub(r"\s+", " ", raw_norm).strip() == re.sub(r"\s+", " ", fix_tokens).strip():
            findings.append("  [ok] Token content unchanged (only whitespace/colon/comment fixes applied).")
            return False, findings

        # Compare stripped lines: if every changed line differs only in content we expect from our repairs
        diff = diff_lines(raw, fixed)
        added_stripped   = [re.sub(r"\s+", "", l[1:]) for l in diff if l.startswith("+") and not l.startswith("+++")]
        removed_stripped = [re.sub(r"\s+", "", l[1:]) for l in diff if l.startswith("-") and not l.startswith("---")]

        # Build set of non-whitespace-only changes
        added_set   = set(added_stripped) - {""}
        removed_set = set(removed_stripped) - {""}

        # Changes that are ONLY whitespace/colon/comment differences
        whitespace_only = all(
            re.sub(r"[\s:]", "", a) == re.sub(r"[\s:]", "", r) or
            re.sub(r"[\s:#]", "", a) == re.sub(r"[\s:#]", "", r)
            for a, r in zip(added_stripped, removed_stripped)
        ) if (added_stripped and removed_stripped and len(added_stripped) == len(removed_stripped)) else False

        if whitespace_only:
            findings.append("  [ok] All line changes are whitespace/colon/comment-only (indentation repair).")
            return False, findings

        # Look for genuinely new or removed content
        LOGIC_KEYWORDS = re.compile(
            r"\b(if|elif|else|for|while|return|break|continue|raise|and|or|not)\b"
        )
        truly_new     = added_set - removed_set
        truly_removed = removed_set - added_set
        for token in truly_new:
            if LOGIC_KEYWORDS.search(token):
                findings.append(f"  [logic-added]   new token content: {token[:80]}")
                has_logic = True
        for token in truly_removed:
            if LOGIC_KEYWORDS.search(token):
                findings.append(f"  [logic-removed] removed token content: {token[:80]}")
                has_logic = True

        if not has_logic:
            findings.append("  [ok] Changed lines differ only in syntax tokens (no logic keywords added/removed).")

    elif raw_fp is None and fix_fp is None:
        findings.append("  [warning] Neither raw nor fixed parse — cannot assess logic changes.")
        has_logic = True

    # 2. Supplementary line-level detail when logic change detected
    if has_logic:
        diff = diff_lines(raw, fixed)
        for l in diff[:40]:
            findings.append("  " + l.rstrip())

    return has_logic, findings


def write_audit(audit_path, student_id, raw, fixed, changes_from_diff, has_logic, findings, verdict):
    lines = [f"# Audit — {student_id}\n"]
    lines.append(f"**Verdict:** {verdict}\n")
    lines.append("## Repair changes applied\n")
    for ch in changes_from_diff:
        lines.append(f"- {ch.get('tag','')} {ch.get('desc','')}")
    lines.append("\n## Logic-change analysis\n")
    for f in findings:
        lines.append(f)
    lines.append("\n## Diff\n```diff")
    lines.extend([l.rstrip() for l in diff_lines(raw, fixed)])
    lines.append("```")
    with open(audit_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def load_diff_changes(diff_md_path):
    """Parse the changes list from a diff.md file."""
    if not os.path.exists(diff_md_path):
        return []
    text = open(diff_md_path, encoding="utf-8").read()
    changes = []
    for line in text.splitlines():
        m = re.match(r"- \*\*(\[.*?\])\*\* (.*)", line)
        if m:
            changes.append({"tag": m.group(1), "desc": m.group(2)})
    return changes


def process_problem(prob_dir):
    manifest_path = os.path.join(prob_dir, "manifest.csv")
    fixed_dir     = os.path.join(prob_dir, "fixed")
    raw_dir       = os.path.join(prob_dir, "raw")
    audit_dir     = os.path.join(prob_dir, "audit")
    os.makedirs(audit_dir, exist_ok=True)

    with open(manifest_path, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    flagged = []
    confirmed_ok = []

    for row in rows:
        sid    = row["student_id"]
        status = row["status"]

        if status != "repaired":
            continue  # only audit repaired files

        raw_path  = os.path.join(raw_dir,  f"{sid}.txt")
        fixed_path= os.path.join(fixed_dir, f"{sid}.py")
        diff_path = os.path.join(fixed_dir, f"{sid}.diff.md")
        audit_path= os.path.join(audit_dir, f"{sid}.md")

        if not os.path.exists(raw_path) or not os.path.exists(fixed_path):
            continue

        raw   = open(raw_path,   encoding="utf-8").read()
        fixed = open(fixed_path, encoding="utf-8").read()
        changes_from_diff = load_diff_changes(diff_path)

        # Quick check: if raw == fixed (no changes), trivially OK
        if raw.strip() == fixed.strip():
            write_audit(audit_path, sid, raw, fixed, [],
                        False,
                        ["  [ok] Raw and fixed are identical — no changes were made."],
                        "NO LOGIC CHANGES — code unchanged")
            confirmed_ok.append(sid)
            continue

        has_logic, findings = classify_changes(raw, fixed)

        if has_logic:
            verdict = "FLAGGED — potential logic change detected; requires manual review"
            row["status"] = "needs-manual-review"
            flagged.append(sid)
        else:
            verdict = "OK — changes are syntax/whitespace only; no logic impact detected"
            confirmed_ok.append(sid)

        write_audit(audit_path, sid, raw, fixed, changes_from_diff, has_logic, findings, verdict)
        print(f"  {sid}: {'FLAGGED' if has_logic else 'ok'}")

    # Rewrite manifest
    fieldnames = list(rows[0].keys()) if rows else []
    with open(manifest_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)

    return flagged, confirmed_ok


if __name__ == "__main__":
    targets = sys.argv[1:] if len(sys.argv) > 1 else PROBLEMS

    all_flagged = {}
    for prob_dir in targets:
        print(f"\n=== Stage 4 audit: {prob_dir} ===")
        flagged, ok = process_problem(prob_dir)
        all_flagged[prob_dir] = flagged
        print(f"  Audited repaired files: {len(ok)+len(flagged)}  |  Newly flagged: {len(flagged)}  |  Confirmed OK: {len(ok)}")
        if flagged:
            print(f"  Flagged IDs: {flagged}")

    print("\n=== Audit complete ===")
    for prob, ids in all_flagged.items():
        if ids:
            print(f"  {prob}: {len(ids)} newly downgraded to needs-manual-review: {ids}")
