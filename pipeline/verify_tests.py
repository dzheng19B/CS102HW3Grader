import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def ref_p1(nums, k):
    n = len(nums)
    best = 0
    found = False
    neg = sum(1 for x in nums[:k] if x < 0)
    s = sum(nums[:k])
    if neg <= 1:
        best = s
        found = True
    for i in range(k, n):
        if nums[i] < 0: neg += 1
        if nums[i-k] < 0: neg -= 1
        s += nums[i] - nums[i-k]
        if neg <= 1:
            if not found or s > best:
                best = s
                found = True
    return best if found else 0

def ref_p2(nums, T):
    c = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] <= T: c += 1
    return c

for path, fn in [(ROOT / "problem1" / "test_cases.json", ref_p1), (ROOT / "problem2" / "test_cases.json", ref_p2)]:
    data = json.load(open(path))
    print(f"=== {path} ===")
    for c in data["cases"]:
        got = fn(*c["args"])
        mark = "OK" if got == c["expected"] else f"MISMATCH got={got}"
        print(f"  {c['name']}: expected={c['expected']} {mark}")
