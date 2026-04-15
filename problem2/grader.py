"""Stage 3 grader for problem 2 (count_pairs). See problem1/grader.py for notes."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "problem1"))
import grader as p1_grader

p1_grader.PDIR = Path(__file__).parent
p1_grader.FIXED = p1_grader.PDIR / "fixed"
p1_grader.RESULTS = p1_grader.PDIR / "results"
p1_grader.TEST_CASES_PATH = p1_grader.PDIR / "test_cases.json"

if __name__ == "__main__":
    p1_grader.main("count_pairs")
