# Mock Technical Interview - Full Report

> Generated 2026-05-19 13:41  
> 80 students | 75 graded | 27 all-pass | 7 minor errors | 41 critical errors | 0 compile errors | 1 non-optimal solutions

## How to read this report

- **Summary table**: one row per student with problem, language, score, severity, and optimality.
- **Per-student sections**: test results (if graded), syntax changes, extracted code, and original document.
- **Score**: `passed/total` test cases. A dash means the code could not be graded.
- **Severity**: `PASS` = all tests pass; `Minor Error` = right approach, some bugs (>50% pass); `Critical Error` = wrong approach or major bugs (<=50% pass or uncompilable).
- **Optimal**: whether the student used the expected optimal algorithm. Expected approaches: Guess Number Higher or Lower: Binary search O(log n); Longest Substring Without Repeating Characters: Sliding window O(n); Contains Nearby Duplicate: Hash map O(n); Merge Two Sorted Lists: Iterative merge O(n+m); Evaluate Reverse Polish Notation: Stack O(n).

## Distribution

| Problem | Students |
|---------|--------:|
| Guess Number Higher or Lower | 15 |
| Longest Substring Without Repeating Characters | 17 |
| Contains Nearby Duplicate | 12 |
| Merge Two Sorted Lists | 14 |
| Evaluate Reverse Polish Notation | 17 |
| **Total** | **80** |

| Language | Count |
|----------|------:|
| empty | 2 |
| java | 9 |
| pseudocode | 5 |
| python | 64 |

## Summary

| # | Student | Question | Score | Severity | Optimal | Failed Tests |
|--:|---------|----------|------:|----------|---------|--------------|
| 1 | Coverdale, Solomon | Contains Nearby Duplicate | 8/8 | PASS | Yes |  |
| 2 | Genc, Sude | Contains Nearby Duplicate | 8/8 | PASS | Yes |  |
| 3 | Safronov, Danila | Contains Nearby Duplicate | 8/8 | PASS | Yes |  |
| 4 | Weisberg, Evan | Contains Nearby Duplicate | 8/8 | PASS | Yes |  |
| 5 | Wong, Ethan | Contains Nearby Duplicate | 8/8 | PASS | Yes |  |
| 6 | Broderick, Maddie | Contains Nearby Duplicate | 0/8 | Critical Error | Yes | true_basic; true_adjacent; false_too_far; false_k_zero; single_element; no_dups; true_exact_k; empty |
| 7 | Chan, Cheong Ting Eland | Contains Nearby Duplicate | 6/8 | Minor Error | Yes | true_basic; true_exact_k |
| 8 | Guo, Jason | Contains Nearby Duplicate | 1/8 | Critical Error | Yes | true_basic; true_adjacent; false_too_far; false_k_zero; single_element; no_dups; true_exact_k |
| 9 | Lin, Brian | Contains Nearby Duplicate | 5/8 | Minor Error | Yes | true_basic; true_adjacent; true_exact_k |
| 10 | Lin, Tiffany | Contains Nearby Duplicate | 4/8 | Critical Error | Yes | true_basic; true_adjacent; true_exact_k; empty |
| 11 | McBean, Andrew | Contains Nearby Duplicate | 1/8 | Critical Error | Yes | true_basic; true_adjacent; false_too_far; false_k_zero; single_element; no_dups; true_exact_k |
| 12 | Stevens, Jack | Contains Nearby Duplicate | 6/8 | Minor Error | Yes | false_too_far; false_k_zero |
| 13 | Carozza, Ashley | Evaluate Reverse Polish Notation | 7/7 | PASS | Yes |  |
| 14 | Cheung, Ivan | Evaluate Reverse Polish Notation | 7/7 | PASS | Yes |  |
| 15 | Ng, Gavin | Evaluate Reverse Polish Notation | 7/7 | PASS | Yes |  |
| 16 | Sellam, Naomi | Evaluate Reverse Polish Notation | 7/7 | PASS | Yes |  |
| 17 | Singh, Kushagra | Evaluate Reverse Polish Notation | 7/7 | PASS | Yes |  |
| 18 | Attina, Ava | Evaluate Reverse Polish Notation | 0/7 | Critical Error | Yes | example1; example2; example3; add_only; single; subtract; neg_divide |
| 19 | Carhart, Sean | Evaluate Reverse Polish Notation | 0/7 | Critical Error | Yes | example1; example2; example3; add_only; single; subtract; neg_divide |
| 20 | Godzki, Kyle | Evaluate Reverse Polish Notation | 3/7 | Critical Error | Yes | example2; example3; subtract; neg_divide |
| 21 | Mahaman Sani, Abdoul Razakou | Evaluate Reverse Polish Notation | 5/7 | Minor Error | Yes | example3; single |
| 22 | Majlis, Mahir | Evaluate Reverse Polish Notation | 0/7 | Critical Error | Yes | example1; example2; example3; add_only; single; subtract; neg_divide |
| 23 | Moran, Juan | Evaluate Reverse Polish Notation | 0/7 | Critical Error | Yes | example1; example2; example3; add_only; single; subtract; neg_divide |
| 24 | Patel, Ved | Evaluate Reverse Polish Notation | 0/7 | Critical Error | Yes | example1; example2; example3; add_only; single; subtract; neg_divide |
| 25 | Regueiferos, Logan | Evaluate Reverse Polish Notation | 6/7 | Minor Error | Yes | example3 |
| 26 | Seng, Jason | Evaluate Reverse Polish Notation | 1/7 | Critical Error | Yes | example1; example2; example3; add_only; subtract; neg_divide |
| 27 | Stehura, Max | Evaluate Reverse Polish Notation | 0/7 | Critical Error | Yes | example1; example2; example3; add_only; single; subtract; neg_divide |
| 28 | Vallarta, Giankyle | Evaluate Reverse Polish Notation | 0/7 | Critical Error | Yes | example1; example2; example3; add_only; single; subtract; neg_divide |
| 29 | Wahlin, Kartik | Evaluate Reverse Polish Notation | 3/7 | Critical Error | Yes | example2; example3; subtract; neg_divide |
| 30 | Chen, Albert | Guess Number Higher or Lower | 7/7 | PASS | Yes |  |
| 31 | Diusheyeva, Lilia | Guess Number Higher or Lower | 7/7 | PASS | Yes |  |
| 32 | Kukreti, Naman | Guess Number Higher or Lower | 7/7 | PASS | Yes |  |
| 33 | Park, Matthew | Guess Number Higher or Lower | 7/7 | PASS | Yes |  |
| 34 | Rpk, Parks | Guess Number Higher or Lower | 7/7 | PASS | Yes |  |
| 35 | Wang, Hewitt | Guess Number Higher or Lower | 7/7 | PASS | Yes |  |
| 36 | Zhou, Qianjun | Guess Number Higher or Lower | 7/7 | PASS | Yes |  |
| 37 | Zuluaga, Santiago | Guess Number Higher or Lower | 7/7 | PASS | Yes |  |
| 38 | Chan, Gaven | Guess Number Higher or Lower | 0/7 | Critical Error | Yes | basic; single; pick_low; pick_high; large; mid_range; pick_is_n |
| 39 | Connors, William | Guess Number Higher or Lower | 0/7 | Critical Error | Yes | basic; single; pick_low; pick_high; large; mid_range; pick_is_n |
| 40 | Juance, Reginald | Guess Number Higher or Lower | 0/7 | Critical Error | Yes | basic; single; pick_low; pick_high; large; mid_range; pick_is_n |
| 41 | Ramos Rodriguez, Jordanny | Guess Number Higher or Lower | 0/7 | Critical Error | Yes | basic; single; pick_low; pick_high; large; mid_range; pick_is_n |
| 42 | Yang, Kevin | Guess Number Higher or Lower | 0/7 | Critical Error | Yes | basic; single; pick_low; pick_high; large; mid_range; pick_is_n |
| 43 | Yuan, Lilian | Guess Number Higher or Lower | 0/7 | Critical Error | Yes | basic; single; pick_low; pick_high; large; mid_range; pick_is_n |
| 44 | Zaidi, Rijaa | Guess Number Higher or Lower | 0/7 | Critical Error | Yes | basic; single; pick_low; pick_high; large; mid_range; pick_is_n |
| 45 | Calandra, Clare | Longest Substring Without Repeating Characters | 8/8 | PASS | Yes |  |
| 46 | Conroy, William | Longest Substring Without Repeating Characters | 8/8 | PASS | Yes |  |
| 47 | Friedlander, Nicholas | Longest Substring Without Repeating Characters | 8/8 | PASS | Yes |  |
| 48 | Halsband, Samuel | Longest Substring Without Repeating Characters | 8/8 | PASS | Yes |  |
| 49 | Steck, Jake | Longest Substring Without Repeating Characters | 8/8 | PASS | Yes |  |
| 50 | Yang, Isabella | Longest Substring Without Repeating Characters | 8/8 | PASS | Yes |  |
| 51 | Balkam, Tianna | Longest Substring Without Repeating Characters | 1/8 | Critical Error | Yes | example1; all_same; example3; single_char; all_unique; spaces; end_longest |
| 52 | Carey, Carson | Longest Substring Without Repeating Characters | 1/8 | Critical Error | Yes | example1; all_same; example3; single_char; all_unique; spaces; end_longest |
| 53 | Chen, Shunyi | Longest Substring Without Repeating Characters | 6/8 | Minor Error | Yes | example3; spaces |
| 54 | DiNapoli, Michael | Longest Substring Without Repeating Characters | 1/8 | Critical Error | Yes | example1; all_same; example3; single_char; all_unique; spaces; end_longest |
| 55 | Gaston, Justin | Longest Substring Without Repeating Characters | 1/8 | Critical Error | Yes | example1; all_same; example3; single_char; all_unique; spaces; end_longest |
| 56 | Noh, Jin | Longest Substring Without Repeating Characters | 1/8 | Critical Error | Yes | example1; all_same; example3; single_char; all_unique; spaces; end_longest |
| 57 | Thelusma, Treyson | Longest Substring Without Repeating Characters | 1/8 | Critical Error | Yes | example1; all_same; example3; single_char; all_unique; spaces; end_longest |
| 58 | Vega, Dominic | Longest Substring Without Repeating Characters | 1/8 | Critical Error | Yes | example1; all_same; example3; single_char; all_unique; spaces; end_longest |
| 59 | Zhang, Jiarong | Longest Substring Without Repeating Characters | 1/8 | Critical Error | Yes | example1; all_same; example3; single_char; all_unique; spaces; end_longest |
| 60 | Zhang, Ryan | Longest Substring Without Repeating Characters | 7/8 | Minor Error | No - Nested loops instead of sliding window | example1 |
| 61 | Zuniga, Christian | Longest Substring Without Repeating Characters | 1/8 | Critical Error | Yes | example1; all_same; example3; single_char; all_unique; spaces; end_longest |
| 62 | Calin, Stephania | Merge Two Sorted Lists | 7/7 | PASS | Yes |  |
| 63 | Lu, Zhi Xiong | Merge Two Sorted Lists | 7/7 | PASS | Yes |  |
| 64 | Tsui, Ryan | Merge Two Sorted Lists | 7/7 | PASS | Yes |  |
| 65 | Batz, Alison | Merge Two Sorted Lists | 0/7 | Critical Error | Yes | example1; both_empty; one_empty; other_empty; interleave; all_same; single_each |
| 66 | Gnajewski, Monica | Merge Two Sorted Lists | 0/7 | Critical Error | Yes | example1; both_empty; one_empty; other_empty; interleave; all_same; single_each |
| 67 | Karamchandani, Varun | Merge Two Sorted Lists | 0/7 | Critical Error | Yes | example1; both_empty; one_empty; other_empty; interleave; all_same; single_each |
| 68 | Minhas, Vikram | Merge Two Sorted Lists | 1/7 | Critical Error | Yes | example1; both_empty; other_empty; interleave; all_same; single_each |
| 69 | Ng, Kenneth | Merge Two Sorted Lists | 0/7 | Critical Error | Yes | example1; both_empty; one_empty; other_empty; interleave; all_same; single_each |
| 70 | Porto, Ian | Merge Two Sorted Lists | 1/7 | Critical Error | Yes | example1; both_empty; one_empty; interleave; all_same; single_each |
| 71 | Santhosh, Athulya | Merge Two Sorted Lists | 3/7 | Critical Error | Yes | example1; interleave; all_same; single_each |
| 72 | Schauber, Kathryn | Merge Two Sorted Lists | 3/7 | Critical Error | Yes | example1; interleave; all_same; single_each |
| 73 | Yang, Gabriel | Merge Two Sorted Lists | 1/7 | Critical Error | Yes | example1; one_empty; other_empty; interleave; all_same; single_each |
| 74 | Yu, Justin | Merge Two Sorted Lists | 0/7 | Critical Error | Yes | example1; both_empty; one_empty; other_empty; interleave; all_same; single_each |
| 75 | Zheng, Vincent | Merge Two Sorted Lists | 0/7 | Critical Error | Yes | example1; both_empty; one_empty; other_empty; interleave; all_same; single_each |
| 76 | Lee, Kristen | unknown | - | extracted | Yes |  |
| 77 | Maldonado, Noel | unknown | - | manual-review | Yes |  |
| 78 | Martin, Ryan | unknown | - | empty | Yes |  |
| 79 | Wu, Xinlin | unknown | - | manual-review | Yes |  |
| 80 | Zou, Elaine | unknown | - | extracted | Yes |  |

---

## Student Details

### Contains Nearby Duplicate

#### Maddie Broderick (`77137`)

- **Problem:** Contains Nearby Duplicate
- **Language:** python
- **Score:** 0/8 (Critical Error)
- **Grading status:** graded
- **Files:** Copy of Copy of CS 102 Paired Technical Interview Printouts - General Info.pdf (pdf); MockTechnicalMaddieBroderick.py (direct)

| Test Case | Result |
|-----------|--------|
| true_basic | FAIL |
| true_adjacent | FAIL |
| false_too_far | FAIL |
| false_k_zero | FAIL |
| single_element | FAIL |
| no_dups | FAIL |
| true_exact_k | FAIL |
| empty | FAIL |

<details>
<summary>Edits made by grader</summary>

- [syntax-only] Lowered keyword 'If'

</details>

<details>
<summary>Extracted Code (77137.py)</summary>

```python
def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    mapp = {}
    j = 0
    for j in len(nums):
        if nums[j] in mapp:
            if j - mapp[nums[j]] <= k:
                return True
        mapp[nums[j]] = j
    return False
        
# Time complexity: O(n) because it runs through the array once
# Solves the problem by running through the list and adding values
# to the hashmap. If the value already exist, it checks if abs(i-j) <= k
```

</details>

<details>
<summary>Original Document (77137.txt)</summary>

```
Paired
 
Technical
 
Interview
 
Overview
 
Mock
 
interviews
 
are
 
one
 
of
 
the
 
most
 
effective
 
ways
 
to
 
prepare
 
for
 
technical
 
interviews.
 
They
 
help
 
you
 
practice
 
solving
 
problems
 
under
 
realistic
 
time
 
pressure
 
while
 
also
 
developing
 
the
 
technical
 
communication
 
skills
 
required
 
in
 
a
 
real
 
interview
 
setting.
 
In
 
addition,
 
you’ll
 
gain
 
experience
 
evaluating
 
a
 
candidate’ s
 
performance
 
from
 
the
 
interviewer ’s
 
perspective,
 
which
 
will
 
help
 
you
 
understand
 
how
 
hiring
 
decisions
 
are
 
made.
 
 
You
 
will
 
work
 
in
 
pairs,
 
either
 
with
 
a
 
partner
 
you
 
choose
 
or
 
one
 
assigned
 
to
 
you
 
if
 
needed.
 
Each
 
pair
 
will
 
consist
 
of
 
one
 
interviewer ,
 
and
 
one
 
candidate.
 
 
 
 
 Interviewer
 
 
As
 
the
 
interviewer ,
 
your
 
job
 
is
 
to
 
run
 
the
 
interview ,
 
make
 
a
 
hiring
 
decision,
 
and
 
CRUSH
 
DREAMS
 
🤬
 
(earnestly
 
evaluate
 
performance.)
 
You
 
will:
 
●
 
Introduce
 
and
 
explain
 
the
 
problem
 
clearly
 
●
 
Read
 
the
 
question
 
prompt
 
and
 
clarify
 
requirements
 
●
 
Discuss
 
edge
 
cases
 
and
 
constraints
 
●
 
Provide
 
hints
 
when
 
appropriate
 
(without
 
giving
 
away
 
the
 
solution)
 
●
 
Answer
 
the
 
candidate’ s
 
questions
 
●
 
Write
 
and
 
submit
 
○
 
Structured
 
notes
 
taken
 
during
 
the
 
interview
 
○
 
A
 
short
 
evaluation
 
of
 
performance,
 
and
 
a
 
hiring
 
decision
 
Your
 
evaluation
 
should
 
include:
 
●
 
Key
 
strengths
 
●
 
Key
 
weaknesses
 
●
 
A
 
hiring
 
recommendation
 
You
 
will
 
be
 
graded
 
on
 
the
 
quality
 
of
 
your
 
notes
 
and
 
analysis,
 
not
 
on
 
correctness
 
of
 
hints.
 
Your
 
comments
 
and
 
report
 
will
 
not
 
in
 
any
 
way
 
impact
 
your
 
partner ’s
 
grade.
 
 
Interviewer
 
Advice
 
●
 
Guide,
 
don’t
 
solve:
 
Your
 
job
 
is
 
to
 
help
 
them
 
think,
 
not
 
lead
 
them
 
directly
 
to
 
the
 
answer .
 
Start
 
with
 
questions
 
before
 
giving
 
hints.
 
●
 
Follow
 
thinking:
 
If
 
you
 
can’t
 
follow
 
their
 
thinking,
 
ask
 
them
 
questions:
 
“What
 
are
 
you
 
thinking?”
 
or
 
“Can
 
you
 
walk
 
me
 
through
 
your
 
approach.”
 
●
 
Use
 
progressive
 
hints:
 
If
 
they
 
need
 
hints,
 
start
 
with
 
broad
 
questions,
 
then
 
give
 
small
 
nudges
 
only
 
if
 
needed.
 
Avoid
 
jumping
 
straight
 
to
 
the
 
key
 
idea.
 
●
 
Look
 
for
 
positive
 
signals,
 
not
 
perfection:
 
Focus
 
on
 
how
 
they
 
reason,
 
adapt,
 
and
 
communicate.
 
Getting
 
the
 
optimal
 
solution
 
is
 
ideal,
 
but
 
not
 
required
 
if
 
their
 
communication
 
and
 
reasoning
 
is
 
strong.
 
 
●
 
You
 
will
 
be
 
partially
 
graded
 
on
 
your
 
notes
 
in
 
each
 
section
:
 
Good
 
evaluations
 
use
 
concrete
 
examples
 
(e.g.,
 
“identified
 
hashmap
 
approach
 
after
 
hint”
 
or
 
“Clearly
 
communicated
 
why
 
stacks
 
were
 
the
 
optimal
 
solution
 
without
 
prompting”
  
vs.
 
“did
 
well”).
 
 
 Interviewer
 
Evaluation
 
Form
 
Candidate
 
Information
 
●
 
Candidate
 
Name:
 
Katie
 
Schauber
 
●
 
Interviewer
 
Name:
 
Maddie
 
Broderick
 
●
 
Date:
 
5/6
 
●
 
Problem
 
Given:
 
Merge
 
Two
 
Sorted
 
Lists
 
 
1.
 
Problem
 
Understanding
 
(0–4)
 
Did
 
the
 
candidate
 
clearly
 
understand
 
the
 
problem?
 
 
0
 
–
 
Completely
 
misunderstood
 
 
1
 
–
 
Major
 
gaps,
 
needed
 
heavy
 
assistance
 
 
2
 
–
 
Partial
 
understanding,
 
some
 
clarification
 
needed
 
 
3
 
–
 
Mostly
 
clear ,
 
minor
 
clarifications
 
 
4
 
–
 
Fully
 
understood,
 
restated
 
clearly
 
Notes:
 
-
 
Knew
 
from
 
the
 
start
 
the
 
type
 
of
 
problem
 
and
 
was
 
able
 
to
 
reason
 
out
 
the
 
general
 
idea
 
-
 
Asked
 
a
 
few
 
clarifying
 
questions
 
but
 
overall
 
general
 
understanding
 
-
 
Initial
 
idea
 
didn’t
 
really
 
work,
 
but
 
pivoted
 
and
 
found
 
solution
 
that
 
worked
 
 
 
 
 
 2.
 
Communication
 
&
 
Collaboration
 
(0–4)
 
Did
 
the
 
candidate
 
clearly
 
explain
 
their
 
thinking
 
and
 
work
 
effectively
 
with
 
the
 
interviewer?
 
 
0
 
–
 
No
 
explanation,
 
unresponsive
 
or
 
defensive
 
 
1
 
–
 
Very
 
unclear ,
 
struggled
 
with
 
feedback
 
 
2
 
–
 
Some
 
explanation,
 
inconsistent
 
collaboration
 
 
3
 
–
 
Clear ,
 
receptive,
 
reasonably
 
collaborative
 
 
4
 
–
 
Very
 
clear ,
 
structured,
 
highly
 
collaborative
 
and
 
adaptive
 
Notes:
 
Asked
 
clarifying
 
questions,
 
wrote
 
pseudo
 
code
 
and
 
talked
 
it
 
out
 
clearly
 
I
 
asked
 
questions
 
to
 
try
 
and
 
guide
 
toward
 
a
 
simpler
 
solution,
 
she
 
was
 
a
 
little
 
apprehensive
 
but
 
then
 
was
 
collaborative
 
Seemed
 
to
 
mostly
 
be
 
talking
 
it
 
out
 
to
 
herself,
 
and
 
stopped
 
communicating
 
somewhat
 
 
 
 
3.
 
Implementation
 
&
 
Technical
 
Depth
 
(0–4)
 
How
 
well
 
did
 
they
 
implement
 
their
 
solution
 
and
 
reason
 
about
 
its
 
correctness
 
and
 
efficiency?
 
(Coding,
 
testing,
 
complexity ,
 
optimization)
 
 
0
 
–
 
No
 
working
 
solution,
 
no
 
understanding
 
of
 
complexity
 
 
1
 
–
 
Major
 
issues,
 
incorrect
 
or
 
missing
 
complexity
 
reasoning
 
 
2
 
–
 
Partially
 
correct
 
solution,
 
basic
 
or
 
incomplete
 
analysis
 
 
3
 
–
 
Mostly
 
correct,
 
reasonable
 
testing,
 
correct
 
complexity
 
analysis
 
 
4
 
–
 
Clean,
 
correct,
 
well-tested
 
solution
 
with
 
strong
 
optimization
 
and
 
tradeof f
 
discussion
 
Notes:
 Missed
 
a
 
few
 
edge
 
cases
 
initially ,
 
when
 
prompted
 
addressed
 
them.
 
When
 
she
 
realized
 
her
 
solution
 
was
 
slightly
 
off
 
and
 
could
 
be
 
made
 
better
 
she
 
pivoted
 
well
 
 
 
 
 
4.
 
Team
 
Fit
 
&
 
Working
 
Style
 
(0–4)
 
Would
 
you
 
want
 
this
 
person
 
on
 
your
 
team
 
based
 
on
 
how
 
they
 
operate
 
under
 
pressure
 
and
 
uncertainty?
 
 
0
 
–
 
Actively
 
defensive,
 
dismissive,
 
or
 
hard
 
to
 
work
 
with
 
 
1
 
–
 
Friction-heavy ,
 
resistant
 
to
 
feedback
 
or
 
collaboration
 
 
2
 
–
 
Neutral;
 
neither
 
adds
 
nor
 
detracts
 
 
3
 
–
 
Positive
 
teammate;
 
receptive,
 
steady ,
 
easy
 
to
 
work
 
with
 
 
4
 
–
 
Strong
 
team
 
asset;
 
calm
 
under
 
uncertainty ,
 
humble,
 
ownership
 
mindset
 
Notes:
 
Little
 
hesitant
 
to
 
ask
 
for
 
help,
 
wanted
 
to
 
figure
 
it
 
out
 
on
 
her
 
own,
 
but
 
communicated
 
her
 
thought
 
process
 
well
 
 
 
 
 Final
 
Evaluation
 
Total
 
Score:
 
12
 
/
 
16
 
Hiring
 
Recommendation
 
 
Strong
 
Hire
 
 
Hire
 
 
Lean
 
Hire
 
 
Lean
 
No
 
Hire
 
 
No
 
Hire
 
 
Strong
 
No
 
Hire
 
 
Final
 
Decision
 
Summarize
 
your
 
decision
 
in
 
3–5
 
sentences.
 
Focus
 
on:
 
●
 
Key
 
strengths
 
●
 
Key
 
weaknesses
 
●
 
Why
 
you
 
made
 
your
 
decision
 
Use
 
specific
 
examples
 
from
 
the
 
interview
 
to
 
support
 
your
 
decision.
 
-
 
Went
 
through
 
the
 
UMPIRE
 
system
 
well,
 
very
 
communicative
 
-
 
When
 
she
 
got
 
somewhat
 
stuck
 
was
 
hesitant
 
to
 
ask
 
for
 
help
 
but
 
was
 
able
 
to
 
talk
 
through
 
it
 
herself
 
-
 
Had
 
a
 
clear
 
understanding
 
of
 
the
 
problem
 
and
 
the
 
type
 
of
 
solution
 
-
 
Seemed
 
to
 
doubt
 
her
 
solution
 
at
 
the
 
end,
 
double
 
checked
 
with
 
the
 
same
 
example
 
multiple
 
times
 
even
 
though
 
her
 
solution
 
worked
 
 
 
 
Interviewer
 
Grading
 
Guidelines
 
 
●
 
Completion
 
(are
 
all
 
sections
 
filled
 
out)?
 
 
○
 
40%
 
credit
 
●
 
Final
 
Decision
 
&
 
Justification
 
 ○
 
40%
 
credit
 
 
●
 
Per
 
section
 
–
 
Notes:
 
○
 
5%
 
credit
 
if
 
the
 
provided
 
notes
 
were
 
valuable
 
(bullets
 
or
 
sentences
 
with
 
specific
 
examples
 
citing
 
your
 
reasoning
 
for
 
the
 
ranking)
 
 
Candidate
 
As
 
the
 
candidate,
 
your
 
goal
 
is
 
to
 
✨
 
GET
 
A
 
JOB
 
✨
 
(survive
 
a
 
technical
 
interview).
 
You
 
will:
 
●
 
Solve
 
the
 
given
 
coding
 
problem
 
●
 
Aim
 
for
 
an
 
efficient
 
(ideally
 
optimal)
 
solution
 
●
 
Clearly
 
explain
 
your
 
thought
 
process
 
while
 
working
 
●
 
Communicate
 
tradeof fs,
 
ideas,
 
and
 
reasoning
 
out
 
loud
 
●
 
Respond
 
to
 
hints
 
or
 
feedback
 
from
 
the
 
interviewer
 
●
 
Write
 
and
 
submit
 
 
○
 
A
 
working
 
solution
 
○
 
A
 
short
 
writeup
 
explaining
 
the
 
time
 
complexity
 
of
 
your
 
solution
 
and
 
how
 
it
 
solves
 
the
 
problem.
 
For
 
fairness
 
to
 
our
 
less
 
experienced
 
students,
 
you
 
will
 
have
 
access
 
to
 
our
 
Python
 
cheat
 
sheet
 
during
 
the
 
exercise
 
(though
 
eventually
 
you’ll
 
need
 
to
 
be
 
able
 
to
 
take
 
interviews
 
without
 
this!)
 
 
You
 
will
 
be
 
graded
 
on
 
the
 
quality
 
of
 
your
 
submitted
 
code
 
and
 
your
 
problem-solving
 
approach.
 
You
 
will
 
not
 
be
 
graded
 
in
 
any
 
way
 
from
 
the
 
comments
 
or
 
report
 
submitted
 
by
 
the
 
interviewer .
 
You
 
may
 
code
 
on
 
paper ,
 
or
 
in
 
any
 
IDE/text
 
editor
 
that
 
does
 
NOT
 
have
 
AI
 
or
 
autocomplete
 
(examples:
 
Vim,
 
notepad,
 
VsCode
 
without
 
Copilot)
 
 
 
def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    mapp = {}
    j = 0
    for j in len(nums):
        if nums[j] in mapp:
            if j - mapp[nums[j]] <= k:
                return True
        mapp[nums[j]] = j
    return False
        
# Time complexity: O(n) because it runs through the array once
# Solves the problem by running through the list and adding values
# to the hashmap. If the value already exist, it checks if abs(i-j) <= k
```

</details>

---

#### Cheong Ting Eland Chan (`77139`)

- **Problem:** Contains Nearby Duplicate
- **Language:** python
- **Score:** 6/8 (Minor Error)
- **Grading status:** graded
- **Files:** mock_interview.py (direct)

| Test Case | Result |
|-----------|--------|
| true_basic | FAIL |
| true_adjacent | PASS |
| false_too_far | PASS |
| false_k_zero | PASS |
| single_element | PASS |
| no_dups | PASS |
| true_exact_k | FAIL |
| empty | PASS |

<details>
<summary>Edits made by grader</summary>

- [syntax-only] Fixed typo -> 'True'
- [syntax-only] Fixed typo -> 'False'

</details>

<details>
<summary>Extracted Code (77139.py)</summary>

```python
# the two elements have to be the same
# the difference of the indices of the same element has to be less than or equal to k

#this duplicates 

#hash table 

# O(N)

def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    num_set = {}

    for i, num in enumerate(nums):
        temp = num_set.get(num)
        if temp and abs(temp - i) <= k:
            return true
        
        num_set[num] = i

    return false
```

</details>

<details>
<summary>Original Document (77139.txt)</summary>

```
# the two elements have to be the same
# the difference of the indices of the same element has to be less than or equal to k

#this duplicates 

#hash table 

# O(N)

def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    num_set = {}

    for i, num in enumerate(nums):
        temp = num_set.get(num)
        if temp and abs(temp - i) <= k:
            return true
        
        num_set[num] = i

    return false
```

</details>

---

#### Solomon Coverdale (`77672`)

- **Problem:** Contains Nearby Duplicate
- **Language:** python
- **Score:** 8/8 (PASS)
- **Grading status:** graded
- **Files:** Solomon.CS102 PAIRED TECHNICAL INTERVIEW.txt (direct)

| Test Case | Result |
|-----------|--------|
| true_basic | PASS |
| true_adjacent | PASS |
| false_too_far | PASS |
| false_k_zero | PASS |
| single_element | PASS |
| no_dups | PASS |
| true_exact_k | PASS |
| empty | PASS |

<details>
<summary>Extracted Code (77672.py)</summary>

```python
def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    dict = {}
    for i,val in enumerate(nums):
        if val in dict and i-dict[val] <= k:
            return True
        else:
            dict[val] = i

    return False
```

</details>

<details>
<summary>Original Document (77672.txt)</summary>

```
CS102 PAIRED TECHNICAL INTERVIEW

This is the template for what you are expected to submit for the CS102 PAIRED Technical Interview.
Please make sure you have your items in this order when you submit so the we can grade it easier🙏

Refer back to the Paired Technical Interview Print outs to the content you should submit.
In general, you should submit at least a number and some notes for the interviewer side, and your full code solution for the Candidate.

We encourage you to comment your code if you'd like!

Solomon Coverdale

Lilian Yuan

Interviewer Form

[Problem Given] (Just the Name of the Problem is fine)

1) Problem Understanding

3 - Mostly clear, minor clarifications
Notes: Seemed to mostly understand the question, still had to ask some questions

2) Communication & Collaboration

4 - Very clear, structured, highly collaborative and adaptive
Notes: explained thought process well

3) Implementation & Technical Depth

4 - clean, correct, well-tested solution with strong optimization and tradeoff discussion
Notes: used binary search(optimal for problem)

4) Team Fit & Working Style

4 - Strong team asset; calm under uncertainty, humble, ownership mindset

Final Evaluation

Candidate has strong communication skills, will work good on a team. Knows various searching algorithms and is personable, strong hire.

Final Decision

Strong hire

Candidate Form

def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
	dict = {}
	for i,val in enumerate(nums):
		if val in dict and i-dict[val] <= k:
			return True
		else:
			dict[val] = i

	return False
```

</details>

---

#### Sude Genc (`73748`)

- **Problem:** Contains Nearby Duplicate
- **Language:** python
- **Score:** 8/8 (PASS)
- **Grading status:** graded
- **Files:** CS102 PAIRED TECHNICAL INTERVIEW-2.txt (direct)

| Test Case | Result |
|-----------|--------|
| true_basic | PASS |
| true_adjacent | PASS |
| false_too_far | PASS |
| false_k_zero | PASS |
| single_element | PASS |
| no_dups | PASS |
| true_exact_k | PASS |
| empty | PASS |

<details>
<summary>Edits made by grader</summary>

- [syntax-only] Fixed typo -> 'True'
- [syntax-only] Fixed typo -> 'False'

</details>

<details>
<summary>Extracted Code (73748.py)</summary>

```python
def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    d = {}
    for i , var in enumerate(nums):
        if var in d and i-d[var] <= k:
            return True
        else:
            d[var]=i
    return False

#time complexity for this solution is O(n). turns list into a dictionary(hashmap), 
#then looped through variables using sliding windows. if satisfies the condition return true
# else add to the dictionary(hashmap) and continue to loop. at the end of the loop if condition
# did not met return false
```

</details>

<details>
<summary>Original Document (73748.txt)</summary>

```
CS102 PAIRED TECHNICAL INTERVIEW

This is the template for what you are expected to submit for the CS102 PAIRED Technical Interview.
Please make sure you have your items in this order when you submit so the we can grade it easier🙏

Refer back to the Paired Technical Interview Print outs to the content you should submit.
In general, you should submit at least a number and some notes for the interviewer side, and your full code solution for the Candidate.

We encourage you to comment your code if you'd like!

Sude Genc 

Isabella Yang

Interviewer Form

Longest Substring Without Repeating Characters

1) Problem Understanding
	4

2) Communication & Collaboration
	3

3) Implementation & Technical Depth
	4

4) Team Fit & Working Style
	4

Final Evaluation
	15/16

Final Decision
	I am hiring her 

Candidate Form

def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    d = {}
    for i , var in enumerate(nums):
        if var in d and i-d[var] <= k:
            return True
        else:
            d[var]=i
    return False

#time complexity for this solution is O(n). turns list into a dictionary(hashmap), 
#then looped through variables using sliding windows. if satisfies the condition return true
# else add to the dictionary(hashmap) and continue to loop. at the end of the loop if condition
# did not met return false
```

</details>

---

#### Jason Guo (`79145`)

- **Problem:** Contains Nearby Duplicate
- **Language:** python
- **Score:** 1/8 (Critical Error)
- **Grading status:** graded
- **Files:** interview.txt (direct)

| Test Case | Result |
|-----------|--------|
| true_basic | FAIL |
| true_adjacent | FAIL |
| false_too_far | FAIL |
| false_k_zero | FAIL |
| single_element | FAIL |
| no_dups | FAIL |
| true_exact_k | FAIL |
| empty | PASS |

<details>
<summary>Extracted Code (79145.py)</summary>

```python
def containsNearbyDuplicate(nums: List[int], k:int) -> bool:
    s = set()
    d = {}
    
    for i in range(len(nums)):
    
        if nums[i] in s:
            if abs(d[nums[i]] - i) <= k:
                return True
            else:
                d[nums[i]] = i
        else:
            s.append(nums[i]) 
            d[nums[i]] = i
    
    return False
            
# Time complexity is O(n) because set and dictionary lookup is O(1) so only the for loop O(n) applies.
# This solves the problem by creating a set to detect duplicates and the dictionary to keep track of indices. It works by iterating through the array until it finds a duplicate. When it finds a duplicate, it looks up the previous indice with the dictionary and does the abs(i - j) <= k operation to return True or continue if False until it reaches the end of the array.
```

</details>

<details>
<summary>Original Document (79145.txt)</summary>

```
def containsNearbyDuplicate(nums: List[int], k:int) -> bool:
	s = set()
	d = {}
	
	for i in range(len(nums)):
	
		if nums[i] in s:
			if abs(d[nums[i]] - i) <= k:
				return True
			else:
				d[nums[i]] = i
		else:
			s.append(nums[i]) 
			d[nums[i]] = i
	
	return False
			
# Time complexity is O(n) because set and dictionary lookup is O(1) so only the for loop O(n) applies.
# This solves the problem by creating a set to detect duplicates and the dictionary to keep track of indices. It works by iterating through the array until it finds a duplicate. When it finds a duplicate, it looks up the previous indice with the dictionary and does the abs(i - j) <= k operation to return True or continue if False until it reaches the end of the array.
```

</details>

---

#### Brian Lin (`69560`)

- **Problem:** Contains Nearby Duplicate
- **Language:** java
- **Score:** 5/8 (Minor Error)
- **Grading status:** graded
- **Repair level:** aggressive
- **Files:** brian technical interiew.txt (direct)

| Test Case | Result |
|-----------|--------|
| true_basic | FAIL |
| true_adjacent | FAIL |
| false_too_far | PASS |
| false_k_zero | PASS |
| single_element | PASS |
| no_dups | PASS |
| true_exact_k | FAIL |
| empty | PASS |

<details>
<summary>Edits made by grader</summary>

- [syntax-only] Mechanical Java->Python transpile
- [syntax-only] Replaced && with and
- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def containsNearbyDuplicate(nums, k): return 0`

</details>

<details>
<summary>Extracted Code (69560.java)</summary>

```java
public Boolean containsNearbyDuplicate(int[] nums, int k){


    Map<Integer,Integer> x = new HashMap<>();

    for(int i=0; i<nums.length();i++){
        int val = nums[i];


        if(x.containsValue(val) && i - x.value(i) <= k){
            return true;
        }else{
            x.put(value,i);
        }
    }
    return false;
}
```

</details>

<details>
<summary>Original Document (69560.txt)</summary>

```
public Boolean containsNearbyDuplicate(int[] nums, int k){


	Map<Integer,Integer> x = new HashMap<>();

	for(int i=0; i<nums.length();i++){
		int val = nums[i];


		if(x.containsValue(val) && i - x.value(i) <= k){
			return true;
		}else{
			x.put(value,i);
		}
	}
	return false;
}
```

</details>

---

#### Tiffany Lin (`78601`)

- **Problem:** Contains Nearby Duplicate
- **Language:** python
- **Score:** 4/8 (Critical Error)
- **Grading status:** graded
- **Files:** CS102 PAIRED TECHNICAL INTERVIEW.txt (direct)

| Test Case | Result |
|-----------|--------|
| true_basic | FAIL |
| true_adjacent | FAIL |
| false_too_far | PASS |
| false_k_zero | PASS |
| single_element | PASS |
| no_dups | PASS |
| true_exact_k | FAIL |
| empty | FAIL |

<details>
<summary>Edits made by grader</summary>

- [syntax-only] Fixed --> to ->
- [syntax-only] Fixed typo -> 'True'
- [syntax-only] Fixed typo -> 'False'

</details>

<details>
<summary>Extracted Code (78601.py)</summary>

```python
def containsNearbyDuplicate(nums:List[int],k:int) --> bool:
    d = {}
    
    for i,j in enumerate(nums):
        if j in d and i - d[j] <= k:
            return true
        else:
            d[j] = i   
            
        return false
```

</details>

<details>
<summary>Original Document (78601.txt)</summary>

```
CS102 PAIRED TECHNICAL INTERVIEW

This is the template for what you are expected to submit for the CS102 PAIRED Technical Interview.
Please make sure you have your items in this order when you submit so the we can grade it easier🙏

Refer back to the Paired Technical Interview Print outs to the content you should submit.
In general, you should submit at least a number and some notes for the interviewer side, and your full code solution for the Candidate.

We encourage you to comment your code if you'd like!

Tiffany Lin

Ryan Zhang

Interviewer Form

Longest Substring Without Repeating Characters

1) Problem Understanding
3/4
-Identified that it was hashmap at first and changed to hashsets after hints provided
- Needed help understanding how hashset works
- Said "Didn't read the problem correctly" but after explantation he understood

2) Communication & Collaboration
3/4
- Asks question when needed the help
- Was clear on what he wanted to do
- Explained the whole code/working on the code fully/ Explained the reasoning about every single line

3) Implementation & Technical Depth
3/4
- Solution was close to the actual given code, but wasn't exact code but he did it not exactly the same
- Overall went the right path after guidance 
- 90% similar to the solution
- Solution should be able to run
4) Team Fit & Working Style
3/4
-No signs of acting defensive,nor resistant to feedback
- Stands up to mistake and thanks for the help given
- Was easy to work with, didn't stiff up or have signs of bad communication skills/ wasn't awkward
Final Evaluation
12/16
Lean Hire
Final Decision
Was a okay communcatior, but I wouldn't consider him the best, as at some time he would repeat asking questions since he didn't understand or freeze for a few seconds. Explained the step by step really well on why this would work and how it works. He didn't mention anything about the time complexity. I made this decision because there might be better candidates out there and he did pretty average, but nothing outstanding.

Candidate Form

Contains Duplicate II
def containsNearbyDuplicate(nums:List[int],k:int) --> bool:
    d = {}
    
    for i,j in enumerate(nums):
        if j in d and i - d[j] <= k:
            return true
        else:
            d[j] = i   
            
        return false
        
        
I started out thinking it was a sliding window/two pointer two sum problem which the interviewer said would work but the time complexity would be O(N^2) and asked if I 
can make it faster, so he guided me to use a hashmap. I used enumerate instead of range becauseit would check the indicies and nums and i added to the dic if it did not 
seen yet. and checked if the incides subtracted from each other is less than equal to k if so return true if not return false. So i made it a O(N) time complexity.
```

</details>

---

#### Andrew McBean (`74837`)

- **Problem:** Contains Nearby Duplicate
- **Language:** python
- **Score:** 1/8 (Critical Error)
- **Grading status:** graded
- **Files:** CS102 PAIRED TECHNICAL INTERVIEW.txt (direct)

| Test Case | Result |
|-----------|--------|
| true_basic | FAIL |
| true_adjacent | FAIL |
| false_too_far | FAIL |
| false_k_zero | FAIL |
| single_element | FAIL |
| no_dups | FAIL |
| true_exact_k | FAIL |
| empty | PASS |

<details>
<summary>Edits made by grader</summary>

- [syntax-only] Extracted function block from noisy file

</details>

<details>
<summary>Extracted Code (74837.py)</summary>

```python
The time complexity of the code is O(n). The function utilizes a fixed sliding window where both pointers are incremented checking for the condition of whether there are duplicates. To check the duplicates I used a hash map, but a hash set could have also been used to simplify the if statements. It solves the problem by returning True when a duplicate is detected and False if the entire function runs without a return.

def containsNearbyDuplicate(nums: List[int], k:int) -> bool:
    unqique = {}
    for i in range(k):
        if unique.get(num[i], 0) == 0:
            unique[nums[i]] = i
        else:
            return True
    for i in range(k, len(nums)):
        if unique.get(nums[i], 0) == 0:
            unique[nums[i]] = i
        else:
            return True
        dic.remove(nums[i-k])
    return False
```

</details>

<details>
<summary>Original Document (74837.txt)</summary>

```
Andrew McBean

Jin Noh

The time complexity of the code is O(n). The function utilizes a fixed sliding window where both pointers are incremented checking for the condition of whether there are duplicates. To check the duplicates I used a hash map, but a hash set could have also been used to simplify the if statements. It solves the problem by returning True when a duplicate is detected and False if the entire function runs without a return.

def containsNearbyDuplicate(nums: List[int], k:int) -> bool:
    unqique = {}
    for i in range(k):
        if unique.get(num[i], 0) == 0:
            unique[nums[i]] = i
        else:
            return True
    for i in range(k, len(nums)):
        if unique.get(nums[i], 0) == 0:
            unique[nums[i]] = i
        else:
            return True
        dic.remove(nums[i-k])
    return False
```

</details>

---

#### Danila Safronov (`78296`)

- **Problem:** Contains Nearby Duplicate
- **Language:** python
- **Score:** 8/8 (PASS)
- **Grading status:** graded
- **Files:** Quiz 3 Leetcode.txt (direct)

| Test Case | Result |
|-----------|--------|
| true_basic | PASS |
| true_adjacent | PASS |
| false_too_far | PASS |
| false_k_zero | PASS |
| single_element | PASS |
| no_dups | PASS |
| true_exact_k | PASS |
| empty | PASS |

<details>
<summary>Extracted Code (78296.py)</summary>

```python
def containsNearbyDuplicate(nums: List[int], k: int) -> bool: 

    seen = {}

    for i, num in enumerate(nums): 
        if num in seen and i - seen[num] <= k:
            return True
        seen[num] = i
    return False
```

</details>

<details>
<summary>Original Document (78296.txt)</summary>

```
Candidate - Danila Safronov
Interviewer - Carson Carey 



def containsNearbyDuplicate(nums: List[int], k: int) -> bool: 

	seen = {}

	for i, num in enumerate(nums): 
		if num in seen and i - seen[num] <= k:
			return True
		seen[num] = i
	return False
```

</details>

---

#### Jack Stevens (`77510`)

- **Problem:** Contains Nearby Duplicate
- **Language:** pseudocode
- **Score:** 6/8 (Minor Error)
- **Grading status:** graded
- **Files:** Jack Stevens paried interview.txt (direct)

| Test Case | Result |
|-----------|--------|
| true_basic | PASS |
| true_adjacent | PASS |
| false_too_far | FAIL |
| false_k_zero | FAIL |
| single_element | PASS |
| no_dups | PASS |
| true_exact_k | PASS |
| empty | PASS |

<details>
<summary>Edits made by grader</summary>

- [syntax-only] Lowered keyword 'Def'
- [syntax-only] Lowered keyword 'For'
- [syntax-only] Lowered keyword 'If'
- [syntax-only] Lowered keyword 'Return'
- [syntax-only] Replaced em/en dashes with hyphens

</details>

<details>
<summary>Extracted Code (77510.py)</summary>

```python
#Use a set to hold checked values of the array to compare the current index to the past values #to find duplicates
#I can use the indexes within the set and then add that to the current list length to find the #original list indexes and compare them to K 

Def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
        s = {}
        For i in range(len(nums)):
                if nums[i] in s:
                        If(abs(i – s[nums[i]]) <= k):
                                Return True
                s[i] = nums[i]
        return False
```

</details>

<details>
<summary>Original Document (77510.txt)</summary>

```

Candidate Form

#Use a set to hold checked values of the array to compare the current index to the past values #to find duplicates
#I can use the indexes within the set and then add that to the current list length to find the #original list indexes and compare them to K 

Def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
	s = {}
	For i in range(len(nums)):
		if nums[i] in s:
			If(abs(i – s[nums[i]]) <= k):
				Return True
		s[i] = nums[i]
 	return False
```

</details>

---

#### Evan Weisberg (`66281`)

- **Problem:** Contains Nearby Duplicate
- **Language:** python
- **Score:** 8/8 (PASS)
- **Grading status:** graded
- **Files:** class Solution.txt (direct)

| Test Case | Result |
|-----------|--------|
| true_basic | PASS |
| true_adjacent | PASS |
| false_too_far | PASS |
| false_k_zero | PASS |
| single_element | PASS |
| no_dups | PASS |
| true_exact_k | PASS |
| empty | PASS |

<details>
<summary>Extracted Code (66281.py)</summary>

```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for index,n in enumerate(nums):
            if n in d:
                if index-d[n] <= k:
                    return True 
            d[n] = index
        return False
```

</details>

<details>
<summary>Original Document (66281.txt)</summary>

```
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for index,n in enumerate(nums):
            if n in d:
                if index-d[n] <= k:
                    return True 
            d[n] = index
        return False
```

</details>

---

#### Ethan Wong (`75870`)

- **Problem:** Contains Nearby Duplicate
- **Language:** python
- **Score:** 8/8 (PASS)
- **Grading status:** graded
- **Files:** TechnicalInterview.txt (direct)

| Test Case | Result |
|-----------|--------|
| true_basic | PASS |
| true_adjacent | PASS |
| false_too_far | PASS |
| false_k_zero | PASS |
| single_element | PASS |
| no_dups | PASS |
| true_exact_k | PASS |
| empty | PASS |

<details>
<summary>Extracted Code (75870.py)</summary>

```python
def containsNearbyDuplicate(nums: List[int], k: in) -> bool:
    dict = {}

    for key, value in enumerate(nums):
        if value in dict:
            if abs(key - dict[value]) <= k:
                return True
            dict[value] = key
        else:
            dict[value] = key
    
    return False
```

</details>

<details>
<summary>Original Document (75870.txt)</summary>

```
def containsNearbyDuplicate(nums: List[int], k: in) -> bool:
	dict = {}

	for key, value in enumerate(nums):
		if value in dict:
			if abs(key - dict[value]) <= k:
				return True
			dict[value] = key
		else:
			dict[value] = key
	
	return False
```

</details>

---

### Evaluate Reverse Polish Notation

#### Ava Attina (`66963`)

- **Problem:** Evaluate Reverse Polish Notation
- **Language:** python
- **Score:** 0/7 (Critical Error)
- **Grading status:** graded
- **Repair level:** aggressive
- **Files:** Ava Attina CS 102 Paired Technical Interview Printouts - General Info-3.pdf (pdf); cs102quiz.txt (direct)

| Test Case | Result |
|-----------|--------|
| example1 | FAIL |
| example2 | FAIL |
| example3 | FAIL |
| add_only | FAIL |
| single | FAIL |
| subtract | FAIL |
| neg_divide | FAIL |

<details>
<summary>Edits made by grader</summary>

- [syntax-only] Appended 1 missing closing bracket(s)
- [ambiguous] Conservative re-indent: normalized indent levels to 4-space tiers
- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def evalRPN(tokens): return 0`

</details>

<details>
<summary>Extracted Code (66963.py)</summary>

```python
def evalPRN(tokens: List[str]) -> int:
    stack = []
    for i in tokens:
        
        if i == '+':
            stack.append(stack.pop() + stack.pop())
        elif i == '-':
            second, first = stack.pop(), stack.pop()
            stack.append(first - second)
        elif i == '*':
            stack.append(stack.pop() * stack.pop()
        elif i == '/':
            second, first = stack.pop(), stack.pop()
            stack.append(int(first/second))
        else:
        
            stack.append(int(i))
        
        return stack[0]
# O(1) time complexity
# Ava Attina
```

</details>

<details>
<summary>Original Document (66963.txt)</summary>

```
Paired
 
Technical
 
Interview
 
Overview
 
Mock
 
interviews
 
are
 
one
 
of
 
the
 
most
 
effective
 
ways
 
to
 
prepare
 
for
 
technical
 
interviews.
 
They
 
help
 
you
 
practice
 
solving
 
problems
 
under
 
realistic
 
time
 
pressure
 
while
 
also
 
developing
 
the
 
technical
 
communication
 
skills
 
required
 
in
 
a
 
real
 
interview
 
setting.
 
In
 
addition,
 
you’ll
 
gain
 
experience
 
evaluating
 
a
 
candidate’ s
 
performance
 
from
 
the
 
interviewer ’s
 
perspective,
 
which
 
will
 
help
 
you
 
understand
 
how
 
hiring
 
decisions
 
are
 
made.
 
 
You
 
will
 
work
 
in
 
pairs,
 
either
 
with
 
a
 
partner
 
you
 
choose
 
or
 
one
 
assigned
 
to
 
you
 
if
 
needed.
 
Each
 
pair
 
will
 
consist
 
of
 
one
 
interviewer ,
 
and
 
one
 
candidate.
 
 
 
 
 Interviewer
 
 
As
 
the
 
interviewer ,
 
your
 
job
 
is
 
to
 
run
 
the
 
interview ,
 
make
 
a
 
hiring
 
decision,
 
and
 
CRUSH
 
DREAMS
 
🤬
 
(earnestly
 
evaluate
 
performance.)
 
You
 
will:
 
●
 
Introduce
 
and
 
explain
 
the
 
problem
 
clearly
 
●
 
Read
 
the
 
question
 
prompt
 
and
 
clarify
 
requirements
 
●
 
Discuss
 
edge
 
cases
 
and
 
constraints
 
●
 
Provide
 
hints
 
when
 
appropriate
 
(without
 
giving
 
away
 
the
 
solution)
 
●
 
Answer
 
the
 
candidate’ s
 
questions
 
●
 
Write
 
and
 
submit
 
○
 
Structured
 
notes
 
taken
 
during
 
the
 
interview
 
○
 
A
 
short
 
evaluation
 
of
 
performance,
 
and
 
a
 
hiring
 
decision
 
Your
 
evaluation
 
should
 
include:
 
●
 
Key
 
strengths
 
●
 
Key
 
weaknesses
 
●
 
A
 
hiring
 
recommendation
 
You
 
will
 
be
 
graded
 
on
 
the
 
quality
 
of
 
your
 
notes
 
and
 
analysis,
 
not
 
on
 
correctness
 
of
 
hints.
 
Your
 
comments
 
and
 
report
 
will
 
not
 
in
 
any
 
way
 
impact
 
your
 
partner ’s
 
grade.
 
 
Interviewer
 
Advice
 
●
 
Guide,
 
don’t
 
solve:
 
Your
 
job
 
is
 
to
 
help
 
them
 
think,
 
not
 
lead
 
them
 
directly
 
to
 
the
 
answer .
 
Start
 
with
 
questions
 
before
 
giving
 
hints.
 
●
 
Follow
 
thinking:
 
If
 
you
 
can’t
 
follow
 
their
 
thinking,
 
ask
 
them
 
questions:
 
“What
 
are
 
you
 
thinking?”
 
or
 
“Can
 
you
 
walk
 
me
 
through
 
your
 
approach.”
 
●
 
Use
 
progressive
 
hints:
 
If
 
they
 
need
 
hints,
 
start
 
with
 
broad
 
questions,
 
then
 
give
 
small
 
nudges
 
only
 
if
 
needed.
 
Avoid
 
jumping
 
straight
 
to
 
the
 
key
 
idea.
 
●
 
Look
 
for
 
positive
 
signals,
 
not
 
perfection:
 
Focus
 
on
 
how
 
they
 
reason,
 
adapt,
 
and
 
communicate.
 
Getting
 
the
 
optimal
 
solution
 
is
 
ideal,
 
but
 
not
 
required
 
if
 
their
 
communication
 
and
 
reasoning
 
is
 
strong.
 
 
●
 
You
 
will
 
be
 
partially
 
graded
 
on
 
your
 
notes
 
in
 
each
 
section
:
 
Good
 
evaluations
 
use
 
concrete
 
examples
 
(e.g.,
 
“identified
 
hashmap
 
approach
 
after
 
hint”
 
or
 
“Clearly
 
communicated
 
why
 
stacks
 
were
 
the
 
optimal
 
solution
 
without
 
prompting”
  
vs.
 
“did
 
well”).
 
 
 Interviewer
 
Evaluation
 
Form
 
Candidate
 
Information
 
●
 
Candidate
 
Name:
 
Micheal
 
DiNapoli
 
●
 
Interviewer
 
Name:
 
Ava
 
Attina
 
●
 
Date:
 
5/6/26
 
●
 
Problem
 
Given:
 
Longest
 
Subarray
 
 
1.
 
Problem
 
Understanding
 
(0–4)
 
Did
 
the
 
candidate
 
clearly
 
understand
 
the
 
problem?
 
 
0
 
–
 
Completely
 
misunderstood
 
 
1
 
–
 
Major
 
gaps,
 
needed
 
heavy
 
assistance
 
 
2
 
–
 
Partial
 
understanding,
 
some
 
clarification
 
needed
 
 
3
 
–
 
Mostly
 
clear ,
 
minor
 
clarifications
 
 
4
 
–
 
Fully
 
understood,
 
restated
 
clearly
 
Notes:
 
 
 
 
Understood
 
the
 
problem
 
and
 
hints
 
given
 
clearly
 
 
 2.
 
Communication
 
&
 
Collaboration
 
(0–4)
 
Did
 
the
 
candidate
 
clearly
 
explain
 
their
 
thinking
 
and
 
work
 
effectively
 
with
 
the
 
interviewer?
 
 
0
 
–
 
No
 
explanation,
 
unresponsive
 
or
 
defensive
 
 
1
 
–
 
Very
 
unclear ,
 
struggled
 
with
 
feedback
 
 
2
 
–
 
Some
 
explanation,
 
inconsistent
 
collaboration
 
 
3
 
–
 
Clear ,
 
receptive,
 
reasonably
 
collaborative
 
 
4
 
–
 
Very
 
clear ,
 
structured,
 
highly
 
collaborative
 
and
 
adaptive
 
Notes:
 
Asked
 
questions
 
when
 
appropriate
 
and
 
explained
 
his
 
reasoning
 
clearly
 
 
 
 
3.
 
Implementation
 
&
 
Technical
 
Depth
 
(0–4)
 
How
 
well
 
did
 
they
 
implement
 
their
 
solution
 
and
 
reason
 
about
 
its
 
correctness
 
and
 
efficiency?
 
(Coding,
 
testing,
 
complexity ,
 
optimization)
 
 
0
 
–
 
No
 
working
 
solution,
 
no
 
understanding
 
of
 
complexity
 
 
1
 
–
 
Major
 
issues,
 
incorrect
 
or
 
missing
 
complexity
 
reasoning
 
 
2
 
–
 
Partially
 
correct
 
solution,
 
basic
 
or
 
incomplete
 
analysis
 
 
3
 
–
 
Mostly
 
correct,
 
reasonable
 
testing,
 
correct
 
complexity
 
analysis
 
 
4
 
–
 
Clean,
 
correct,
 
well-tested
 
solution
 
with
 
strong
 
optimization
 
and
 
tradeof f
 
discussion
 
Notes:
 
 
Got
 
the
 
correct
 
solution
 
and
 
considered
 
all
 
edge
 
cases
 
 
 4.
 
Team
 
Fit
 
&
 
Working
 
Style
 
(0–4)
 
Would
 
you
 
want
 
this
 
person
 
on
 
your
 
team
 
based
 
on
 
how
 
they
 
operate
 
under
 
pressure
 
and
 
uncertainty?
 
 
0
 
–
 
Actively
 
defensive,
 
dismissive,
 
or
 
hard
 
to
 
work
 
with
 
 
1
 
–
 
Friction-heavy ,
 
resistant
 
to
 
feedback
 
or
 
collaboration
 
 
2
 
–
 
Neutral;
 
neither
 
adds
 
nor
 
detracts
 
 
3
 
–
 
Positive
 
teammate;
 
receptive,
 
steady ,
 
easy
 
to
 
work
 
with
 
 
4
 
–
 
Strong
 
team
 
asset;
 
calm
 
under
 
uncertainty ,
 
humble,
 
ownership
 
mindset
 
Notes:
 
Good
 
communicator
 
and
 
problem
 
solver
 
 
 
 
 Final
 
Evaluation
 
Total
 
Score:
 
16
 
/
 
16
 
Hiring
 
Recommendation
 
 
Strong
 
Hire
 
 
Hire
 
 
Lean
 
Hire
 
 
Lean
 
No
 
Hire
 
 
No
 
Hire
 
 
Strong
 
No
 
Hire
 
 
Final
 
Decision
 
Summarize
 
your
 
decision
 
in
 
3–5
 
sentences.
 
Focus
 
on:
 
●
 
Key
 
strengths
 
●
 
Key
 
weaknesses
 
●
 
Why
 
you
 
made
 
your
 
decision
 
Use
 
specific
 
examples
 
from
 
the
 
interview
 
to
 
support
 
your
 
decision.
 
 
 
Asked
 
questions
 
when
 
appropriate
 
and
 
carefully
 
considered
 
the
 
hints
 
I
 
gave.
 
Occasionally
 
did
 
not
 
ask
 
questions
 
when
 
they
 
were
 
needed.
 
I
 
would
 
hire
 
this
 
client
 
as
 
strong
 
communication
 
and
 
problem
 
solving
 
skills
 
are
 
important
 
for
 
a
 
cohesive
 
team.
 
 
Interviewer
 
Grading
 
Guidelines
 
 
●
 
Completion
 
(are
 
all
 
sections
 
filled
 
out)?
 
 
○
 
40%
 
credit
 
●
 
Final
 
Decision
 
&
 
Justification
 
 
○
 
40%
 
credit
 
 
●
 
Per
 
section
 
–
 
Notes:
 ○
 
5%
 
credit
 
if
 
the
 
provided
 
notes
 
were
 
valuable
 
(bullets
 
or
 
sentences
 
with
 
specific
 
examples
 
citing
 
your
 
reasoning
 
for
 
the
 
ranking)
 
 
Candidate
 
As
 
the
 
candidate,
 
your
 
goal
 
is
 
to
 
✨
 
GET
 
A
 
JOB
 
✨
 
(survive
 
a
 
technical
 
interview).
 
You
 
will:
 
●
 
Solve
 
the
 
given
 
coding
 
problem
 
●
 
Aim
 
for
 
an
 
efficient
 
(ideally
 
optimal)
 
solution
 
●
 
Clearly
 
explain
 
your
 
thought
 
process
 
while
 
working
 
●
 
Communicate
 
tradeof fs,
 
ideas,
 
and
 
reasoning
 
out
 
loud
 
●
 
Respond
 
to
 
hints
 
or
 
feedback
 
from
 
the
 
interviewer
 
●
 
Write
 
and
 
submit
 
 
○
 
A
 
working
 
solution
 
○
 
A
 
short
 
writeup
 
explaining
 
the
 
time
 
complexity
 
of
 
your
 
solution
 
and
 
how
 
it
 
solves
 
the
 
problem.
 
For
 
fairness
 
to
 
our
 
less
 
experienced
 
students,
 
you
 
will
 
have
 
access
 
to
 
our
 
Python
 
cheat
 
sheet
 
during
 
the
 
exercise
 
(though
 
eventually
 
you’ll
 
need
 
to
 
be
 
able
 
to
 
take
 
interviews
 
without
 
this!)
 
 
You
 
will
 
be
 
graded
 
on
 
the
 
quality
 
of
 
your
 
submitted
 
code
 
and
 
your
 
problem-solving
 
approach.
 
You
 
will
 
not
 
be
 
graded
 
in
 
any
 
way
 
from
 
the
 
comments
 
or
 
report
 
submitted
 
by
 
the
 
interviewer .
 
You
 
may
 
code
 
on
 
paper ,
 
or
 
in
 
any
 
IDE/text
 
editor
 
that
 
does
 
NOT
 
have
 
AI
 
or
 
autocomplete
 
(examples:
 
Vim,
 
notepad,
 
VsCode
 
without
 
Copilot)
 
 
This
 
experience
 
demonstrated
 
to
 
me
 
the
 
importance
 
of
 
communicating
 
during
 
a
 
technical
 
interview .
 
Not
 
only
 
is
 
communication
 
important
 
because
 
the
 
interviewer
 
can
 
give
 
you
 
insight
 
on
 
the
 
problem,
 
but
 
you
 
can
 
also
 
demonstrate
 
your
 
technical
 
knowledge
 
even
 
if
 
you
 
don’t
 
arrive
 
at
 
the
 
correct
 
solution.
 
def evalPRN(tokens: List[str]) -> int:
	stack = []
	for i in tokens:
		
		if i == '+':
			stack.append(stack.pop() + stack.pop())
		elif i == '-':
			second, first = stack.pop(), stack.pop()
			stack.append(first - second)
		elif i == '*':
			stack.append(stack.pop() * stack.pop()
		elif i == '/':
			second, first = stack.pop(), stack.pop()
			stack.append(int(first/second))
		else:
		
			stack.append(int(i))
		
		return stack[0]
# O(1) time complexity
# Ava Attina
```

</details>

---

#### Sean Carhart (`77764`)

- **Problem:** Evaluate Reverse Polish Notation
- **Language:** java
- **Score:** 0/7 (Critical Error)
- **Grading status:** graded
- **Repair level:** aggressive
- **Files:** CS102 Leetcode.txt (direct)

| Test Case | Result |
|-----------|--------|
| example1 | FAIL |
| example2 | FAIL |
| example3 | FAIL |
| add_only | FAIL |
| single | FAIL |
| subtract | FAIL |
| neg_divide | FAIL |

<details>
<summary>Edits made by grader</summary>

- [syntax-only] Mechanical Java->Python transpile
- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def evalRPN(tokens): return 0`

</details>

<details>
<summary>Extracted Code (77764.java)</summary>

```java
public int evalRPN(String[] tokens){
deque<Integer> stack = new deque<>();
for (int i = 0;  i < tokens.length; i++)
{
        String character = tokens[i];
        if(character.equals(“+”))
        {
                int num2 = stack.pop();
                int num1 = stack.pop();
                int result = num1 + num2;
                stack.push(result);
        }
        else if(character.equals(“-”))
        {
                int num2 = stack.pop();
                int num1 = stack.pop();
                int result = num1 - num2;
                stack.push(result);
        }
        else if(character.equals(“*”))
        {
                int num2 = stack.pop();
                int num1 = stack.pop();
                int result = num1 * num2;
                stack.push(result);
        }
        else if(character.equals(“/”))
        {
                int num2 = stack.pop();
                int num1 = stack.pop();
                int result = num1 / num2;
                stack.push(result);
        }
        else
        {
                int num = character.parseInt();
                stack.push(num);
        }
}
return stack.pop();
}
```

</details>

<details>
<summary>Original Document (77764.txt)</summary>

```
﻿Sean Carhart

Vikram Minhas

Interviewer Form

Merge two sorted lists

1) Problem Understanding

3/4

Notes:
Initially misunderstood the question and started solving it with an arraylist, but quickly got back on track after a small redirection.

2) Communication & Collaboration

4/4

Notes:
Very able to explain everything they did and why they were doing it.

3) Implementation & Technical Depth

3/4

Notes:
Mostly correct, missed final part of the solution adding the rest of the larger linked list to the sorted one.

4) Team Fit & Working Style

4/4

Notes:
Very sociable. Had to quickly adapt after a brief misunderstanding.

Final Evaluation

14/16
Hire

Final Decision

I would say this is definatley a hire. A slight weakness would be that he didn't read the problem close enough, which led to an incomplete solution and him having to restart. However, he was able to effectively explain his solution, was adaptable, and appeared very knowledgeable and confident.

Candidate Form

Problem: Evaluate Reverse Polish Notation - Candidate


public int evalRPN(String[] tokens){
deque<Integer> stack = new deque<>();
for (int i = 0;  i < tokens.length; i++)
{
        String character = tokens[i];
        if(character.equals(“+”))
        {
                int num2 = stack.pop();
                int num1 = stack.pop();
                int result = num1 + num2;
                stack.push(result);
        }
        else if(character.equals(“-”))
        {
                int num2 = stack.pop();
                int num1 = stack.pop();
                int result = num1 - num2;
                stack.push(result);
        }
        else if(character.equals(“*”))
        {
                int num2 = stack.pop();
                int num1 = stack.pop();
                int result = num1 * num2;
                stack.push(result);
        }
        else if(character.equals(“/”))
        {
                int num2 = stack.pop();
                int num1 = stack.pop();
                int result = num1 / num2;
                stack.push(result);
        }
        else
        {
                int num = character.parseInt();
                stack.push(num);
        }
}
return stack.pop();
}

The complexity of my solution is O(n). It iterates through the array, if the string character is an operator, then it pops the last two integers off of the stack and performs that operator on them, before adding that result back to the top of the stack. If the String character isn't an operator, then by the rules of the question it must be an integer, and that integer is simply added to the stack. Because it is in correct notation, I should not have to worry about an operator appearing before two integers and breaking the code. The last integer in the stack should be the arithmetic result, so return it.
```

</details>

---

#### Ashley Carozza (`69252`)

- **Problem:** Evaluate Reverse Polish Notation
- **Language:** python
- **Score:** 7/7 (PASS)
- **Grading status:** graded
- **Files:** CS102 PAIRED TECHNICAL INTERVIEW - Ashley Carozza.txt (direct)

| Test Case | Result |
|-----------|--------|
| example1 | PASS |
| example2 | PASS |
| example3 | PASS |
| add_only | PASS |
| single | PASS |
| subtract | PASS |
| neg_divide | PASS |

<details>
<summary>Extracted Code (69252.py)</summary>

```python
def evalRPN(tokens: List[str]) -> int:
    #create empty stack
    stack = []
    #set of the operations
    operations = {"+", "*", "-", "/"}

    for token in tokens:
        if token in operations:
            #second operand (top of stack)
            b = stack.pop()
            #first operand
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                #truncate toward 0, not floor
                stack.append(int(a / b))
        else:
            #convert string to int and push onto stack
            stack.append(int(token))
    #final result is only element left
    return stack[0]
            
#Approach: I used a stack to process the token from left to right. I push numbers onto the stack, and when an operator is hit, I pop the two operands, apply the operation, 
#and then push the result. The final value left on the stack is the answer.
#Time complexity: The solution is O(n) where n is the number of tokens, since every token is visited exactly once and all stack operations (push/pop) are O(1).m
```

</details>

<details>
<summary>Original Document (69252.txt)</summary>

```
CS102 PAIRED TECHNICAL INTERVIEW

This is the template for what you are expected to submit for the CS102 PAIRED Technical Interview.
Please make sure you have your items in this order when you submit so the we can grade it easier🙏

Refer back to the Paired Technical Interview Print outs to the content you should submit.
In general, you should submit at least a number and some notes for the interviewer side, and your full code solution for the Candidate.

We encourage you to comment your code if you'd like!

Ashley Carozza

Clare Calandra

Interviewer Form

Longest Substring Without Repeating Characters

1) Problem Understanding: 4/4 - Clare took a couple minutes to fully digest the problem and work through it in her head. Once she was ready, she clarified with me the goal of the problem. She didn't need any additional information from me about the problem to get started or while coding!

2) Communication & Collaboration: 4/4 - Clare explained her code with a high level of intelligence. It was clear she knew what she was talking about and there seemed to be no gaps in her understanding. She responded well to feedback, too. She was able to answer every question I had and clarified it when needed.

3) Implementation & Technical Depth: 4/4 - Clare's code passed all the test cases on the doc and her code was well-commented as well. She was also able to explain and complete this problem with good time optimization. She obviously showed she knows how to apply hash sets.

4) Team Fit & Working Style: 4/4 - Clare would work great on a team based on how she performed during this interview. Even under pressure, she maintained her calmness and elegance. Even when she attempted a different approach to the problem and it wasn't optimized, she was able to reflect, go back, and revise. This is a highly valuable quality of any team member as reflection allows for progress. 

Final Evaluation: 16/16

Final Decision: I would hire Clare. Her ability to talk through her code and train of thought was incredible. Her words were articulate and I never felt lost. Her code was also optimized and obviously displayed a high level of understand a hash set. She had a good amount of confidence as well, but not cocky. Even though she had a different and less optimized approach at the start and needed a slight hint, she was able to recover successfully and ended up with some great code! She would make a great addition to the team, especially because of her can-do attitude. I would 100% hire her!

Candidate Form

def evalRPN(tokens: List[str]) -> int:
    #create empty stack
    stack = []
    #set of the operations
    operations = {"+", "*", "-", "/"}

    for token in tokens:
        if token in operations:
            #second operand (top of stack)
            b = stack.pop()
            #first operand
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                #truncate toward 0, not floor
                stack.append(int(a / b))
        else:
            #convert string to int and push onto stack
            stack.append(int(token))
    #final result is only element left
    return stack[0]
            
#Approach: I used a stack to process the token from left to right. I push numbers onto the stack, and when an operator is hit, I pop the two operands, apply the operation, 
#and then push the result. The final value left on the stack is the answer.
#Time complexity: The solution is O(n) where n is the number of tokens, since every token is visited exactly once and all stack operations (push/pop) are O(1).m
```

</details>

---

#### Ivan Cheung (`70932`)

- **Problem:** Evaluate Reverse Polish Notation
- **Language:** python
- **Score:** 7/7 (PASS)
- **Grading status:** graded
- **Files:** CS102 PAIRED TECHNICAL INTERVIEW.txt (direct)

| Test Case | Result |
|-----------|--------|
| example1 | PASS |
| example2 | PASS |
| example3 | PASS |
| add_only | PASS |
| single | PASS |
| subtract | PASS |
| neg_divide | PASS |

<details>
<summary>Extracted Code (70932.py)</summary>

```python
def evalRPN(tokens: List[str]) -> int:

    stack = []
    for e in tokens:
        
        if e == "+":
            stack.append(stack.pop() + stack.pop())
        
        elif e == "-":
            second = stack.pop()
            first = stack.pop()
            stack.append(first - second)

        elif e == "*":
            
            stack.append(stack.pop() * stack.pop())
        
        elif e == "/":
            second = stack.pop()
            first = stack.pop()
            stack.append(int(first / second))
        
        else:
            stack.append(int(e))
        
    return stack[0]
```

</details>

<details>
<summary>Original Document (70932.txt)</summary>

```
CS102 PAIRED TECHNICAL INTERVIEW

This is the template for what you are expected to submit for the CS102 PAIRED Technical Interview.
Please make sure you have your items in this order when you submit so the we can grade it easier🙏

Refer back to the Paired Technical Interview Print outs to the content you should submit.
In general, you should submit at least a number and some notes for the interviewer side, and your full code solution for the Candidate.

We encourage you to comment your code if you'd like!

Ivan Cheung

William Conroy

Interviewer Form

Length of Longest Substring

1) Problem Understanding
	4

2) Communication & Collaboration
	4

3) Implementation & Technical Depth
	4

4) Team Fit & Working Style
	4

Final Evaluation
	16

Final Decision
The candidate asked questions to fully understand the task. He was able to work calmly and explained his thought process. He did have trouble with some concepts but overall was knowledgeable about the task.

Candidate Form

def evalRPN(tokens: List[str]) -> int:

	stack = []
	for e in tokens:
		
		if e == "+":
			stack.append(stack.pop() + stack.pop())
		
		elif e == "-":
			second = stack.pop()
			first = stack.pop()
			stack.append(first - second)

		elif e == "*":
			
			stack.append(stack.pop() * stack.pop())
		
		elif e == "/":
			second = stack.pop()
			first = stack.pop()
			stack.append(int(first / second))
		
		else:
			stack.append(int(e))
		
	return stack[0]
```

</details>

---

#### Kyle Godzki (`67982`)

- **Problem:** Evaluate Reverse Polish Notation
- **Language:** python
- **Score:** 3/7 (Critical Error)
- **Grading status:** graded
- **Files:** PairedTechInterview.txt (direct)

| Test Case | Result |
|-----------|--------|
| example1 | PASS |
| example2 | FAIL |
| example3 | FAIL |
| add_only | PASS |
| single | PASS |
| subtract | FAIL |
| neg_divide | FAIL |

<details>
<summary>Edits made by grader</summary>

- [syntax-only] Extracted function block from noisy file

</details>

<details>
<summary>Extracted Code (67982.py)</summary>

```python
#Kyle Godzki
#Ethan Wong

# Stack -> LIFO


def evalRPN(tokens: List[str]) -> int:
        stack = []
        for token in tokens: O(N) # This is the for loop
                if token in '+-*/':
                        a, b = stack.pop(), stack.pop() #O(1) # Pops last two entries in stack
                        if token == '+': stack.append(a + b) # O(1) # Adds last two popped entries, answer entered
                        if token == '-': stack.append(a - b) 
                        if token == '*': stack.append(a * b)
                        if token == '/': stack.append(a / b)
                else:
                        stack.append(int(token))
        return stack[0] # return answer

Final complexity was O(N) since only one for loop and everything else just for loops. Space complexity was O((N/2) + 1) with our added stack.
```

</details>

<details>
<summary>Original Document (67982.txt)</summary>

```
#Kyle Godzki
#Ethan Wong

# Stack -> LIFO


def evalRPN(tokens: List[str]) -> int:
	stack = []
	for token in tokens: O(N) # This is the for loop
		if token in '+-*/':
			a, b = stack.pop(), stack.pop() #O(1) # Pops last two entries in stack
			if token == '+': stack.append(a + b) # O(1) # Adds last two popped entries, answer entered
			if token == '-': stack.append(a - b) 
 			if token == '*': stack.append(a * b)
			if token == '/': stack.append(a / b)
		else:
			stack.append(int(token))
	return stack[0] # return answer

Final complexity was O(N) since only one for loop and everything else just for loops. Space complexity was O((N/2) + 1) with our added stack.
```

</details>

---

#### Abdoul Razakou Mahaman Sani (`78738`)

- **Problem:** Evaluate Reverse Polish Notation
- **Language:** python
- **Score:** 5/7 (Minor Error)
- **Grading status:** graded
- **Files:** CS102 PAIRED TECHNICAL INTERVIEW.txt (direct)

| Test Case | Result |
|-----------|--------|
| example1 | PASS |
| example2 | PASS |
| example3 | FAIL |
| add_only | PASS |
| single | FAIL |
| subtract | PASS |
| neg_divide | PASS |

<details>
<summary>Extracted Code (78738.py)</summary>

```python
def evalRPN(tokens: List[str]):
    stack = []
    operator = ["+","-","*","/"]
    for i in tokens:
        if i not in operator:
            stack.append(i)
        else:
            val1 = int(stack.pop()) 
            val2 = int(stack.pop())
            if i == "/":
                result = val2//val1

            else:
                if i == "+":
                    result = val2+val1
                elif i == "-":
                    result = val2-val1
                elif i == "*":
                    result = val2*val1
            stack.append(result)
    return stack[0]
```

</details>

<details>
<summary>Original Document (78738.txt)</summary>

```
CS102 PAIRED TECHNICAL INTERVIEW

This is the template for what you are expected to submit for the CS102 PAIRED Technical Interview.
Please make sure you have your items in this order when you submit so the we can grade it easier🙏

Refer back to the Paired Technical Interview Print outs to the content you should submit.
In general, you should submit at least a number and some notes for the interviewer side, and your full code solution for the Candidate.

We encourage you to comment your code if you'd like!

Abdoul Sani

Treyson Thelusma

Interviewer Form

Longest Substring without repeating Characters

1) Problem Understanding
[4]

2) Communication & Collaboration
[3]

3) Implementation & Technical Depth
[4]

4) Team Fit & Working Style
[4]

Final Evaluation
[15/16]
Strong Hire
Final Decision
Showcase strong comprehension of the problem through explaining the problem to the interviewer. Communicated well and how strong reasoning skills. Would recommend for his completeness. 
Candidate Form

def evalRPN(tokens: List[str]):
	stack = []
	operator = ["+","-","*","/"]
	for i in tokens:
		if i not in operator:
			stack.append(i)
		else:
			val1 = int(stack.pop()) 
			val2 = int(stack.pop())
			if i == "/":
				result = val2//val1

			else:
				if i == "+":
					result = val2+val1
				elif i == "-":
					result = val2-val1
				elif i == "*":
					result = val2*val1
			stack.append(result)
	return stack[0]
```

</details>

---

#### Mahir Majlis (`79344`)

- **Problem:** Evaluate Reverse Polish Notation
- **Language:** python
- **Score:** 0/7 (Critical Error)
- **Grading status:** graded
- **Repair level:** aggressive
- **Files:** MAHIR MAJLIS- Interview Response.txt (direct)

| Test Case | Result |
|-----------|--------|
| example1 | FAIL |
| example2 | FAIL |
| example3 | FAIL |
| add_only | FAIL |
| single | FAIL |
| subtract | FAIL |
| neg_divide | FAIL |

<details>
<summary>Edits made by grader</summary>

- [logic-affecting] Replaced unparseable code with stub `def evalRPN(tokens): return 0`

</details>

<details>
<summary>Extracted Code (79344.py)</summary>

```python
The valid operators are '+', '-', '*', and '/'.
```

</details>

<details>
<summary>Original Document (79344.txt)</summary>

```
MAHIR MAJLIS 4/27/2026

INTERVIEWER FORM:

Interviewee : Naman Kukreti

Interviewer: ME

Problem Understanding : 3/4
Communication / Collaboration : 4/4
Implementation / Technical Depth : 2/4
Team Fit / Working Style : 3/4

Total: 12/16

Final Decision: Lean Hire 

Strengths: Explained their approach well, asked clarifying questions on edge cases and complexity that is desired

Weaknesses: Didn't implement intended binary search solution; possibly submitted equivalent (or at the very least, an acceptable) binary search solution

_________________________________________________________

CANDIDATE FORM:

Interviewee : ME 

Interviewer: Naman Kukreti


Evaluate Reverse Polish Notation — Candidate
Problem Information:
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation. Evaluate the expression and return an integer that represents the value of the expression. Note that:
The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
Constraints: 
1 <= tokens.length <= 104
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].

 Example 1:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

MY SOLUTION:

def evalRPN(tokens: List[str]) -> int:

	stack = []
	result = 0
	set_ops = {"+", "-", "/", "*"}
	for token in tokens:
		if token not in set_ops:
			stack.append(int(token)) //type casting
		else:
			b = stack.pop() //operands in correct position
			a = stack.pop()

			if token == "+":
				stack.append(a + b)
			elif token == "-":
				stack.append(a - b)
			elif token == "*":
				stack.append(a * b) 
			else:
				stack.append(a // b)
y

	return stack[0]

			
		
REFLECTION: 

On Paper


	

Hints:
```

</details>

---

#### Juan Moran (`79318`)

- **Problem:** Evaluate Reverse Polish Notation
- **Language:** python
- **Score:** 0/7 (Critical Error)
- **Grading status:** graded
- **Files:** 427 CS102 Mock-Interview.txt (direct)

| Test Case | Result |
|-----------|--------|
| example1 | FAIL |
| example2 | FAIL |
| example3 | FAIL |
| add_only | FAIL |
| single | FAIL |
| subtract | FAIL |
| neg_divide | FAIL |

<details>
<summary>Edits made by grader</summary>

- [syntax-only] Extracted function block from noisy file

</details>

<details>
<summary>Extracted Code (79318.py)</summary>

```python
arr = [4,13,5, / , +]
stack = [4,13,5]
term1 = 5 , stack [4,13]
term2 = 13, stack [4]
[4,2]
term1 = 2 , stack = [4]
term2 = 4, stack =[]
stack = [6]

def evalRPN(arr) :
        stack = []
        term1 = ""
        term2 = ""
        for i in range(len(arr)):
                if (len(arr) == 1):
                        return arr
                if arr[i].isDigit():
                        stack.push(arr[i])
                if arr[i] == "*":
                        term1 = stack[-1]
                        stack.pop()
                        term2 = stack[-1]
                        stack.pop()
                        term2 = int(term1)*int(term2)
                        stack.push(term2)
                if arr[i] == "/":
                        term1 = stack[-1]
                        stack.pop()
                        term2 = stack[-1]
                        stack.pop()
                        term2 = int(term2)/int(term1)
                        stack.push(term2)
                if arr[i] == "+":
                        term1 = stack[-1]
                        stack.pop()
                        term2 = stack[-1]
                        stack.pop()
                        term2 = int(term1)+int(term2)
                        stack.push(term2)
                if arr[i] == "-":
                        term1 = stack[-1]
                        stack.pop()
                        term2 = stack[-1]
                        stack.pop()
                        term2 = int(term2)-int(term1)
                        stack.push(term2)
        return stack[-1]
```

</details>

<details>
<summary>Original Document (79318.txt)</summary>

```
4/27 CS102 Mock-Interview

arr = [4,13,5, / , +]
stack = [4,13,5]
term1 = 5 , stack [4,13]
term2 = 13, stack [4]
[4,2]
term1 = 2 , stack = [4]
term2 = 4, stack =[]
stack = [6]

def evalRPN(arr) :
	stack = []
	term1 = ""
	term2 = ""
 	for i in range(len(arr)):
		if (len(arr) == 1):
			return arr
		if arr[i].isDigit():
			stack.push(arr[i])
		if arr[i] == "*":
			term1 = stack[-1]
			stack.pop()
			term2 = stack[-1]
			stack.pop()
			term2 = int(term1)*int(term2)
			stack.push(term2)
		if arr[i] == "/":
			term1 = stack[-1]
			stack.pop()
			term2 = stack[-1]
			stack.pop()
			term2 = int(term2)/int(term1)
			stack.push(term2)
		if arr[i] == "+":
			term1 = stack[-1]
			stack.pop()
			term2 = stack[-1]
			stack.pop()
			term2 = int(term1)+int(term2)
			stack.push(term2)
		if arr[i] == "-":
			term1 = stack[-1]
			stack.pop()
			term2 = stack[-1]
			stack.pop()
			term2 = int(term2)-int(term1)
			stack.push(term2)
	return stack[-1]
```

</details>

---

#### Gavin Ng (`79826`)

- **Problem:** Evaluate Reverse Polish Notation
- **Language:** python
- **Score:** 7/7 (PASS)
- **Grading status:** graded
- **Files:** IMG_4592.HEIC (image); IMG_4593.HEIC (image); IMG_4594.HEIC (image); IMG_4595.HEIC (image); interview.py (direct)

| Test Case | Result |
|-----------|--------|
| example1 | PASS |
| example2 | PASS |
| example3 | PASS |
| add_only | PASS |
| single | PASS |
| subtract | PASS |
| neg_divide | PASS |

<details>
<summary>Extracted Code (79826.py)</summary>

```python
#Gavin Ng
#Noel Maldaro 
#Evaluate Reverse Polish Notation
#Candidate Form


from typing import List 

def evalRPN(tokens: List[str]) -> int:
    sum = 0
    stack = []
 
    for i in range(len(tokens)):
        if tokens[i] == "+" or tokens[i] == "-" or tokens[i] == "*" or tokens[i] == "/": #checks if token is an operator
            num2 = stack.pop()#pops the 2 operands
            num1 = stack.pop()
            if tokens[i] == "+": 
                sum = num1 + num2
            elif tokens[i] == "-":
                sum = num1 - num2
            elif tokens[i] == "*":
                sum = num1 * num2
            else:
                sum = int(num1 / num2) #else divides already checked is operator
            stack.append(sum) #push the result back to stack
        else:
            stack.append(int(tokens[i])) #else pushes next token to stack as int

    return stack.pop() #last element would be final answer




print(evalRPN(["2", "1", "+", "3", "*"])) #sol: 9 
print(evalRPN(["4", "13", "5", "/", "+"])) #sol: 6
print(evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])) #sol: 22 (did math on paper)
```

</details>

<details>
<summary>Original Document (79826.txt)</summary>

```
#Gavin Ng
#Noel Maldaro 
#Evaluate Reverse Polish Notation
#Candidate Form


from typing import List 

def evalRPN(tokens: List[str]) -> int:
    sum = 0
    stack = []
 
    for i in range(len(tokens)):
        if tokens[i] == "+" or tokens[i] == "-" or tokens[i] == "*" or tokens[i] == "/": #checks if token is an operator
            num2 = stack.pop()#pops the 2 operands
            num1 = stack.pop()
            if tokens[i] == "+": 
                sum = num1 + num2
            elif tokens[i] == "-":
                sum = num1 - num2
            elif tokens[i] == "*":
                sum = num1 * num2
            else:
                sum = int(num1 / num2) #else divides already checked is operator
            stack.append(sum) #push the result back to stack
        else:
            stack.append(int(tokens[i])) #else pushes next token to stack as int

    return stack.pop() #last element would be final answer




print(evalRPN(["2", "1", "+", "3", "*"])) #sol: 9 
print(evalRPN(["4", "13", "5", "/", "+"])) #sol: 6
print(evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])) #sol: 22 (did math on paper)
```

</details>

---

#### Ved Patel (`69531`)

- **Problem:** Evaluate Reverse Polish Notation
- **Language:** python
- **Score:** 0/7 (Critical Error)
- **Grading status:** graded
- **Repair level:** aggressive
- **Files:** CS102 PAIRED TECHNICAL INTERVIEW copy.txt (direct)

| Test Case | Result |
|-----------|--------|
| example1 | FAIL |
| example2 | FAIL |
| example3 | FAIL |
| add_only | FAIL |
| single | FAIL |
| subtract | FAIL |
| neg_divide | FAIL |

<details>
<summary>Edits made by grader</summary>

- [syntax-only] Replaced || with or
- [syntax-only] Removed trailing semicolons
- [ambiguous] Conservative re-indent: normalized indent levels to 4-space tiers
- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def evalRPN(tokens): return 0`

</details>

<details>
<summary>Extracted Code (69531.py)</summary>

```python
def evalRPN(tokens: List[str] -> int): 
    # [4, 13, 5, /, +]

    # Time Complexity O(n)
    # Space Complexity O(n)

    #5
    #13 /  (2)
    #4 +  = 6 

    #13 / 5 = 2.5 = 2   


    #[result] 

    #result
    #result + 5 
    #result + 17
    #result * 10
    #result / 6
    #result * - 11
    #(3 + 9)

    #results = 0
    #l, r = 0, 1

    operations = {}

    if len(tokens) <= 2:
        return tokens[0]

    while(len(tokens) > 1):
        if tokens[r+1] != "*" || tokens[r+1] != "/" || tokens[r+1] != "+" :
            l++ 
            r++
            continue

        operations.append(tokens[l] + tokens[r+1] + tokens[r]);
        tokens.remove(r)
        tokens.remove(r+1)
        tokens[l] = "x"


    lr, rr, op = 0, 0 , 0
    results = 0
    for i in operations: 
        lr = operations[i][0]
        op = operations[i][1]
        rr = operations[i][2]

        if lr == "x":
            lr = results

        if op == "+":
            result = lr + rr    

        elif op == "*":
    
            result = lr * rr
        elif op == "/":
            result = lr // rr
    
    return results
```

</details>

<details>
<summary>Original Document (69531.txt)</summary>

```
CS102 PAIRED TECHNICAL INTERVIEW

This is the template for what you are expected to submit for the CS102 PAIRED Technical Interview.
Please make sure you have your items in this order when you submit so the we can grade it easier🙏

Refer back to the Paired Technical Interview Print outs to the content you should submit.
In general, you should submit at least a number and some notes for the interviewer side, and your full code solution for the Candidate.

We encourage you to comment your code if you'd like!

[Ved Patel]

[William Connors]

Interviewer Form

[Guess Number Higher or Lower]

1) Problem Understanding 2

2) Communication & Collaboration 3

3) Implementation & Technical Depth 2 

4) Team Fit & Working Style 2.5
	
Final Evaluation 10.5
	Did not ask enough questions at the beginning and got stuck in a hole
	kept on trying to use recursion
Final Decision
	Unfortunately, I will most likely not hire him due to not understanding the python concept but he was very good at asking questions regarding the code 

Candidate Form

def evalRPN(tokens: List[str] -> int): 
	# [4, 13, 5, /, +]

	# Time Complexity O(n)
	# Space Complexity O(n)

	#5
	#13 /  (2)
	#4 +  = 6 

	#13 / 5 = 2.5 = 2   


	#[result] 

	#result
	#result + 5 
	#result + 17
	#result * 10
	#result / 6
	#result * - 11
	#(3 + 9)

	#results = 0
	#l, r = 0, 1

	operations = {}

	if len(tokens) <= 2:
		return tokens[0]

	while(len(tokens) > 1):
		if tokens[r+1] != "*" || tokens[r+1] != "/" || tokens[r+1] != "+" :
			l++ 
			r++
			continue

		operations.append(tokens[l] + tokens[r+1] + tokens[r]);
		tokens.remove(r)
		tokens.remove(r+1)
		tokens[l] = "x"


	lr, rr, op = 0, 0 , 0
	results = 0
	for i in operations: 
		lr = operations[i][0]
		op = operations[i][1]
		rr = operations[i][2]

		if lr == "x":
			lr = results

		if op == "+":
			result = lr + rr	

		elif op == "*":
	
			result = lr * rr
		elif op == "/":
			result = lr // rr
	
	return results
```

</details>

---

#### Logan Regueiferos (`70953`)

- **Problem:** Evaluate Reverse Polish Notation
- **Language:** python
- **Score:** 6/7 (Minor Error)
- **Grading status:** graded
- **Files:** cs102.py (direct)

| Test Case | Result |
|-----------|--------|
| example1 | PASS |
| example2 | PASS |
| example3 | FAIL |
| add_only | PASS |
| single | PASS |
| subtract | PASS |
| neg_divide | PASS |

<details>
<summary>Extracted Code (70953.py)</summary>

```python
def reversepolishnotation ( tokens ):
    stack = []
    i = 0
    while (i < len(tokens)):
        if (tokens[i] == "+"):
            stack.append(stack.pop() + stack.pop())
        elif (tokens[i] == "-"):
            temp = 0
            temp = stack.pop()
            stack.append(stack.pop() - temp)
        elif (tokens[i] == "*"):
            stack.append(stack.pop() * stack.pop())
        elif (tokens[i] == "/"):
            temp = 0
            temp = stack.pop()
            stack.append(stack.pop() / temp)
        else:
            stack.append(float(tokens[i]))
        i+=1
    return stack[0]
print(reversepolishnotation(["1","2","3","/","+"]))
```

</details>

<details>
<summary>Original Document (70953.txt)</summary>

```
def reversepolishnotation ( tokens ):
	stack = []
	i = 0
	while (i < len(tokens)):
		if (tokens[i] == "+"):
			stack.append(stack.pop() + stack.pop())
		elif (tokens[i] == "-"):
			temp = 0
			temp = stack.pop()
			stack.append(stack.pop() - temp)
		elif (tokens[i] == "*"):
			stack.append(stack.pop() * stack.pop())
		elif (tokens[i] == "/"):
			temp = 0
			temp = stack.pop()
			stack.append(stack.pop() / temp)
		else:
			stack.append(float(tokens[i]))
		i+=1
	return stack[0]
print(reversepolishnotation(["1","2","3","/","+"]))
```

</details>

---

#### Naomi Sellam (`79751`)

- **Problem:** Evaluate Reverse Polish Notation
- **Language:** python
- **Score:** 7/7 (PASS)
- **Grading status:** graded
- **Files:** CS102 PAIRED TECHNICAL INTERVIEW.txt (direct)

| Test Case | Result |
|-----------|--------|
| example1 | PASS |
| example2 | PASS |
| example3 | PASS |
| add_only | PASS |
| single | PASS |
| subtract | PASS |
| neg_divide | PASS |

<details>
<summary>Extracted Code (79751.py)</summary>

```python
def evalRPN(tokens: List[str]) -> int:
    stack = []
    
    for token in tokens:
        if token in {'+', '-', '*', '/'}:
            
            b = stack.pop()  
            a = stack.pop()  
            
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))  
        else:
            stack.append(int(token))
    
    return stack[0]
```

</details>

<details>
<summary>Original Document (79751.txt)</summary>

```
CS102 PAIRED TECHNICAL INTERVIEW

This is the template for what you are expected to submit for the CS102 PAIRED Technical Interview.
Please make sure you have your items in this order when you submit so the we can grade it easier🙏

Refer back to the Paired Technical Interview Print outs to the content you should submit.
In general, you should submit at least a number and some notes for the interviewer side, and your full code solution for the Candidate.

We encourage you to comment your code if you'd like!

Naomi Sellam

Stephania Calin

Interviewer Form

Merge Two Sorted Lists

1) Problem Understanding
4 
She clearly understood the problem and confidently asked me questions about edge cases, exceptions, and constraints. She said there are already two sorted lists and understood that she needs to merge them into one sorted linked list, not by creating new nodes but by re-splicing the existing nodes together. She also asked about returning the new list or modifying it in place. 

2) Communication & Collaboration
3
She was very confident going into coding that she didn't fully explain her thought process before beginning to code, but she did get to it as she coded. She was able to recognize that she needs to use the two pointer technique where there would be one pointer per list and to advance the smaller one. She also recognized that there needs to be a dummy head node to avoid messy edge cases. 

3) Implementation & Technical Depth
4
Her solution was correct. She stated her approach was to create a dummy node as a starting anchor, keep a current pointer on the dummy, and while both lists have nodes, to compare each list and attach the smaller node to current.next. She explained more to her approach which demonstrated proficiency and understanding of the problem and she traced through example 1 quickly to verify how to return dummy.next. Her implementation ran through all test cases effectively and had good optimization.

4) Team Fit & Working Style
4
I would hire this person to my team because she was very communicative, nice, and good at the leetcode problem. She overall was a pleasure to interview and I think she would make a great addition to any team. 

Final Evaluation
Strong Hire

Final Decision

Candidate Form

[Insert Submitted Code]

def evalRPN(tokens: List[str]) -> int:
    stack = []
    
    for token in tokens:
        if token in {'+', '-', '*', '/'}:
            
            b = stack.pop()  
            a = stack.pop()  
            
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))  
        else:
            stack.append(int(token))
    
    return stack[0]
```

</details>

---

#### Jason Seng (`77220`)

- **Problem:** Evaluate Reverse Polish Notation
- **Language:** python
- **Score:** 1/7 (Critical Error)
- **Grading status:** graded
- **Files:** CS102 PAIRED TECHNICAL INTERVIEW JASON SENG2.0.txt (direct)

| Test Case | Result |
|-----------|--------|
| example1 | FAIL |
| example2 | FAIL |
| example3 | FAIL |
| add_only | FAIL |
| single | PASS |
| subtract | FAIL |
| neg_divide | FAIL |

<details>
<summary>Extracted Code (77220.py)</summary>

```python
def exalRPN(tokens: List[str]):
    arr=[]
    
    for i in tokens:
        if i == "+":
            arr.append(arr.pop() + arr.pop())
        elif i == "*":
            arr.append(arr.pop() * arr.pop())
        elif i == "/":
            second = arr.pop()
            first = arr.pop()
            arr.append(int(first / second))
        elif i == "-":
            second = arr.pop()
            first = arr.pop()
            arr.append(first - second)
        else:
            arr.append(int(i))
        return arr[0]
```

</details>

<details>
<summary>Original Document (77220.txt)</summary>

```
CS102 PAIRED TECHNICAL INTERVIEW

This is the template for what you are expected to submit for the CS102 PAIRED Technical Interview.
Please make sure you have your items in this order when you submit so the we can grade it easier🙏

Refer back to the Paired Technical Interview Print outs to the content you should submit.
In general, you should submit at least a number and some notes for the interviewer side, and your full code solution for the Candidate.

We encourage you to comment your code if you'd like!

Jason Seng

Santiago Zuluaga

Interviewer Form

Guess Number Higher or Lower

1) Problem Understanding (4)
-understood completely
-explained approach

2) Communication & Collaboration (3)
-asked for clarification when typing code
-adapted quickly to the feedback
-drew out his thought process

3) Implementation & Technical Depth (4)
-explained the complexities
-code works

4) Team Fit & Working Style(4)
-didn't complain
-remained calm 
-didn't stress out

Final Evaluation 15/16
Hire

Final Decision
He immediately explained his through process when hearing the problem and even drew it out. However, he got a little confused with the code which I helped clarify leading to the code working. I made my decision to hire him because he knew what he was doing and worked together with me when he was confused.

Candidate Form

def exalRPN(tokens: List[str]):
	arr=[]
	
	for i in tokens:
		if i == "+":
			arr.append(arr.pop() + arr.pop())
		elif i == "*":
			arr.append(arr.pop() * arr.pop())
		elif i == "/":
			second = arr.pop()
			first = arr.pop()
			arr.append(int(first / second))
		elif i == "-":
			second = arr.pop()
			first = arr.pop()
			arr.append(first - second)
		else:
			arr.append(int(i))
		return arr[0]


I check the tokens for the different operations and after seeing which one it is I pop the previous 2 numbers and use the operations with them. This goes for adding, subtracting, multiplying, and dividing. I make sure if its not an operation that I just append the integer itself.
```

</details>

---

#### Kushagra Singh (`75746`)

- **Problem:** Evaluate Reverse Polish Notation
- **Language:** python
- **Score:** 7/7 (PASS)
- **Grading status:** graded
- **Files:** CS102 PAIRED TECHNICAL INTERVIEW filled.txt (direct)

| Test Case | Result |
|-----------|--------|
| example1 | PASS |
| example2 | PASS |
| example3 | PASS |
| add_only | PASS |
| single | PASS |
| subtract | PASS |
| neg_divide | PASS |

<details>
<summary>Extracted Code (75746.py)</summary>

```python
from typing import List

def evalRPN(tokens: List[str]) -> int:
    stack = []
    ops = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: int(a / b)
    }
    
    for token in tokens:
        if token in ops:
            b, a = stack.pop(), stack.pop()
            stack.append(ops[token](a, b))
        else:
            stack.append(int(token))
    
    return stack[0]
```

</details>

<details>
<summary>Original Document (75746.txt)</summary>

```
CS102 PAIRED TECHNICAL INTERVIEW


Kushagra Singh

Varun Karamchandani

Interviewer Form

Merge two lists

1) Problem Understanding
Rating: 4
Candidate quickly identified the need to compare nodes iteratively and understood the linked list structure well. Asked a clarifying question about null/empty inputs which showed good awareness.
2) Communication & Collaboration
Rating: 4
Walked through their thought process clearly before jumping into code. Receptive to hints and explained their reasoning at each step. Good energy throughout.
3) Implementation & Technical Depth
Rating: 3
Got a working solution. Could have discussed time/space complexity more proactively — needed a prompt to bring it up. Mentioned the iterative vs recursive tradeoff which was a nice touch.
4) Team Fit & Working Style
Rating: 4
Stayed calm under pressure, asked good questions, and was collaborative. Would work well in a team setting.
Final Evaluation:
Strong candidate overall. Solid fundamentals and good communication. Minor gap in spontaneously analyzing complexity.
Final Decision: Hire

Candidate Form

Problem: Evaluate Reverse Polish Notation

from typing import List

def evalRPN(tokens: List[str]) -> int:
    stack = []
    ops = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: int(a / b)
    }
    
    for token in tokens:
        if token in ops:
            b, a = stack.pop(), stack.pop()
            stack.append(ops[token](a, b))
        else:
            stack.append(int(token))
    
    return stack[0]
```

</details>

---

#### Max Stehura (`80058`)

- **Problem:** Evaluate Reverse Polish Notation
- **Language:** python
- **Score:** 0/7 (Critical Error)
- **Grading status:** graded
- **Files:** CS102 PAIRED TECHNICAL INTERVIEW -.txt (direct)

| Test Case | Result |
|-----------|--------|
| example1 | FAIL |
| example2 | FAIL |
| example3 | FAIL |
| add_only | FAIL |
| single | FAIL |
| subtract | FAIL |
| neg_divide | FAIL |

<details>
<summary>Extracted Code (80058.py)</summary>

```python
def evalRPN(tokens: List[str]) -> int:
    stack = []
    for i in tokens:
        if i == "+":
            x1 = stack.pop()
            x2 = stack.pop()
            y = x1 + x2
            stack.append(y)
        elif i == "-":
            x1 = stack.pop()
            x2 = stack.pop()
            y = x2 - x1
            stack.append(y)
        elif i == "/":
            x1 = stack.pop()
            x2 = stack.pop()
            y = x2 / x1
            stack.append(y)
        elif i == "*":
            x1 = stack.pop()
            x2 = stack.pop()
            y = x1 * x2
            stack.append(y)
        else:
            stack.append(i)
    return stack.pop()
```

</details>

<details>
<summary>Original Document (80058.txt)</summary>

```
CS102 PAIRED TECHNICAL INTERVIEW - Max Stehura

Max Stehura

Ryan Martin

Interviewer Form

Longest Substring Without Repeating Characters

1) Problem Understanding - 4/4

Candidate reread the question, understood the example cases, and overall what the question was asking for. 


2) Communication & Collaboration - 4/4

Candidate wrote pseudocode prior to implementing code, making note of what variables must be initialized and structure of the algorithm. Questions were asked to clarify constraints and how to properly keep track of the sub-string during the while loop and max sub-string.

3) Implementation and Technical Depth - 4/4

Solution perfectly followed what was necessary with only one or no errors made, and mentioned the time and space complexity, time being O(n) and space being O(n) considering the inclusion of a hashset and the associated operations being O(1) to add them or remove elements. They also walked through the already given test cases using their own algorithm, drawing out what would happen from each line.

4) Team Fit and Working Style - 4/4

I would definitely want this person on my team based on their performance, for they were able to quickly and efficiently identify and begin mapping out their solution within a few minutes, and at no point did they express any undesirable responses.

Final Evaluation: 16/16

Final Decision: 

Key strengths included good knowledge of python syntax, ability to correctly identify relevant data structures and how to apply them in the problem. Key weaknesses may be few errors in syntax but overall knows the fundamental concepts to solve the problems. I made my decision to recommend them as a strong hire due to their proficient and satisfactory technical skills and communication abilities.

Candidate Form

Evaluate Reverse Polish Notation

def evalRPN(tokens: List[str]) -> int:
	stack = []
	for i in tokens:
		if i == "+":
			x1 = stack.pop()
			x2 = stack.pop()
			y = x1 + x2
			stack.append(y)
		elif i == "-":
			x1 = stack.pop()
			x2 = stack.pop()
			y = x2 - x1
			stack.append(y)
		elif i == "/":
			x1 = stack.pop()
			x2 = stack.pop()
			y = x2 / x1
			stack.append(y)
		elif i == "*":
			x1 = stack.pop()
			x2 = stack.pop()
			y = x1 * x2
			stack.append(y)
		else:
			stack.append(i)
	return stack.pop()
```

</details>

---

#### Giankyle Vallarta (`70939`)

- **Problem:** Evaluate Reverse Polish Notation
- **Language:** java
- **Score:** 0/7 (Critical Error)
- **Grading status:** graded
- **Repair level:** aggressive
- **Files:** Mock Technical Interview - Giankyle Vallarta.pdf (pdf)

| Test Case | Result |
|-----------|--------|
| example1 | FAIL |
| example2 | FAIL |
| example3 | FAIL |
| add_only | FAIL |
| single | FAIL |
| subtract | FAIL |
| neg_divide | FAIL |

<details>
<summary>Edits made by grader</summary>

- [syntax-only] Mechanical Java->Python transpile
- [syntax-only] Added missing colons
- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def evalRPN(tokens): return 0`

</details>

<details>
<summary>Extracted Code (70939.java)</summary>

```java
evalRPN(String[]
 
tokens)
 
{
 
 
stack<Integers>
 
token2
 
=
 
new
 
Stack<>();
 
 
 
 
for
 
(String
 
x
 
:
 
tokens)
 
{
 
 
 
if
 
(x.equals("+"))
 
{
  
 
 
token2.push(token2.pop()
 
+
 
token2.pop());
 
 
 
}
 
 
else
 
if
 
(x.equals("-"))
 
{
 
 
 
 
int
 
two
 
=
 
token2.pop();
 
 
 
 
 
int
 
one
 
=
 
token2.pop();
 
 
 
 
token2.push(one
 
-
 
two);
 
 
 
}
 
 
else
 
if
 
(x.equals("*"))
 
{
 
 
 
 
token2.push(token2.pop()
 
*
 
token2.pop());
 
 
 
}
 
 
else
 
if
 
(x.equals("/"))
 
{
 
 
 
 
int
 
two
 
=
 
token2.pop();
 
 
 
 
int
 
one
 
=
 
token2.pop();
 
 
 
 
token2.push(one/two);
 
 
}
 
}
 
 
 
return
 
token2.peek();
 
 
}
```

</details>

<details>
<summary>Original Document (70939.txt)</summary>

```
CS102
 
PAIRED
 
TECHNICAL
 
INTER VIEW
 
 
This
 
is
 
the
 
template
 
for
 
what
 
you
 
are
 
expected
 
to
 
submit
 
for
 
the
 
CS102
 
PAIRED
 
Technical
 
Interview .
 
Please
 
make
 
sure
 
you
 
have
 
your
 
items
 
in
 
this
 
order
 
when
 
you
 
submit
 
so
 
the
 
we
 
can
 
grade
 
it
 
easier
🙏
 
 
Refer
 
back
 
to
 
the
 
Paired
 
Technical
 
Interview
 
Print
 
outs
 
to
 
the
 
content
 
you
 
should
 
submit.
 
In
 
general,
 
you
 
should
 
submit
 
at
 
least
 
a
 
number
 
and
 
some
 
notes
 
for
 
the
 
interviewer
 
side,
 
and
 
your
 
full
 
code
 
solution
 
for
 
the
 
Candidate.
 
 
We
 
encourage
 
you
 
to
 
comment
 
your
 
code
 
if
 
you'd
 
like!
 
 
[Giankyle
 
Vallarta]
 
 
[Monica
 
Gnajewski]
 
 
Interviewer
 
Form
 
 
[Evaluate
 
Reverse
 
Polish
 
Notation]
 
→
 
I
 
gave
 
it
 
via
 
written
 
paper .
 
 
1)
 
Problem
 
Understanding
 
 
2)
 
Communication
 
&
 
Collaboration
 
 
3)
 
Implementation
 
&
 
Technical
 
Depth
 
 
4)
 
Team
 
Fit
 
&
 
Working
 
Style
 
 
Final
 
Evaluation
 
 
Final
 
Decision
 
 
Candidate
 
Form
 
 
public
 
int
 
evalRPN(String[]
 
tokens)
 
{
 
 
stack<Integers>
 
token2
 
=
 
new
 
Stack<>();
 
 
 
 
for
 
(String
 
x
 
:
 
tokens)
 
{
 
 
 
if
 
(x.equals("+"))
 
{
  
 
 
token2.push(token2.pop()
 
+
 
token2.pop());
 
 
 
}
 
 
else
 
if
 
(x.equals("-"))
 
{
 
 
 
 
int
 
two
 
=
 
token2.pop();
 
 
 
 
 
int
 
one
 
=
 
token2.pop();
 
 
 
 
token2.push(one
 
-
 
two);
 
 
 
}
 
 
else
 
if
 
(x.equals("*"))
 
{
 
 
 
 
token2.push(token2.pop()
 
*
 
token2.pop());
 
 
 
}
 
 
else
 
if
 
(x.equals("/"))
 
{
 
 
 
 
int
 
two
 
=
 
token2.pop();
 
 
 
 
int
 
one
 
=
 
token2.pop();
 
 
 
 
token2.push(one/two);
 
 
}
 
}
 
 
 
return
 
token2.peek();
 
 
}
```

</details>

---

#### Kartik Wahlin (`75620`)

- **Problem:** Evaluate Reverse Polish Notation
- **Language:** python
- **Score:** 3/7 (Critical Error)
- **Grading status:** graded
- **Files:** cs102 quiz kartikwahlin.txt (direct)

| Test Case | Result |
|-----------|--------|
| example1 | PASS |
| example2 | FAIL |
| example3 | FAIL |
| add_only | PASS |
| single | PASS |
| subtract | FAIL |
| neg_divide | FAIL |

<details>
<summary>Edits made by grader</summary>

- [syntax-only] Lowered keyword 'Return'

</details>

<details>
<summary>Extracted Code (75620.py)</summary>

```python
def evalRPN(tokens: List[str]) -> int:
    tack = []
    num1 = 0 
    num2 = 0
    for bench in tokens:
        if bench == “+”:
            num1 = tack.pop()
            num2 = tack.pop()
            tack. append(num1+num2)
        elif bench == “-”:
            num1 = tack.pop()
            num2 = tack.pop()
            tack. append(num1-num2)
        elif bench == “/”:
            num1 = tack.pop()
            num2 = tack.pop()
            tack. append(num1/num2)
        elif bench == “*”:
            num1 = tack.pop()
            num2 = tack.pop()
            tack.append(num1*num2)
        else:
            tack.append(int(bench)) #if the element is not an operator, it can be cast to an int.
    return tack.pop()
#explanation on paper.
#Stack of encountered numbers - String array
#When we hit an operator, we condense the last 2 numbers into their result and add it back into the stack.
#repeat until end of array, where stack size = 1. Return int value.

#Edge cases are safe: min size is 1 and a valid arithmetic operation is guaranteed
```

</details>

<details>
<summary>Original Document (75620.txt)</summary>

```
Kartik Wahlin
Shunyi Chen

Interviewer Form

[Problem Given] (Just the Name of the Problem is fine)

1) Problem Understanding : 4/4
Asks confirming questions and runs through time complexities for patterns before finding the best pattern
2) Communication & Collaboration: 4/4
Clearly indicated his thought process. Worked with feedback and checked in with interviewer when coming up with ideas.
3) Implementation & Technical Depth 4/4 
After careful thought, solution implements correct patterns for an O(n) time. Code doesn’t contain any excess
4) Team Fit & Working Style 4/4
Open to feedback and willing to adapt when ideas didn’t work out. Kept a constructive mindset.
Final Evaluation
16/16
Strong Hire
Final Decision
Candidate held a growth mindset and kept adapting to learn from mistakes. He was open to feedback and knew about the correct algorithm after considering others. 
One weakness was that he was unfamiliar with python, and initially went for an inconvenient data structure instead of going straight for a hash set.
I decided he was a strong hire because he was able to learn quickly and displayed the necessary technical knowledge. He had a strong understanding of the problem by the end and I could follow his thought process.
Candidate Form:
Evaluate Reverse Polish Notation:

def evalRPN(tokens: List[str]) -> int:
	tack = []
	num1 = 0 
	num2 = 0
	for bench in tokens:
		if bench == “+”:
			num1 = tack.pop()
			num2 = tack.pop()
			tack. append(num1+num2)
		elif bench == “-”:
			num1 = tack.pop()
			num2 = tack.pop()
			tack. append(num1-num2)
		elif bench == “/”:
			num1 = tack.pop()
			num2 = tack.pop()
			tack. append(num1/num2)
		elif bench == “*”:
			num1 = tack.pop()
			num2 = tack.pop()
			tack.append(num1*num2)
		else:
			tack.append(int(bench)) #if the element is not an operator, it can be cast to an int.
	return tack.pop()
#explanation on paper.
#Stack of encountered numbers - String array
#When we hit an operator, we condense the last 2 numbers into their result and add it back into the stack.
#repeat until end of array, where stack size = 1. Return int value.

#Edge cases are safe: min size is 1 and a valid arithmetic operation is guaranteed
```

</details>

---

### Guess Number Higher or Lower

#### Gaven Chan (`69954`)

- **Problem:** Guess Number Higher or Lower
- **Language:** python
- **Score:** 0/7 (Critical Error)
- **Grading status:** graded
- **Files:** CS102 PAIRED TECHNICAL INTERVIEW.txt (direct)

| Test Case | Result |
|-----------|--------|
| basic | FAIL |
| single | FAIL |
| pick_low | FAIL |
| pick_high | FAIL |
| large | FAIL |
| mid_range | FAIL |
| pick_is_n | FAIL |

<details>
<summary>Extracted Code (69954.py)</summary>

```python
#-1 if its higher
#1 if its lower
#0 if equal 

#constraints x >= 1 
#guess() = some_number
#n is the upper limit 
#1, 2, 3, 4 ... n 
#n/2

def guessingGame(int n):
    lower = 1
    upper = n
    
    while(guess() != 0):
        middle = (upper + lower)/2
        if guess(middle) == 0:
            return middle
        
        if guess(middle) == -1:
            upper =  middle - 1
            
        if guess(middle) == 1:
            lower = middle + 1
```

</details>

<details>
<summary>Original Document (69954.txt)</summary>

```
CS102 PAIRED TECHNICAL INTERVIEW

This is the template for what you are expected to submit for the CS102 PAIRED Technical Interview.
Please make sure you have your items in this order when you submit so the we can grade it easier🙏

Refer back to the Paired Technical Interview Print outs to the content you should submit. The interviewer form & candidate reflection should be submitted on paper. The candidate code should be submitted with the format below:

We encourage you to comment your code if you'd like!
[Your name]
Gaven Chan

[Your partner's name]
Jiarong Zhang

Candidate Form

[Insert Submitted Code]
#-1 if its higher
#1 if its lower
#0 if equal 

#constraints x >= 1 
#guess() = some_number
#n is the upper limit 
#1, 2, 3, 4 ... n 
#n/2

def guessingGame(int n):
	lower = 1
	upper = n
	
	while(guess() != 0):
		middle = (upper + lower)/2
		if guess(middle) == 0:
			return middle
		
		if guess(middle) == -1:
			upper =  middle - 1
			
		if guess(middle) == 1:
			lower = middle + 1
```

</details>

---

#### Albert Chen (`78939`)

- **Problem:** Guess Number Higher or Lower
- **Language:** python
- **Score:** 7/7 (PASS)
- **Grading status:** graded
- **Files:** cs102mockInterview.py (direct)

| Test Case | Result |
|-----------|--------|
| basic | PASS |
| single | PASS |
| pick_low | PASS |
| pick_high | PASS |
| large | PASS |
| mid_range | PASS |
| pick_is_n | PASS |

<details>
<summary>Extracted Code (78939.py)</summary>

```python
def guess (n:int) ->int:
    if (n==1):
        return 1
    left =1
    right = n
    middlePointer = (left+right)//2
    while (guess(middlePointer) !=0 and left<=right):
        if (guess(middlePointer) ==-1): #if our guess is too high we move the right pointer
            right = middlePointer -1
        if (guess(middlePointer) == 1): #if our guess is too high we move the left pointer
            left = middlePointer +1
        middlePointer = (left+right)//2
    return middlePointer
    
    
    #1,2 pick=2
#    left =2
#    right = 2
    #middlePointer = 2
```

</details>

<details>
<summary>Original Document (78939.txt)</summary>

```
def guess (n:int) ->int:
	if (n==1):
		return 1
	left =1
	right = n
	middlePointer = (left+right)//2
	while (guess(middlePointer) !=0 and left<=right):
		if (guess(middlePointer) ==-1): #if our guess is too high we move the right pointer
			right = middlePointer -1
		if (guess(middlePointer) == 1): #if our guess is too high we move the left pointer
			left = middlePointer +1
		middlePointer = (left+right)//2
	return middlePointer
	
	
	#1,2 pick=2
#	left =2
#	right = 2
	#middlePointer = 2
```

</details>

---

#### William Connors (`78627`)

- **Problem:** Guess Number Higher or Lower
- **Language:** python
- **Score:** 0/7 (Critical Error)
- **Grading status:** graded
- **Repair level:** aggressive
- **Files:** Technical Interview Submission.docx (docx)

| Test Case | Result |
|-----------|--------|
| basic | FAIL |
| single | FAIL |
| pick_low | FAIL |
| pick_high | FAIL |
| large | FAIL |
| mid_range | FAIL |
| pick_is_n | FAIL |

<details>
<summary>Edits made by grader</summary>

- [ambiguous] Conservative re-indent: normalized indent levels to 4-space tiers
- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def guessNumber(n): return 0`

</details>

<details>
<summary>Extracted Code (78627.py)</summary>

```python
def guessNumber (n: int) -> int:
        l, r = 0, n

        int guess (5)

        while l <= r:
                    mid = (1 + r) // 2
                    if nums [mid] == target:
                        return mid
                    elif nums [mid] < target:
                                l = mid + 1
                    else:
                            r = mid - 1

        return -1
```

</details>

<details>
<summary>Original Document (78627.txt)</summary>

```
CS102 PAIRED TECHNICAL INTERVIEW

This is the template for what you are expected to submit for the CS102 PAIRED Technical Interview.
Please make sure you have your items in this order when you submit so the we can grade it easier🙏

Refer back to the Paired Technical Interview Print outs to the content you should submit.
In general, you should submit at least a number and some notes for the interviewer side, and your full code solution for the Candidate.

We encourage you to comment your code if you'd like!

[William Connors]

[Ved Petel]

Interviewer Form

[Revers Polish Notation]

1) Problem Understanding
4

2) Communication & Collaboration
3

3) Implementation & Technical Depth
3

4) Team Fit & Working Style
3

Final Evaluation
13/16

Final Decision
Lean Hire

Candidate Form

Technical Interview

def guessNumber (n: int) -> int:
l, r = 0, n

int guess (5)

while l <= r:
      mid = (1 + r) // 2
      if nums [mid] == target:
         return mid
      elif nums [mid] < target:
           l = mid + 1
      else:
          r = mid - 1
   
return -1
```

</details>

---

#### Lilia Diusheyeva (`73721`)

- **Problem:** Guess Number Higher or Lower
- **Language:** python
- **Score:** 7/7 (PASS)
- **Grading status:** graded
- **Files:** CS102 PAIRED TECHNICAL INTERVIEW.txt (direct)

| Test Case | Result |
|-----------|--------|
| basic | PASS |
| single | PASS |
| pick_low | PASS |
| pick_high | PASS |
| large | PASS |
| mid_range | PASS |
| pick_is_n | PASS |

<details>
<summary>Edits made by grader</summary>

- [syntax-only] Fixed --> to ->
- [syntax-only] Extracted function block from noisy file

</details>

<details>
<summary>Extracted Code (73721.py)</summary>

```python
4: Fully understood, restated clearly

    Re-explained problem back to ensure all constraints were understood.
    Talked about the examples and how the output would reach that result.


2) Communication & Collaboration
    4: Very clear, structured, highly collaborative and adaptive

    Asked questions to clarify and explained why the sliding window approach was optimal for this problem.
    Asked for hints but starting thinking out loud how each hint led to the way to solution.


3) Implementation & Technical Depth
    2: Partially correct solution, basic or incomplete analysis
    
    Computed code and explained how time complexity resulted as O(n) by ensuring there were no duplicates however, multiple syntax errors found. Also, explained the use of two-pointer and how it would be implemented within the problem but did not fully implement correctly.


4) Team Fit & Working Style
    3: Positive teammate; receptive, steady, easy to work with

    Calm under questioning, good at communicating their thoughts, can be strong asset but a bit uncertain and lacks confidence. Could be more assertive about his ideas and points.


Final Evaluation
    13/16 Hire


Final Decision
    Reginald would be a good candidate for hire as he displayed a good amount of communication and was fully emersed into the problem through his questions and implementation of code. I believe he works well and fast under uncertainty. Despite, being a bit unsure of himself in the beginning, Reginald shows hard work and perseverance through his thinking and problem solving. Even with minor errors, I believe Reginald could do well within a team. 


Candidate Form: Guess Number Higher or Lower 

O log(n) 

def guessNumber(n: int) --> int:
    #initizalize the start and end of the range in guess
    start = 1
    end  = n

    #create while loop to search through while the guesses are valid
    while (start <= end):
        middle = start + (end - start) //2 #get the middle to avoid overflow

        #create statements for the various results
        if guess(middle) == 0:
            return middle #if guess equals 0 then it is the correct guess

        elif guess(middle) ==1:
            start = middle + 1 #guess is too low

        else: 
            end = middle - 1 #guess is too high

    return 0 #in case of fallback
```

</details>

<details>
<summary>Original Document (73721.txt)</summary>

```
CS102 PAIRED TECHNICAL INTERVIEW

Lilia Diusheyeva

Reginald Juance

Interviewer Form

Longest Substring Without Repeating Characters

1) Problem Understanding
	4: Fully understood, restated clearly

	Re-explained problem back to ensure all constraints were understood.
	Talked about the examples and how the output would reach that result.


2) Communication & Collaboration
	4: Very clear, structured, highly collaborative and adaptive

	Asked questions to clarify and explained why the sliding window approach was optimal for this problem.
	Asked for hints but starting thinking out loud how each hint led to the way to solution.


3) Implementation & Technical Depth
	2: Partially correct solution, basic or incomplete analysis
	
	Computed code and explained how time complexity resulted as O(n) by ensuring there were no duplicates however, multiple syntax errors found. Also, explained the use of two-pointer and how it would be implemented within the problem but did not fully implement correctly.


4) Team Fit & Working Style
	3: Positive teammate; receptive, steady, easy to work with

	Calm under questioning, good at communicating their thoughts, can be strong asset but a bit uncertain and lacks confidence. Could be more assertive about his ideas and points.


Final Evaluation
	13/16 Hire


Final Decision
	Reginald would be a good candidate for hire as he displayed a good amount of communication and was fully emersed into the problem through his questions and implementation of code. I believe he works well and fast under uncertainty. Despite, being a bit unsure of himself in the beginning, Reginald shows hard work and perseverance through his thinking and problem solving. Even with minor errors, I believe Reginald could do well within a team. 


Candidate Form: Guess Number Higher or Lower 

O log(n) 

def guessNumber(n: int) --> int:
	#initizalize the start and end of the range in guess
	start = 1
	end  = n

	#create while loop to search through while the guesses are valid
	while (start <= end):
		middle = start + (end - start) //2 #get the middle to avoid overflow

		#create statements for the various results
		if guess(middle) == 0:
			return middle #if guess equals 0 then it is the correct guess

		elif guess(middle) ==1:
			start = middle + 1 #guess is too low

		else: 
			end = middle - 1 #guess is too high

	return 0 #in case of fallback
```

</details>

---

#### Reginald Juance (`68931`)

- **Problem:** Guess Number Higher or Lower
- **Language:** python
- **Score:** 0/7 (Critical Error)
- **Grading status:** graded
- **Repair level:** aggressive
- **Files:** CS102 PAIRED TECHNICAL INTERVIEW.pdf (pdf)

| Test Case | Result |
|-----------|--------|
| basic | FAIL |
| single | FAIL |
| pick_low | FAIL |
| pick_high | FAIL |
| large | FAIL |
| mid_range | FAIL |
| pick_is_n | FAIL |

<details>
<summary>Edits made by grader</summary>

- [syntax-only] Fixed --> to ->
- [syntax-only] Lowered keyword 'While'
- [syntax-only] Fixed typo -> 'True'
- [logic-affecting] Replaced unparseable code with stub `def guessNumber(n): return 0`

</details>

<details>
<summary>Extracted Code (68931.py)</summary>

```python
🙏Refer back to the Paired Technical Interview Print outs to the content you should submit.In general, you should submit at least a number and some notes for the interviewer side, and your full code solution for the Candidate.We encourage you to comment your code if you'd like!Reginald JuanceLilia DiusheveyaInterviewer Form[Problem Given] Guess Number Higher or Lower1) Problem Understanding: 4/4- Lilia understands the problem to a binary search immediately off of the bat- Ordered based on equal, greater than, or lower than- Understands all the constraints given to her (size restrictions)2) Communication & Collaboration: 2/4- While she explained some things throughout the problem, like her thought process and reasoning behind Binary Search, she failed to engage with interviewer clearly- At moments, she struggled to keep eye contact and social connections- Too focused on coding, forgot to explain her entire thought process through the UMPIRE method3) Implementation & Technical Depth: 4/4- Time complexity is O(log n) --> natural to binary search- Implementation is true and correct- Updates range effectively based on guesses4) Team Fit & Working Style: 3/4- Lilia is a positive personality when going through the interview process- She is incredibly receptive to hints, and is easy to work with- She will undoubtedly work well in any conditions that she facesFinal Evaluation- Score: 13/16- Hiring Recommendation: Lean HireFinal Decision- While Lilia is completely capable in implementing the question successfully, she falls short in the team aspect a hiring manager is looking for.She needs to learn to effectively communicate her thoughts when going through the interview process, or else this could raise concerns. However,throughout the interview, she was a positive person when acting under pressure and took into account any comments made. Her implementation was logically soundand ensured a complexity of O(log n)Candidate FormCode in Python:# Two pointer/sliding window problem for left pointer & hash set to prevent duplicates, ensures O(n) time complexity# Sliding window to optimize time complexity O(n)def lengthOfLongestSubstring(s: str) -> int: left = 0 # left pointer to start window max_length =  # maximum substring length, initialize it as 0 & update accordingly char_set = set() # ensures that string follows criteria regarding valid strings, and keeps track of unique/non-duplicate characters  for right in range(len(s): # right pointer for pointer   while s[right] in char_set: # remove invalid characters or duplicates   char_set.remove(s[left])   left = left + 1 # move left pointer over to slide   char_set.add(s[right]) # add the current char to the given set  max_length = max(max_length, right - left + 1) # new answer, accounting for current length  return max_length
```

</details>

<details>
<summary>Original Document (68931.txt)</summary>

```
CS102 PAIRED TECHNICAL INTERVIEWThis is the template for what you are expected to submit for the CS102 PAIRED Technical Interview.Please make sure you have your items in this order when you submit so the we can grade it easier
🙏Refer back to the Paired Technical Interview Print outs to the content you should submit.In general, you should submit at least a number and some notes for the interviewer side, and your full code solution for the Candidate.We encourage you to comment your code if you'd like!Reginald JuanceLilia DiusheveyaInterviewer Form[Problem Given] Guess Number Higher or Lower1) Problem Understanding: 4/4- Lilia understands the problem to a binary search immediately off of the bat- Ordered based on equal, greater than, or lower than- Understands all the constraints given to her (size restrictions)2) Communication & Collaboration: 2/4- While she explained some things throughout the problem, like her thought process and reasoning behind Binary Search, she failed to engage with interviewer clearly- At moments, she struggled to keep eye contact and social connections- Too focused on coding, forgot to explain her entire thought process through the UMPIRE method3) Implementation & Technical Depth: 4/4- Time complexity is O(log n) --> natural to binary search- Implementation is true and correct- Updates range effectively based on guesses4) Team Fit & Working Style: 3/4- Lilia is a positive personality when going through the interview process- She is incredibly receptive to hints, and is easy to work with- She will undoubtedly work well in any conditions that she facesFinal Evaluation- Score: 13/16- Hiring Recommendation: Lean HireFinal Decision- While Lilia is completely capable in implementing the question successfully, she falls short in the team aspect a hiring manager is looking for.She needs to learn to effectively communicate her thoughts when going through the interview process, or else this could raise concerns. However,throughout the interview, she was a positive person when acting under pressure and took into account any comments made. Her implementation was logically soundand ensured a complexity of O(log n)Candidate FormCode in Python:# Two pointer/sliding window problem for left pointer & hash set to prevent duplicates, ensures O(n) time complexity# Sliding window to optimize time complexity O(n)def lengthOfLongestSubstring(s: str) -> int: left = 0 # left pointer to start window max_length =  # maximum substring length, initialize it as 0 & update accordingly char_set = set() # ensures that string follows criteria regarding valid strings, and keeps track of unique/non-duplicate characters  for right in range(len(s): # right pointer for pointer   while s[right] in char_set: # remove invalid characters or duplicates   char_set.remove(s[left])   left = left + 1 # move left pointer over to slide   char_set.add(s[right]) # add the current char to the given set  max_length = max(max_length, right - left + 1) # new answer, accounting for current length  return max_length
```

</details>

---

#### Naman Kukreti (`75854`)

- **Problem:** Guess Number Higher or Lower
- **Language:** python
- **Score:** 7/7 (PASS)
- **Grading status:** graded
- **Files:** NamanKquiz3.txt (direct)

| Test Case | Result |
|-----------|--------|
| basic | PASS |
| single | PASS |
| pick_low | PASS |
| pick_high | PASS |
| large | PASS |
| mid_range | PASS |
| pick_is_n | PASS |

<details>
<summary>Extracted Code (75854.py)</summary>

```python
def guessnumber(num):
    #because pick is guarenteed to be in range, there's no need to check out of range/return -1 or not found
    L = 1
    R = num
    mid = (R+L)//2
    while(guess(mid) != 0):
        mid = (R+L)//2
        if(guess(mid) == -1):
            R = mid-1
        elif(guess(mid) == 1):
            L = mid + 1
    return mid
```

</details>

<details>
<summary>Original Document (75854.txt)</summary>

```
"""
Naman Kukreti

Mahir Majlis

Interviewer Form

[Problem Given] Evaluate Reverse Polish Notation

1) Problem Understanding
 4
Was a "difficult" question, but interviewee broke it down while reading it, suggested stack implentation and knew what time complexity it should be solved in.
2) Communication & Collaboration
3
Only negative was him rereading what I read, talked through the logic he wrote, and was silent at times.
3) Implementation & Technical Depth
Well done, some uneccessary code like a set and temp variables, but those didn'tadd to space or time complexity and improved readability.
4) Team Fit & Working Style
Was a confusing problem, kept talking through it while breaking it down and explaining logic of code while explaining. Didn't panic or go silent for too long.
Final Evaluation
On paper
Final Decision
On paper
Candidate Form
On paper
[Insert Submitted Code]
"""
"""
Candidate Naman Kukreti
Guess Number Higher or Lower — Candidate
Problem Information:  We are playing the Guess Game. The game is as follows:
I pick a number from 1 to n. You have to guess which number I picked (the number I picked stays the same throughout the game). Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked. Constraints: 1 <= n <= 231 - 1,  1 <= pick <= n

Example 1:

Input: n = 10, pick = 6
Output: 6
Example 2:

Input: n = 1, pick = 1
Output: 1
Example 3:

Input: n = 2, pick = 1
Output: 1
U
input:
integer n
output:
the number you picked
constraint:

edgecase:

Match:binary search

Plan:
while guess = 0
	binary search iteration
return mid
Implement:
def guessnumber(num):
        L = 1
        R = num
        mid = (R+L)//2
        while(guess(mid) != 0):
                mid = (R+L)//2
                if(guess(mid) == -1):
                        R = mid-1
                elif(guess(mid) == 1):
                        L = mid + 1
        return mid
Review:
Works on test cases
Evaluate:
O(log(n))
"""

def guessnumber(num):
	#because pick is guarenteed to be in range, there's no need to check out of range/return -1 or not found
	L = 1
	R = num
	mid = (R+L)//2
	while(guess(mid) != 0):
		mid = (R+L)//2
		if(guess(mid) == -1):
			R = mid-1
		elif(guess(mid) == 1):
			L = mid + 1
	return mid
```

</details>

---

#### Matthew Park (`75927`)

- **Problem:** Guess Number Higher or Lower
- **Language:** python
- **Score:** 7/7 (PASS)
- **Grading status:** graded
- **Files:** interview.txt (direct)

| Test Case | Result |
|-----------|--------|
| basic | PASS |
| single | PASS |
| pick_low | PASS |
| pick_high | PASS |
| large | PASS |
| mid_range | PASS |
| pick_is_n | PASS |

<details>
<summary>Extracted Code (75927.py)</summary>

```python
#n is the highest possible number
#return the number that I picked
def guessNumber(n: int) -> int:
    low = 1
    high = n
    
    #loop until we find pick
    while high >= low:
        #set guess number to halfway
        mid = (high + low) // 2#don't worry about overflow in python
        #based on guess number, set low or high
        api_result = guess(mid)
        if api_result == 0:
            return mid
        if api_result == 1:
            low = mid + 1
        if api_result == -1:
            high = mid - 1
        
    return 0#should never reach this line of code - indicates an error


#time complexity: O(log n)
#space complexity: O(1)
#this algorithm uses a binary search, which has an O(log n) time complexity since it repeatedly cuts all possible values in half with each iteration of the loop.
#it uses a loop instead of a recursive call, which keeps the space complexity at O(1). The algorithm first assumes that pick can be any number from 1 to n and then
# shrinks the lower and upper bounds until it finds pick. Since n can be up to 2^31 -1, binary serach is required because an O(n) solution may continue to run for an extremely long time.
```

</details>

<details>
<summary>Original Document (75927.txt)</summary>

```
My name: Matthew Park
Partner's name: Ian Porto

Guess the Number Higher or Lower
#n is the highest possible number
#return the number that I picked
def guessNumber(n: int) -> int:
    low = 1
	high = n
	
	#loop until we find pick
	while high >= low:
		#set guess number to halfway
		mid = (high + low) // 2#don't worry about overflow in python
		#based on guess number, set low or high
		api_result = guess(mid)
		if api_result == 0:
			return mid
		if api_result == 1:
			low = mid + 1
		if api_result == -1:
			high = mid - 1
		
	return 0#should never reach this line of code - indicates an error


#time complexity: O(log n)
#space complexity: O(1)
#this algorithm uses a binary search, which has an O(log n) time complexity since it repeatedly cuts all possible values in half with each iteration of the loop.
#it uses a loop instead of a recursive call, which keeps the space complexity at O(1). The algorithm first assumes that pick can be any number from 1 to n and then
# shrinks the lower and upper bounds until it finds pick. Since n can be up to 2^31 -1, binary serach is required because an O(n) solution may continue to run for an extremely long time.
```

</details>

---

#### Jordanny Ramos Rodriguez (`70834`)

- **Problem:** Guess Number Higher or Lower
- **Language:** python
- **Score:** 0/7 (Critical Error)
- **Grading status:** graded
- **Repair level:** aggressive
- **Files:** Quiz 3.pdf (pdf)

| Test Case | Result |
|-----------|--------|
| basic | FAIL |
| single | FAIL |
| pick_low | FAIL |
| pick_high | FAIL |
| large | FAIL |
| mid_range | FAIL |
| pick_is_n | FAIL |

<details>
<summary>Edits made by grader</summary>

- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def guessNumber(n): return 0`

</details>

<details>
<summary>Extracted Code (70834.py)</summary>

```python
def guessNumber(n: int) -> int:left, right = 1, nwhile left =< right:mid = (left + right) // 2if guess(mid) == -1:right -
if guess(mid) == 1:left += 1else:return mid
```

</details>

<details>
<summary>Original Document (70834.txt)</summary>

```
def guessNumber(n: int) -> int:left, right = 1, nwhile left =< right:mid = (left + right) // 2if guess(mid) == -1:right -
if guess(mid) == 1:left += 1else:return mid
```

</details>

---

#### Parks Rpk (`65685`)

- **Problem:** Guess Number Higher or Lower
- **Language:** python
- **Score:** 7/7 (PASS)
- **Grading status:** graded
- **Files:** Mock Technical Interview CS102 Spring 2026 (1).txt (direct)

| Test Case | Result |
|-----------|--------|
| basic | PASS |
| single | PASS |
| pick_low | PASS |
| pick_high | PASS |
| large | PASS |
| mid_range | PASS |
| pick_is_n | PASS |

<details>
<summary>Edits made by grader</summary>

- [syntax-only] Removed stray bracket at EOF

</details>

<details>
<summary>Extracted Code (65685.py)</summary>

```python
def guessNumber(n: int) -> int:
    l, r = 1, n                    
    while l <= r:                  
        mid = (l + r) // 2
        result = guess(mid)        
        if result == -1:
            r = mid - 1
        elif result == 1:
            l = mid + 1
        else:
            return mid
                                ]
```

</details>

<details>
<summary>Original Document (65685.txt)</summary>

```
CS102 PAIRED TECHNICAL INTERVIEW

This is the template for what you are expected to submit for the CS102 PAIRED Technical Interview.
Please make sure you have your items in this order when you submit so the we can grade it easier🙏

Refer back to the Paired Technical Interview Print outs to the content you should submit.
In general, you should submit at least a number and some notes for the interviewer side, and your full code solution for the Candidate.

We encourage you to comment your code if you'd like!

[Your Name : Parks RPK ]

[Your Partner's Name : Zhi Xiong lu]





Interviewer Form

[Problem Given]

1) Problem Understanding [4]
 - He quite got the problem in the first read , and explained me pretty well and also once I confirmed his understanding is right he explained me the time complexity right after.
2) Communication & Collaboration [4]
 - very clear and structure explanation bruh just drawn the whole thing in the paper and explain so good step by step.
3) Implementation & Technical Depth [3]
-The one point where he tripped a little bit is when I asked him what is the optimal solution time complexity, (Though his solution was a optimal) he was thinking and asked an clarifying question, somehow atlast he was not tricked and came back to the track
4) Team Fit & Working Style
 - He was energetic and ran his test case walkthrough pretty well, also he always asked me whether I am following each and every step, which I think is a really a great thing when it comes to the real world when working as a group.
Final Evaluation

Final Decision
Bruh is PASSED!



Candidate Form

This is Parks' code as an candidate:
[
def guessNumber(n: int) -> int:
    l, r = 1, n                    
    while l <= r:                  
        mid = (l + r) // 2
        result = guess(mid)        
        if result == -1:
            r = mid - 1
        elif result == 1:
            l = mid + 1
        else:
            return mid
                                  ]
```

</details>

---

#### Hewitt Wang (`70374`)

- **Problem:** Guess Number Higher or Lower
- **Language:** python
- **Score:** 7/7 (PASS)
- **Grading status:** graded
- **Files:** sol.py (direct)

| Test Case | Result |
|-----------|--------|
| basic | PASS |
| single | PASS |
| pick_low | PASS |
| pick_high | PASS |
| large | PASS |
| mid_range | PASS |
| pick_is_n | PASS |

<details>
<summary>Extracted Code (70374.py)</summary>

```python
# -1 if the real number is lower
# 0 if the number is equal
# 1 if the real number is higher
# placeholder for testing
def guess(n: int) -> int:
    if (n == 42): return 0
    elif (n > 42): return -1
    else: return 1

def guessNumber(n: int) -> int:
    l = 1
    r = n
    
    while l <= r:
        mid = (l + r) // 2
        result = guess(mid)
        
        if result == -1:
            r = mid - 1
        elif result == 1:
            l = mid + 1
        else:
            return mid

    # no fallback case - we assume correctness

# testing
print(guessNumber(90))
```

</details>

<details>
<summary>Original Document (70374.txt)</summary>

```
# -1 if the real number is lower
# 0 if the number is equal
# 1 if the real number is higher
# placeholder for testing
def guess(n: int) -> int:
    if (n == 42): return 0
    elif (n > 42): return -1
    else: return 1

def guessNumber(n: int) -> int:
    l = 1
    r = n
    
    while l <= r:
        mid = (l + r) // 2
        result = guess(mid)
        
        if result == -1:
            r = mid - 1
        elif result == 1:
            l = mid + 1
        else:
            return mid

    # no fallback case - we assume correctness

# testing
print(guessNumber(90))
```

</details>

---

#### Kevin Yang (`79336`)

- **Problem:** Guess Number Higher or Lower
- **Language:** java
- **Score:** 0/7 (Critical Error)
- **Grading status:** graded
- **Repair level:** aggressive
- **Files:** CS102 PAIRED TECHNICAL INTERVIEW Finished.txt (direct)

| Test Case | Result |
|-----------|--------|
| basic | FAIL |
| single | FAIL |
| pick_low | FAIL |
| pick_high | FAIL |
| large | FAIL |
| mid_range | FAIL |
| pick_is_n | FAIL |

<details>
<summary>Edits made by grader</summary>

- [syntax-only] Mechanical Java->Python transpile
- [syntax-only] Fixed typo -> 'True'
- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def guessNumber(n): return 0`

</details>

<details>
<summary>Extracted Code (79336.java)</summary>

```java
public int guessNumber(int n){
    int low = 1;
    int high = n;
    int middleNum = (int) n /2;
    while(true){
        if(guess(middleNum) == 0){ //Equals
            return middleNum;
        }else if(guess(middleNum) == -1){ //High
            high = middleNum;
        }else{//Low
            low = middleNum;
        }
        middleNum = (high - low) / 2 + low;
    }
}
```

</details>

<details>
<summary>Original Document (79336.txt)</summary>

```
CS102 PAIRED TECHNICAL INTERVIEW

This is the template for what you are expected to submit for the CS102 PAIRED Technical Interview.
Please make sure you have your items in this order when you submit so the we can grade it easier🙏

Refer back to the Paired Technical Interview Print outs to the content you should submit. The interviewer form & candidate reflection should be submitted on paper. The candidate code should be submitted with the format below:

We encourage you to comment your code if you'd like!

[Your Name]
Kevin Yang

[Your Partner's Name]
Christian Z.

Candidate Form

[Insert Submitted Code]
public int guessNumber(int n){
	int low = 1;
	int high = n;
	int middleNum = (int) n /2;
	while(true){
		if(guess(middleNum) == 0){ //Equals
			return middleNum;
		}else if(guess(middleNum) == -1){ //High
			high = middleNum;
		}else{//Low
			low = middleNum;
		}
		middleNum = (high - low) / 2 + low;
	}
}
```

</details>

---

#### Lilian Yuan (`75939`)

- **Problem:** Guess Number Higher or Lower
- **Language:** java
- **Score:** 0/7 (Critical Error)
- **Grading status:** graded
- **Repair level:** aggressive
- **Files:** Lilian Yuan- CS102 PAIRED TECHNICAL INTERVIEW.txt (direct)

| Test Case | Result |
|-----------|--------|
| basic | FAIL |
| single | FAIL |
| pick_low | FAIL |
| pick_high | FAIL |
| large | FAIL |
| mid_range | FAIL |
| pick_is_n | FAIL |

<details>
<summary>Edits made by grader</summary>

- [syntax-only] Mechanical Java->Python transpile
- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers

</details>

<details>
<summary>Extracted Code (75939.java)</summary>

```java
public int guessNumber(int n){
    int min= 1;
    int max = n;

    while(min<=max){
        int pick = n/2;
        int guess = guess(pick);
        if(guess == -1){
            min = pick-1;
        }
        else if(guess == 1){
            max = pick;
        else{
            return pick;
        }
    }
    return 0;

}
```

</details>

<details>
<summary>Original Document (75939.txt)</summary>

```
CS102 PAIRED TECHNICAL INTERVIEW

This is the template for what you are expected to submit for the CS102 PAIRED Technical Interview.
Please make sure you have your items in this order when you submit so the we can grade it easier🙏

Refer back to the Paired Technical Interview Print outs to the content you should submit.
In general, you should submit at least a number and some notes for the interviewer side, and your full code solution for the Candidate.

We encourage you to comment your code if you'd like!

[Lilian Yuan]

[Solomon Coverdale]

Interviewer Form

[Contains Duplicate II] (Just the Name of the Problem is fine)

1) Problem Understanding

3 - Mostly lear, minor clarifications
Notes:
asked good questions and made sure to understand the problem fully before starting

2) Communication & Collaboration

3 - Clear, receptive, reasonably collaborative
Notes:
made sure to explain the code but sometimes would hesitate

3) Implementation & Technical Depth

4- clean, correct, well-tested solution with strong optimization and tradeoff discussion
Notes:
used the optimal data structure for this problem

4) Team Fit & Working Style

4- Strong team asset; calm under uncertainty, humble, ownership mindset
Notes:
asked good clarifying questions, talked calmly, seemed to think through the problem

Final Evaluation: 
14/16
Hire

Final Decision
Candidate was calm and made clarifying questions. I liked how he thought through the process before starting the code. There were times where he would hesitate while writing code but I think he was just making sure what he was doing was right. 

Candidate Form - Guess Number Higher or Lower

public int guessNumber(int n){
	int min= 1;
	int max = n;

	while(min<=max){
		int pick = n/2;
		int guess = guess(pick);
		if(guess == -1){
			min = pick-1;
		}
		else if(guess == 1){
			max = pick;
		else{
			return pick;
		}
	}
	return 0;

}
```

</details>

---

#### Rijaa Zaidi (`67309`)

- **Problem:** Guess Number Higher or Lower
- **Language:** python
- **Score:** 0/7 (Critical Error)
- **Grading status:** graded
- **Repair level:** aggressive
- **Files:** technicalineterview.txt (direct)

| Test Case | Result |
|-----------|--------|
| basic | FAIL |
| single | FAIL |
| pick_low | FAIL |
| pick_high | FAIL |
| large | FAIL |
| mid_range | FAIL |
| pick_is_n | FAIL |

<details>
<summary>Edits made by grader</summary>

- [syntax-only] Converted // comments to #
- [syntax-only] Converted // comments to #
- [syntax-only] Lowered keyword 'While'
- [syntax-only] Extracted function block from noisy file
- [ambiguous] Conservative re-indent: normalized indent levels to 4-space tiers
- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def guessNumber(n): return 0`

</details>

<details>
<summary>Extracted Code (67309.py)</summary>

```python
Date: 04/27/2026
Problem Given: Longest Substring Without Repeating Characters

Problem Understanding (0-4): 1
Notes: recognized sliding window pattern and hashset, required step by step assistance across all parts of the problem

Communication and Collaboration (0-4): 2
Notes: Didn't address the interviewer very much, thoughts were spoken in parts rather than a full sentence, I had to questions to understand the problem rather than being asked questions

Implementation and Technical Depth (0-4): 3
Notes: correct solution after heavy assistance

Team Fit and Working Style (0-4): 1
Notes: Took a few attempts to recieve feedback, spent a not insignificant amount of time on disliking sliding window

Total Score: 7/16
Hiring Reccomendation: No Hire

Final Decision (3-5 Sentences):
Strignths: Tianna didn't outright reject advice and was open to recieving new information. 
Weaknesses: That said, most of that information was about basic implementation and explaining how data structures worked, leaving little time for complexity analysis and discussion
Reasoning: While I appreciate that she's open to learn, it took a lot of time and help to get to the final solution. Lack of technical skill ultimately swayed me to no hire.


Leetcode Solution:
Rijaa Zaidi
Tianna Balkam

def guessNumber(n: int) -> int:
        //n is input, we want pick
        //binary search

        l,r = 1, n

        while l <= r:
                mid = (l + r) // 2
                if guess(mid) == 0:
                        return mid
                elif guess(mid) == 1:
                        l = mid + 1
                else:
                        r = mid - 1
        return 0


        Write-up:
        This solution uses binary search to cut down on the search range and find the solution in O(logn) time. by finding the middle value between l and r and adjusting each pointer based on the guess function output (increasing l if mid was less than pick and decreasing r if mid was greater than pick), the correct picked value will eventually found.
```

</details>

<details>
<summary>Original Document (67309.txt)</summary>

```
Interviewer Evaluation:
Candidate Name: Tianna Balkam
Interviewer Name: Rijaa Zaidi
Date: 04/27/2026
Problem Given: Longest Substring Without Repeating Characters

Problem Understanding (0-4): 1
Notes: recognized sliding window pattern and hashset, required step by step assistance across all parts of the problem

Communication and Collaboration (0-4): 2
Notes: Didn't address the interviewer very much, thoughts were spoken in parts rather than a full sentence, I had to questions to understand the problem rather than being asked questions

Implementation and Technical Depth (0-4): 3
Notes: correct solution after heavy assistance

Team Fit and Working Style (0-4): 1
Notes: Took a few attempts to recieve feedback, spent a not insignificant amount of time on disliking sliding window

Total Score: 7/16
Hiring Reccomendation: No Hire

Final Decision (3-5 Sentences):
Strignths: Tianna didn't outright reject advice and was open to recieving new information. 
Weaknesses: That said, most of that information was about basic implementation and explaining how data structures worked, leaving little time for complexity analysis and discussion
Reasoning: While I appreciate that she's open to learn, it took a lot of time and help to get to the final solution. Lack of technical skill ultimately swayed me to no hire.


Leetcode Solution:
Rijaa Zaidi
Tianna Balkam

def guessNumber(n: int) -> int:
//n is input, we want pick
//binary search

l,r = 1, n

while l <= r:
	mid = (l + r) // 2
	if guess(mid) == 0:
		return mid
	elif guess(mid) == 1:
		l = mid + 1
	else:
	     r = mid - 1
return 0


Write-up:
This solution uses binary search to cut down on the search range and find the solution in O(logn) time. by finding the middle value between l and r and adjusting each pointer based on the guess function output (increasing l if mid was less than pick and decreasing r if mid was greater than pick), the correct picked value will eventually found.
```

</details>

---

#### Qianjun Zhou (`77691`)

- **Problem:** Guess Number Higher or Lower
- **Language:** python
- **Score:** 7/7 (PASS)
- **Grading status:** graded
- **Files:** CS102 PAIRED TECHNICAL INTERVIEW.txt (direct)

| Test Case | Result |
|-----------|--------|
| basic | PASS |
| single | PASS |
| pick_low | PASS |
| pick_high | PASS |
| large | PASS |
| mid_range | PASS |
| pick_is_n | PASS |

<details>
<summary>Edits made by grader</summary>

- [syntax-only] Removed trailing triple-quote

</details>

<details>
<summary>Extracted Code (77691.py)</summary>

```python
def guessNumber(n: int) -> int:
    min = 1
    max = n
    while True:
        currGuess = min + ((max - min) // 2)
        guessRet = guess(currGuess)
        if (guessRet == 1):
            min = currGuess + 1
        if (guessRet == -1):
            max = currGuess - 1
        if (guessRet == 0):
            return currGuess
"""
```

</details>

<details>
<summary>Original Document (77691.txt)</summary>

```
CS102 PAIRED TECHNICAL INTERVIEW

This is the template for what you are expected to submit for the CS102 PAIRED Technical Interview.
Please make sure you have your items in this order when you submit so the we can grade it easier🙏

Refer back to the Paired Technical Interview Print outs to the content you should submit.
In general, you should submit at least a number and some notes for the interviewer side, and your full code solution for the Candidate.

We encourage you to comment your code if you'd like!

[Your Name] Qianjun Ryan Zhou

[Your Partner's Name] Kenneth Ng

Interviewer Form

[Problem Given] Merge Two Sorted Lists 

1) Problem Understanding
4
-Quickly understood the premise of the solution and that it needed two pointer to be most efficient
-Found edge cases and simple construction that allows you to resolve the issues
-Ended up using a weird form of two pointer that was exactly the same as the solution. Making sure to keep the return value of the head stored.

2) Communication & Collaboration
4
-Very adaptive, follows whatever structure the node class needs to be and asks for base code on those.(unable to be given)
-Understanding to many possible solutions and understands in which cases certain solution can be more efficient/fit the use case. 
-Feedback/hint were understood very well.

3) Implementation & Technical Depth
4
-Very linear programmer, finds the line that he needs to code and follows it step by step.
-Gets the main idea of the function down and then resolves the intricacies.

4) Team Fit & Working Style
4
-Very calm under pressure, got the solution out in a reasonable amount of time and was fine with being wrong in certain parts of the code. 
-Takes alot of pride in his own code, understands that the code needs to be perfect before being allowed to be added to the final product and took time to triple check his work to make sure it doesn't cause any problems.


Final Evaluation
16/16 Strong Hire 

Final Decision
He was able to understand and solve the problem on his own in a reasonable amount of time and produced code worth of being pushed onto the final product. The solution was as efficient as possible and he understood what changes could be made to fit a different restriction. There were confusing edge cases that he needed hints for but I wouldn't blame him for it.

Candidate Form

Guess Number Higher or Lower

def guessNumber(n: int) -> int:
	min = 1
	max = n
	while True:
		currGuess = min + ((max - min) // 2)
		guessRet = guess(currGuess)
		if (guessRet == 1):
			min = currGuess + 1
		if (guessRet == -1):
			max = currGuess - 1
		if (guessRet == 0):
			return currGuess
"""
I get 1 input n which is the possible numbers that I can return. I get a helper function which has 1 of 3 returns in an int which can guide my while loop.
The fastest this solution can be is log(n) since it tells if the guess is higher or lowers. We used a binary search which is O(log(n)) and the space complexity since we only needed to save 3 value is O(1).
I know i need a while loop since thats how I would code the binary search. I know I need to keep track of the range of values so i need two constants a min possible value and a max possible value. And then theres just the 3 cases of if statements. 
"""
```

</details>

---

#### Santiago Zuluaga (`79862`)

- **Problem:** Guess Number Higher or Lower
- **Language:** python
- **Score:** 7/7 (PASS)
- **Grading status:** graded
- **Files:** CS102 PAIRED TECHNICAL INTERVIEW Santiago Zuluaga.txt (direct)

| Test Case | Result |
|-----------|--------|
| basic | PASS |
| single | PASS |
| pick_low | PASS |
| pick_high | PASS |
| large | PASS |
| mid_range | PASS |
| pick_is_n | PASS |

<details>
<summary>Edits made by grader</summary>

- [syntax-only] Removed trailing semicolons
- [syntax-only] Removed stray bracket at EOF
- [syntax-only] Added missing colons

</details>

<details>
<summary>Extracted Code (79862.py)</summary>

```python
def guessNumber(n: int):
    
    start, end = 1, n


    while start <= end:
        
        pick = start + (end-start) // 2 
        
        if guess(pick) == 1:
            start = pick + 1

        elif guess(pick) == -1:
            end = pick - 1 

        else
            return pick; 
 
]
```

</details>

<details>
<summary>Original Document (79862.txt)</summary>

```
CS102 PAIRED TECHNICAL INTERVIEW

This is the template for what you are expected to submit for the CS102 PAIRED Technical Interview.
Please make sure you have your items in this order when you submit so the we can grade it easier🙏

Refer back to the Paired Technical Interview Print outs to the content you should submit.
In general, you should submit at least a number and some notes for the interviewer side, and your full code solution for the Candidate.

We encourage you to comment your code if you'd like!

[Santiago Zuluaga]

[Jason Seng]

Interviewer Form

[Reverse polish notation ] (Just the Name of the Problem is fine)

1) Problem Understanding 2/4
IT was a difficult problem so it took some time to understand what was needed and needed hints regarding polish 

2) Communication & Collaboration
Communicated effectively thoughts and ideas regarding the problem and how it could be approached also asked questions regarding uncertainties 
3) Implementation & Technical Depth
Needed some clarifications regarding how to use the data structure and what was exactly happening 
4) Team Fit & Working Style
The person was enthusiastic and motivated to express their knowledge and learn from the process. 
Final Evaluation

Final Decision

Candidate Form

[Python coding

	def guessNumber(n: int):
	
	start, end = 1, n


	while start <= end:
		
		pick = start + (end-start) // 2 
		
		if guess(pick) == 1:
			start = pick + 1

		elif guess(pick) == -1:
			end = pick - 1 

		else
			return pick; 
 
]
```

</details>

---

### Longest Substring Without Repeating Characters

#### Tianna Balkam (`67581`)

- **Problem:** Longest Substring Without Repeating Characters
- **Language:** python
- **Score:** 1/8 (Critical Error)
- **Grading status:** graded
- **Files:** def lengthOfLongestSubstring(s str).txt (direct)

| Test Case | Result |
|-----------|--------|
| example1 | FAIL |
| all_same | FAIL |
| example3 | FAIL |
| empty | PASS |
| single_char | FAIL |
| all_unique | FAIL |
| spaces | FAIL |
| end_longest | FAIL |

<details>
<summary>Extracted Code (67581.py)</summary>

```python
def lengthOfLongestSubstring(s: str) -> int:
    l = 0
    count = 0
    seen = set()
    for r in range(len(s)):
        if s[r] in seen:
            seen.remove(s[l])
            left += 1
        seen.add(s[r])
        count = max(count, s[r] - s[l] + 1)
    return count
```

</details>

<details>
<summary>Original Document (67581.txt)</summary>

```
def lengthOfLongestSubstring(s: str) -> int:
	l = 0
	count = 0
	seen = set()
	for r in range(len(s)):
		if s[r] in seen:
			seen.remove(s[l])
			left += 1
		seen.add(s[r])
		count = max(count, s[r] - s[l] + 1)
	return count
```

</details>

---

#### Clare Calandra (`68530`)

- **Problem:** Longest Substring Without Repeating Characters
- **Language:** python
- **Score:** 8/8 (PASS)
- **Grading status:** graded
- **Files:** CS102 PAIRED TECHNICAL INTERVIEW.txt (direct)

| Test Case | Result |
|-----------|--------|
| example1 | PASS |
| all_same | PASS |
| example3 | PASS |
| empty | PASS |
| single_char | PASS |
| all_unique | PASS |
| spaces | PASS |
| end_longest | PASS |

<details>
<summary>Extracted Code (68530.py)</summary>

```python
def lengthOfLongestSubstring(s: str) -> int:
    set_of_chars = set() #create a HashSet to track chars (make sure no repeats)
    left = 0 #track elements (2-pointer method start left pointer at index 0)
    length = 0 #keep track of return value (start at 0)
    for i in range(len(s)): #iterate through the elements(characters) of the given string s 
        while s[i] in set_of_chars: # if the element is in the set, execute the following
            set_of_chars.remove(s[left]) #remove the character from the set 
            left += 1 #increment left pointer 
        set_of_chars.add(s[i]) #add the element back to set after removing duplicates  
        length = max(length, i - left + 1) # to return the correct length, take max 
        #of the current length and (the difference between the right and left pointer indices + 1)  
    return length #return the length of the string without duplicates 
# time complexity is O(n) because I utilized a HashSet and iterated through each element in the given string using # the two-pointer method (the left pointer starts at zero and increments by 1 to the right)
```

</details>

<details>
<summary>Original Document (68530.txt)</summary>

```
CS102 PAIRED TECHNICAL INTERVIEW

This is the template for what you are expected to submit for the CS102 PAIRED Technical Interview.
Please make sure you have your items in this order when you submit so the we can grade it easier🙏

Refer back to the Paired Technical Interview Print outs to the content you should submit.
In general, you should submit at least a number and some notes for the interviewer side, and your full code solution for the Candidate.

We encourage you to comment your code if you'd like!

[Clare Calandra]

[Ashley Carozza]

Interviewer Form

[Evaluate Reverse Polish Notation] (Just the Name of the Problem is fine)

1) Problem Understanding
4 - Fully understood, restated clearly 
Comments: 
- exemplified full understanding of the problem 
- knew which data structure to use and the importance of the order of operands 

2) Communication & Collaboration
4 - Very clear, structured, highly collaborative & adaptive 
Comments: 
- asked questions about edge cases & specifics on inputs 
- asked to clarify division by zero in this scenario 
- communicated thought process behind data structure chosen(stack) 

3) Implementation & Technical Depth
4 - Clean, correct, well-tested solution with strong optimization and tradeoff discussion 
Comments: 
- used all examples to test code & they passed 
- also ran through an example to explain in words how it worked 

4) Team Fit & Working Style
4 - Strong team asset; calm under uncertainty, humble, ownership mindset 
Comments: 
- positive attitude 
- very receptive to comments & hints/help 
- did not panic, was humble, and handled the problem in a calm manner 

Final Evaluation
16/16 - Strong hire recommendation 

Final Decision
    Ashley is an overall exceptional candidate after acing this technical interview. Not only did she show a deep understanding of the problem at hand, but also portrayed a humble, calm, and ownership mindset. She asked all the right questions when it came to edge cases and certain limitations on the question (input only having +, -, *, /, and ints and division by zero clarification). Additionally, she communicated her thought process well throughout the entire interview. 

Candidate Form

def lengthOfLongestSubstring(s: str) -> int:
    set_of_chars = set() #create a HashSet to track chars (make sure no repeats)
    left = 0 #track elements (2-pointer method start left pointer at index 0)
    length = 0 #keep track of return value (start at 0)
    for i in range(len(s)): #iterate through the elements(characters) of the given string s 
        while s[i] in set_of_chars: # if the element is in the set, execute the following
            set_of_chars.remove(s[left]) #remove the character from the set 
            left += 1 #increment left pointer 
        set_of_chars.add(s[i]) #add the element back to set after removing duplicates  
        length = max(length, i - left + 1) # to return the correct length, take max 
        #of the current length and (the difference between the right and left pointer indices + 1)  
    return length #return the length of the string without duplicates 
# time complexity is O(n) because I utilized a HashSet and iterated through each element in the given string using # the two-pointer method (the left pointer starts at zero and increments by 1 to the right)
```

</details>

---

#### Carson Carey (`74510`)

- **Problem:** Longest Substring Without Repeating Characters
- **Language:** java
- **Score:** 1/8 (Critical Error)
- **Grading status:** graded
- **Repair level:** aggressive
- **Files:** Technical Interview CS102.rtf (rtf)

| Test Case | Result |
|-----------|--------|
| example1 | FAIL |
| all_same | FAIL |
| example3 | FAIL |
| empty | PASS |
| single_char | FAIL |
| all_unique | FAIL |
| spaces | FAIL |
| end_longest | FAIL |

<details>
<summary>Edits made by grader</summary>

- [syntax-only] Mechanical Java->Python transpile
- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def lengthOfLongestSubstring(s): return 0`

</details>

<details>
<summary>Extracted Code (74510.java)</summary>

```java
//

public int lengthOfLongestSubstring(String s) {
    HashSet<Character> seen = new HashSet<Character>();
    int maxLength = 0;
    int l = 0;

    for(int r = 0; r<s.length(); r++) {
        while(seen.contains(s.charAt(r))) {
            seen.remove(s.charAt(l));
            l++;
        }
        seen.add(s.charAt(r));

        if(r-l+1>maxLength) {
            maxLength = r-l+1;
        }
    }
    return maxLength;
}
```

</details>

<details>
<summary>Original Document (74510.txt)</summary>

```
Candidate: Carson Carey

Interviewer: Danila Safronov

Candidate Form

//

public int lengthOfLongestSubstring(String s) {
	HashSet<Character> seen = new HashSet<Character>();
	int maxLength = 0;
	int l = 0;

	for(int r = 0; r<s.length(); r++) {
		while(seen.contains(s.charAt(r))) {
			seen.remove(s.charAt(l));
			l++;
		}
		seen.add(s.charAt(r));

		if(r-l+1>maxLength) {
			maxLength = r-l+1;
		}
	}
	return maxLength;
}
```

</details>

---

#### Shunyi Chen (`79105`)

- **Problem:** Longest Substring Without Repeating Characters
- **Language:** python
- **Score:** 6/8 (Minor Error)
- **Grading status:** graded
- **Files:** CS102 PAIRED TECHNICAL INTERVIEW.txt (direct)

| Test Case | Result |
|-----------|--------|
| example1 | PASS |
| all_same | PASS |
| example3 | FAIL |
| empty | PASS |
| single_char | PASS |
| all_unique | PASS |
| spaces | FAIL |
| end_longest | PASS |

<details>
<summary>Edits made by grader</summary>

- [syntax-only] Replaced Unicode line separator

</details>

<details>
<summary>Extracted Code (79105.py)</summary>

```python
def lengthOfLongestSubstring(s: str) -> int
    dict = {}
    right, left = 0, 0
    max = 0
    while right < len(s):
        if not s[right] in dict:
            dict[s[right]] = 0
            right+=1
            temp = right - left
            if temp > max:
                max = temp
        else:             left+=1
            del dict[s[left]]

    return max
```

</details>

<details>
<summary>Original Document (79105.txt)</summary>

```
CS102 PAIRED TECHNICAL INTERVIEW

This is the template for what you are expected to submit for the CS102 PAIRED Technical Interview.
Please make sure you have your items in this order when you submit so the we can grade it easier🙏

Refer back to the Paired Technical Interview Print outs to the content you should submit.
In general, you should submit at least a number and some notes for the interviewer side, and your full code solution for the Candidate.

We encourage you to comment your code if you'd like!

Shunyi Chen
Kartik Wahlin

Interviewer Form

evaluate reverse polish notation (Just the Name of the Problem is fine)

1) Problem Understanding
4
double checked with me if he missed anything regarding question, also explained question in own words

2) Communication & Collaboration
4
shows me he knows his plan. explains throughly. told me that he would need to pop and append to another stack, explained each section of code, like telling me why he needed a if else statement

3) Implementation & Technical Depth
4
solution if very efficient and very optimized. he double checked with me. he asked me about constraints, checked if it was the same on my paper, and realized about an empty list being an edge case and asked me to double check that as well.

4) Team Fit & Working Style
4
yes i would hire him because hes very open to feedback and suggestions, like i suggested that he couldve not had an else statement and he was like yeah i see that

Final Evaluation
16/16
Final Decision
i would definitely hire this guy. hes veyr open to feedback, and takes time before and after to explain his thinking and strategy as well. i think he would work very well in a team setting
Candidate Form

[Insert Submitted Code] - my question is longest substring without repeating characters

def lengthOfLongestSubstring(s: str) -> int
	dict = {}
	right, left = 0, 0
	max = 0
	while right < len(s):
		if not s[right] in dict:
			dict[s[right]] = 0
			right+=1
			temp = right - left
			if temp > max:
				max = temp
		else: 			left+=1
			del dict[s[left]]

	return max
```

</details>

---

#### William Conroy (`67634`)

- **Problem:** Longest Substring Without Repeating Characters
- **Language:** python
- **Score:** 8/8 (PASS)
- **Grading status:** graded
- **Files:** CS102 PAIRED TECHNICAL INTERVIEW.txt (direct)

| Test Case | Result |
|-----------|--------|
| example1 | PASS |
| all_same | PASS |
| example3 | PASS |
| empty | PASS |
| single_char | PASS |
| all_unique | PASS |
| spaces | PASS |
| end_longest | PASS |

<details>
<summary>Extracted Code (67634.py)</summary>

```python
def lengthOfLongestSubstring(s: str) -> int:

    l = 0

    windowSum = 0

    h = set()

    for right in range(len(s)):
        while s[right] in h:
            h.remove(s[l])
            l += 1
        h.add(s[right])
        windowSum = max(windowSum, right - l + 1)

    return windowSum
```

</details>

<details>
<summary>Original Document (67634.txt)</summary>

```
CS102 PAIRED TECHNICAL INTERVIEW

This is the template for what you are expected to submit for the CS102 PAIRED Technical Interview.
Please make sure you have your items in this order when you submit so the we can grade it easier🙏

Refer back to the Paired Technical Interview Print outs to the content you should submit. The interviewer form & candidate reflection should be submitted on paper. The candidate code should be submitted with the format below:

We encourage you to comment your code if you'd like!

William Conroy

Ivan Cheung

Candidate Form



Final Decision for Ivan:
15/16 Strong Hire


Overall Ivan is a strong hire. While he was a little lost at the start he talked it through and was able to piece everything together throughout the interview. After helping with the data structure he wrote pseudocode to ensure he had a plan. He also asked communicated his ideas ensuring he was on the right track along the way. (Other comments on paper)



Technical Interview

def lengthOfLongestSubstring(s: str) -> int:

l = 0

windowSum = 0

h = set()

for right in range(len(s)):
	while s[right] in h:
		h.remove(s[l])
		l += 1
	h.add(s[right])
	windowSum = max(windowSum, right - l + 1)

return windowSum
```

</details>

---

#### Michael DiNapoli (`65542`)

- **Problem:** Longest Substring Without Repeating Characters
- **Language:** python
- **Score:** 1/8 (Critical Error)
- **Grading status:** graded
- **Files:** Michael DiNapoli CS 102 Paired Technical Interview Printouts.pdf (pdf); Michael DiNapoli Mock Interview.txt (direct)

| Test Case | Result |
|-----------|--------|
| example1 | FAIL |
| all_same | FAIL |
| example3 | FAIL |
| empty | PASS |
| single_char | FAIL |
| all_unique | FAIL |
| spaces | FAIL |
| end_longest | FAIL |

<details>
<summary>Extracted Code (65542.py)</summary>

```python
def lengthOfLongestSubstring(s):
    left = 0
    maxlength = 0
    substring = set()

    for right in range(len(s)):
        while s[right] in substring:
            substring.remove(s[left])
            left+=1
        substring.add(s[right])
        maxlength = max(substring, right - left + 1)

    return maxlength

# Michael DiNapoli O(n^2)
```

</details>

<details>
<summary>Original Document (65542.txt)</summary>

```
Paired
 
Technical
 
Interview
 
Overview
 
 
Mock
 
interviews
 
are
 
one
 
of
 
the
 
most
 
effective
 
ways
 
to
 
prepare
 
for
 
technical
 
interviews.
 
They
 
help
 
you
 
practice
 
solving
 
problems
 
under
 
realistic
 
time
 
pressure
 
while
 
also
 
developing
 
the
 
technical
 
communication
 
skills
 
required
 
in
 
a
 
real
 
interview
 
setting.
 
In
 
addition,
 
you’ll
 
gain
 
experience
 
evaluating
 
a
 
candidate’ s
 
performance
 
from
 
the
 
interviewer ’s
 
perspective,
 
which
 
will
 
help
 
you
 
understand
 
how
 
hiring
 
decisions
 
are
 
made.
 
 
You
 
will
 
work
 
in
 
pairs,
 
either
 
with
 
a
 
partner
 
you
 
choose
 
or
 
one
 
assigned
 
to
 
you
 
if
 
needed.
 
Each
 
pair
 
will
 
consist
 
of
 
one
 
interviewer ,
 
and
 
one
 
candidate.
 
Interviewer
 
 
 
As
 
the
 
interviewer ,
 
your
 
job
 
is
 
to
 
run
 
the
 
interview ,
 
make
 
a
 
hiring
 
decision,
 
and
 
CRUSH
 
DREAMS
 
��
 
(earnestly
 
evaluate
 
performance.)
 
 
You
 
will:
 
 
●
 
Introduce
 
and
 
explain
 
the
 
problem
 
clearly
 
 
●
 
Read
 
the
 
question
 
prompt
 
and
 
clarify
 
requirements
 
 
●
 
Discuss
 
edge
 
cases
 
and
 
constraints
 
 
●
 
Provide
 
hints
 
when
 
appropriate
 
(without
 
giving
 
away
 
the
 
solution)
 
●
 
Answer
 
the
 
candidate’ s
 
questions
 
 
●
 
Write
 
and
 
submit
 
 
○
 
Structured
 
notes
 
taken
 
during
 
the
 
interview
 
 
○
 
A
 
short
 
evaluation
 
of
 
performance,
 
and
 
a
 
hiring
 
decision
 
 
Your
 
evaluation
 
should
 
include:
 
 
●
 
Key
 
strengths
 
 
●
 
Key
 
weaknesses
 
 
●
 
A
 
hiring
 
recommendation
 
 
You
 
will
 
be
 
graded
 
on
 
the
 
quality
 
of
 
your
 
notes
 
and
 
analysis,
 
not
 
on
 
correctness
 
of
 
hints.
 
Your
 
comments
 
and
 
report
 
will
 
not
 
in
 
any
 
way
 
impact
 
your
 
partner ’s
 
grade.
 
 
Interviewer
 
Advice
 
 
●
 
Guide,
 
don’t
 
solve:
 
Your
 
job
 
is
 
to
 
help
 
them
 
think,
 
not
 
lead
 
them
 
directly
 
to
 
the
 answer .
 
Start
 
with
 
questions
 
before
 
giving
 
hints.
 
 
●
 
Follow
 
thinking:
 
If
 
you
 
can’t
 
follow
 
their
 
thinking,
 
ask
 
them
 
questions:
 
“What
 
are
 
you
 
thinking?”
 
or
 
“Can
 
you
 
walk
 
me
 
through
 
your
 
approach.”
 
 
●
 
Use
 
progressive
 
hints:
 
If
 
they
 
need
 
hints,
 
start
 
with
 
broad
 
questions,
 
then
 
give
 
small
 
nudges
 
only
 
if
 
needed.
 
Avoid
 
jumping
 
straight
 
to
 
the
 
key
 
idea.
 
●
 
Look
 
for
 
positive
 
signals,
 
not
 
perfection:
 
Focus
 
on
 
how
 
they
 
reason,
 
adapt,
 
and
 
communicate.
 
Getting
 
the
 
optimal
 
solution
 
is
 
ideal,
 
but
 
not
 
required
 
if
 
their
 
communication
 
and
 
reasoning
 
is
 
strong.
 
 
●
 
You
 
will
 
be
 
partially
 
graded
 
on
 
your
 
notes
 
in
 
each
 
section
:
 
Good
 
evaluations
 
use
 
concrete
 
examples
 
(e.g.,
 
“identified
 
hashmap
 
approach
 
after
 
hint”
 
or
 
“Clearly
 
communicated
 
why
 
stacks
 
were
 
the
 
optimal
 
solution
 
without
 
prompting”
 
vs.
 
“did
 
well”).
 
Interviewer
 
Evaluation
 
Form
 
 
Candidate
 
Information
 
 
●
 
Candidate
 
Name:
 
Ava
 
Attina
 
●
 
Interviewer
 
Name:
 
Michael
 
DiNapoli
 
●
 
Date:
 
5/6/2026
 
●
 
Problem
 
Given:
 
Evaluate
 
Reverse
 
Polish
 
Notation
 
1.
 
Problem
 
Understanding
 
(0–4)
 
Did
 
the
 
candidate
 
clearly
 
understand
 
the
 
problem?
 
 
0
 
–
 
Completely
 
misunderstood
 
 
1
 
–
 
Major
 
gaps,
 
needed
 
heavy
 
assistance
 
 
2
 
–
 
Partial
 
understanding,
 
some
 
clarification
 
needed
 
3
 
–
 
Mostly
 
clear ,
 
minor
 
clarifications
 
 
4
 
–
 
Fully
 
understood,
 
restated
 
clearly
 
 
Notes:
 
Shefully
 
understood
 
the
 
problem.
 
She
 
completed
 
it
 
with
 
some
 
minor
 
clarifications.
 
She
 
knew
 
the
 
data
 
structure
 
nd
 
how
 
to
 
work
 
through
 
the
 
problem
 
by
 
identifying
 
how
 
to
 
use
 
conditionals
 
to
 
complete
 
the
 
problem.
 
 
2.
 
Communication
 
&
 
Collaboration
 
(0–4)
 
 
Did
 
the
 
candidate
 
clearly
 
explain
 
their
 
thinking
 
and
 
work
 
effectively
 
with
 
the
 interviewer?
 
 
0
 
–
 
No
 
explanation,
 
unresponsive
 
or
 
defensive
 
 
1
 
–
 
Very
 
unclear ,
 
struggled
 
with
 
feedback
 
 
2
 
–
 
Some
 
explanation,
 
inconsistent
 
collaboration
 
 
3
 
–
 
Clear ,
 
receptive,
 
reasonably
 
collaborative
 
 
4
 
–
 
Very
 
clear ,
 
structured,
 
highly
 
collaborative
 
and
 
adaptive
 
 
Notes:
 
yes
 
very
 
clear ,
 
structure
 
and
 
highly
 
collaborative
 
and
 
adaptive.
 
Explained
 
why
 
she
 
did
 
the
 
code
 
the
 
way
 
she
 
did
 
it.
 
3.
 
Implementation
 
&
 
Technical
 
Depth
 
(0–4)
 
 
How
 
well
 
did
 
they
 
implement
 
their
 
solution
 
and
 
reason
 
about
 
its
 
correctness
 
and
 
efficiency?
 
(Coding,
 
testing,
 
complexity ,
 
optimization)
 
 
0
 
–
 
No
 
working
 
solution,
 
no
 
understanding
 
of
 
complexity
 
 
1
 
–
 
Major
 
issues,
 
incorrect
 
or
 
missing
 
complexity
 
reasoning
 
 
2
 
–
 
Partially
 
correct
 
solution,
 
basic
 
or
 
incomplete
 
analysis
 
 
3
 
–
 
Mostly
 
correct,
 
reasonable
 
testing,
 
correct
 
complexity
 
analysis
 
4
 
–
 
Clean,
 
correct,
 
well-tested
 
solution
 
with
 
strong
 
optimization
 
and
 
tradeof f
 
discussion
 
 
Notes:
 
She
 
knew
 
how
 
to
 
implement
 
the
 
code
 
and
 
how
 
it
 
worked.
 
4.
 
Team
 
Fit
 
&
 
Working
 
Style
 
(0–4)
 
 
Would
 
you
 
want
 
this
 
person
 
on
 
your
 
team
 
based
 
on
 
how
 
they
 
operate
 
under
 
pressure
 
and
 
uncertainty?
 
 
0
 
–
 
Actively
 
defensive,
 
dismissive,
 
or
 
hard
 
to
 
work
 
with
 
 
1
 
–
 
Friction-heavy ,
 
resistant
 
to
 
feedback
 
or
 
collaboration
 
 2
 
–
 
Neutral;
 
neither
 
adds
 
nor
 
detracts
 
 
3
 
–
 
Positive
 
teammate;
 
receptive,
 
steady ,
 
easy
 
to
 
work
 
with
 
 
4
 
–
 
Strong
 
team
 
asset;
 
calm
 
under
 
uncertainty ,
 
humble,
 
ownership
 
mindset
 
Notes:
 
Positive
 
and
 
knew
 
what
 
she
 
was
 
doing.
 
I
 
think
 
she
 
would
 
work
 
well
 
on
 
team.
 
Final
 
Evaluation
 
 
Total
 
Score:
 
_16__
 
/
 
16
 
 
Hiring
 
Recommendation
 
 
Strong
 
Hire
 
 
Hire
 
 
Lean
 
Hire
 
 
Lean
 
No
 
Hire
 
 
No
 
Hire
 
 
Strong
 
No
 
Hire
 
 
Final
 
Decision
 
 
Summarize
 
your
 
decision
 
in
 
3–5
 
sentences.
 
Focus
 
on:
 
 
●
 
Key
 
strengths
 
 
●
 
Key
 
weaknesses
 
 
●
 
Why
 
you
 
made
 
your
 
decision
 
 
Use
 
specific
 
examples
 
from
 
the
 
interview
 
to
 
support
 
your
 
decision.
 
 Interviewer
 
Grading
 
Guidelines
 
 
●
 
Completion
 
(are
 
all
 
sections
 
filled
 
out)?
 
 
○
 
40%
 
credit
 
 
●
 
Final
 
Decision
 
&
 
Justification
 
 
○
 
40%
 
credit
 
 
●
 
Per
 
section
 
–
 
Notes:
 
 
○
 
5%
 
credit
 
if
 
the
 
provided
 
notes
 
were
 
valuable
 
(bullets
 
or
 
sentences
 
with
 
specific
 
examples
 
citing
 
your
 
reasoning
 
for
 
the
 
ranking)
 
Candidate
 
 
As
 
the
 
candidate,
 
your
 
goal
 
is
 
to
 
✨
 
GET
 
A
 
JOB
 
✨
 
(survive
 
a
 
technical
 
interview).
 
You
 
will:
 
 
●
 
Solve
 
the
 
given
 
coding
 
problem
 
 
●
 
Aim
 
for
 
an
 
efficient
 
(ideally
 
optimal)
 
solution
 
 
●
 
Clearly
 
explain
 
your
 
thought
 
process
 
while
 
working
 
 
●
 
Communicate
 
tradeof fs,
 
ideas,
 
and
 
reasoning
 
out
 
loud
 
 
●
 
Respond
 
to
 
hints
 
or
 
feedback
 
from
 
the
 
interviewer
 
 
●
 
Write
 
and
 
submit
 
 
○
 
A
 
working
 
solution
 
 
○
 
A
 
short
 
writeup
 
explaining
 
the
 
time
 
complexity
 
of
 
your
 
solution
 
and
 
how
 
it
 
solves
 
the
 
problem.
 
 
For
 
fairness
 
to
 
our
 
less
 
experienced
 
students,
 
you
 
will
 
have
 
access
 
to
 
our
 
Python
 
cheat
 
sheet
 
during
 
the
 
exercise
 
(though
 
eventually
 
you’ll
 
need
 
to
 
be
 
able
 
to
 
take
 
interviews
 
without
 
this!)
 
 
You
 
will
 
be
 
graded
 
on
 
the
 
quality
 
of
 
your
 
submitted
 
code
 
and
 
your
 
problem-solving
 
approach.
 
You
 
will
 
not
 
be
 
graded
 
in
 
any
 
way
 
from
 
the
 
comments
 
or
 
report
 
submitted
 
by
 
the
 
interviewer .
 
You
 
may
 
code
 
on
 
paper ,
 
or
 
in
 
any
 
IDE/text
 
editor
 
that
 
does
 
NOT
 
have
 
AI
 or
 
autocomplete
 
(examples:
 
Vim,
 
notepad,
 
VsCode
 
without
 
Copilot)
 
 
I
 
think
 
the
 
interview
 
went
 
well.
 
I
 
was
 
able
 
to
 
identify
 
the
 
data
 
structure
 
that
 
had
 
to
 
be
 
used
 
and
 
how
 
to
 
implement
 
it.
 
Overall
 
I
 
think
 
it
 
went
 
well
 
but
 
I
 
also
 
think
 
I’ll
 
need
 
to
 
practice
 
more
 
to
 
really
 
get
 
down
 
all
 
of
 
the
 
possible
 
data
 
structures
 
that
 
could
 
be
 
asked
 
during
 
a
 
technical
 
interview .
 
def lengthOfLongestSubstring(s):
    left = 0
    maxlength = 0
    substring = set()

    for right in range(len(s)):
        while s[right] in substring:
            substring.remove(s[left])
            left+=1
        substring.add(s[right])
        maxlength = max(substring, right - left + 1)

    return maxlength

# Michael DiNapoli O(n^2)
```

</details>

---

#### Nicholas Friedlander (`67138`)

- **Problem:** Longest Substring Without Repeating Characters
- **Language:** python
- **Score:** 8/8 (PASS)
- **Grading status:** graded
- **Files:** CS102 PAIRED TECHNICAL INTERVIEW.txt (direct)

| Test Case | Result |
|-----------|--------|
| example1 | PASS |
| all_same | PASS |
| example3 | PASS |
| empty | PASS |
| single_char | PASS |
| all_unique | PASS |
| spaces | PASS |
| end_longest | PASS |

<details>
<summary>Edits made by grader</summary>

- [syntax-only] Lowered keyword 'If'
- [syntax-only] Replaced em/en dashes with hyphens
- [syntax-only] Added missing colons

</details>

<details>
<summary>Extracted Code (67138.py)</summary>

```python
# I would achieve this problem by doing a dynamic sliding window solution
# Set and left and right integer
# Go through the string and update a variable with the longest substring length being equal to the window size
# If a letter of the substring is repeated the window would shift to the right
# Time complexity of O(n)

def lengthOfLongestSubstring(s: str) -> int: 
    left = 0
    longestLength = 0
    substringSet = set()
    for right in range(len(s)): 
        while s[right] in substringSet 
            substringSet.remove(s[left])
            left += 1
        substringSet.add(s[right])

        if (right – left + 1 > longestLength):
            longestLength = right – left + 1

    return longestLength
```

</details>

<details>
<summary>Original Document (67138.txt)</summary>

```
Candidate Form

# I would achieve this problem by doing a dynamic sliding window solution
# Set and left and right integer
# Go through the string and update a variable with the longest substring length being equal to the window size
# If a letter of the substring is repeated the window would shift to the right
# Time complexity of O(n)

def lengthOfLongestSubstring(s: str) -> int: 
left = 0
longestLength = 0
substringSet = set()
for right in range(len(s)): 
	while s[right] in substringSet 
		substringSet.remove(s[left])
		left += 1
	substringSet.add(s[right])

	if (right – left + 1 > longestLength):
		longestLength = right – left + 1

return longestLength
```

</details>

---

#### Justin Gaston (`78797`)

- **Problem:** Longest Substring Without Repeating Characters
- **Language:** java
- **Score:** 1/8 (Critical Error)
- **Grading status:** graded
- **Repair level:** aggressive
- **Files:** MockInterview.txt (direct)

| Test Case | Result |
|-----------|--------|
| example1 | FAIL |
| all_same | FAIL |
| example3 | FAIL |
| empty | PASS |
| single_char | FAIL |
| all_unique | FAIL |
| spaces | FAIL |
| end_longest | FAIL |

<details>
<summary>Edits made by grader</summary>

- [syntax-only] Mechanical Java->Python transpile
- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def lengthOfLongestSubstring(s): return 0`

</details>

<details>
<summary>Extracted Code (78797.java)</summary>

```java
public int lengthOfLongestSubstring(String s){
    String final = 0;
    int maxLength = 0;
    HashSet <String> hashSet = new HashSet<>();
    for(int i = 0; i< s.length; i++){
        hashSet.add(s.charAt(i);
        while(hashSet.contains(s.charAt(i)){
            if(final.length > maxLength){
                maxLength = final.Length;
            }
            hashSet.remove();
        }
        
    }
    return final.length;
}

//I do not think that I implimented this properly at all
//However my thought process was this:
//Add letters to hasset until I encounter a duplicates
//then while the hashSet isn't empty, remove the letters from the 
//hashSet and add them to a string, and save that strings length
//then when the while loop is done clear out the string and repeat the process
//until the string is exhausted
```

</details>

<details>
<summary>Original Document (78797.txt)</summary>

```
My name: Justin Gaston
My Partners name: Kristen Lee

Candidate form: Longest Substring without duplicates

public int lengthOfLongestSubstring(String s){
	String final = 0;
	int maxLength = 0;
	HashSet <String> hashSet = new HashSet<>();
	for(int i = 0; i< s.length; i++){
		hashSet.add(s.charAt(i);
		while(hashSet.contains(s.charAt(i)){
			if(final.length > maxLength){
				maxLength = final.Length;
			}
			hashSet.remove();
		}
		
	}
	return final.length;
}

//I do not think that I implimented this properly at all
//However my thought process was this:
//Add letters to hasset until I encounter a duplicates
//then while the hashSet isn't empty, remove the letters from the 
//hashSet and add them to a string, and save that strings length
//then when the while loop is done clear out the string and repeat the process
//until the string is exhausted
```

</details>

---

#### Samuel Halsband (`68358`)

- **Problem:** Longest Substring Without Repeating Characters
- **Language:** python
- **Score:** 8/8 (PASS)
- **Grading status:** graded
- **Files:** CS102 PAIRED TECHNICAL INTERVIEW.txt (direct)

| Test Case | Result |
|-----------|--------|
| example1 | PASS |
| all_same | PASS |
| example3 | PASS |
| empty | PASS |
| single_char | PASS |
| all_unique | PASS |
| spaces | PASS |
| end_longest | PASS |

<details>
<summary>Extracted Code (68358.py)</summary>

```python
class Solution:
    def lengthOfLongestSubstring(self,s: str) -> int:
        maxLen = 0
        l = 0
        for r in range(0,len(s)):
            while (s[r] in s[l:r]):
                l+=1
            maxLen = max(maxLen,r-l+1)
        return maxLen
```

</details>

<details>
<summary>Original Document (68358.txt)</summary>

```
class Solution:
    def lengthOfLongestSubstring(self,s: str) -> int:
        maxLen = 0
        l = 0
        for r in range(0,len(s)):
            while (s[r] in s[l:r]):
                l+=1
            maxLen = max(maxLen,r-l+1)
        return maxLen
```

</details>

---

#### Jin Noh (`70971`)

- **Problem:** Longest Substring Without Repeating Characters
- **Language:** python
- **Score:** 1/8 (Critical Error)
- **Grading status:** graded
- **Repair level:** aggressive
- **Files:** Interview.txt (direct)

| Test Case | Result |
|-----------|--------|
| example1 | FAIL |
| all_same | FAIL |
| example3 | FAIL |
| empty | PASS |
| single_char | FAIL |
| all_unique | FAIL |
| spaces | FAIL |
| end_longest | FAIL |

<details>
<summary>Edits made by grader</summary>

- [syntax-only] Added missing colons
- [syntax-only] Appended 1 missing closing bracket(s)
- [ambiguous] Conservative re-indent: normalized indent levels to 4-space tiers
- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def lengthOfLongestSubstring(s): return 0`

</details>

<details>
<summary>Extracted Code (70971.py)</summary>

```python
def lengthOfLongestSubstring(s: str) -> int:

    maxString = 0

    duplicate = {}

    left = 0
    
    for right in range(len(s.str)):

        window_sum += s.str [r]

        while left < len(s.str)
            window_sum == s.str[left
            left += 1

        if (s.substring(i) != (s.subtring[i+1]):
            maxString =+ 1

        elif (s.subtring(i) == s.subtring[i+1]):
            maxString =+ 1
            
            return (maxString)
```

</details>

<details>
<summary>Original Document (70971.txt)</summary>

```
def lengthOfLongestSubstring(s: str) -> int:

	maxString = 0

	duplicate = {}

	left = 0
	
	for right in range(len(s.str)):

		window_sum += s.str [r]

		while left < len(s.str)
			window_sum == s.str[left
			left += 1

		if (s.substring(i) != (s.subtring[i+1]):
			maxString =+ 1

		elif (s.subtring(i) == s.subtring[i+1]):
			maxString =+ 1
			
			return (maxString)
```

</details>

---

#### Jake Steck (`69296`)

- **Problem:** Longest Substring Without Repeating Characters
- **Language:** python
- **Score:** 8/8 (PASS)
- **Grading status:** graded
- **Files:** CS102 PAIRED TECHNICAL INTERVIEW.txt (direct)

| Test Case | Result |
|-----------|--------|
| example1 | PASS |
| all_same | PASS |
| example3 | PASS |
| empty | PASS |
| single_char | PASS |
| all_unique | PASS |
| spaces | PASS |
| end_longest | PASS |

<details>
<summary>Extracted Code (69296.py)</summary>

```python
def lengthOfLongestSubstring(s: str) -> int:
    charSet = set()
    result = 0
    length = len(s)
    left = 0
    
    for right in range(length):
        while s[right] in charSet:
            charSet.remove(s[left])
            left += 1
        charSet.add(s[right])
        result = max(result, right - left + 1)
    return result
```

</details>

<details>
<summary>Original Document (69296.txt)</summary>

```
Jake Steck

Ryan Tsui

Interviewer Form

Merge Two Sorted Lists

1) Problem Understanding
	4

2) Communication & Collaboration
	4

3) Implementation & Technical Depth
	4
	
4) Team Fit & Working Style
	3

Final Evaluation
	15/16

Final Decision
	Strong Hire

Candidate Form

def lengthOfLongestSubstring(s: str) -> int:
    charSet = set()
    result = 0
    length = len(s)
    left = 0
    
    for right in range(length):
        while s[right] in charSet:
            charSet.remove(s[left])
            left += 1
        charSet.add(s[right])
        result = max(result, right - left + 1)
    return result
```

</details>

---

#### Treyson Thelusma (`79860`)

- **Problem:** Longest Substring Without Repeating Characters
- **Language:** python
- **Score:** 1/8 (Critical Error)
- **Grading status:** graded
- **Files:** longest_substring.py (direct)

| Test Case | Result |
|-----------|--------|
| example1 | FAIL |
| all_same | FAIL |
| example3 | FAIL |
| empty | PASS |
| single_char | FAIL |
| all_unique | FAIL |
| spaces | FAIL |
| end_longest | FAIL |

<details>
<summary>Extracted Code (79860.py)</summary>

```python
class Solution:
    def lengthOfLongestSubstring(s: str) -> int:
        max_length = 0
        length = 0
        seen = {}
        
        l = 0
        r = 0
        
        while r < len(s):
            if s[r] not in seen:
                seen[s[r]] = r    
                length = r - l + 1
                r += 1        
            else:
                max_length = max(max_length, length)
                l = seen[s[r]] + 1        
        return max_length
```

</details>

<details>
<summary>Original Document (79860.txt)</summary>

```
class Solution:
	def lengthOfLongestSubstring(s: str) -> int:
		max_length = 0
		length = 0
		seen = {}
		
		l = 0
		r = 0
		
		while r < len(s):
			if s[r] not in seen:
				seen[s[r]] = r	
				length = r - l + 1
				r += 1		
			else:
				max_length = max(max_length, length)
				l = seen[s[r]] + 1		
		return max_length
```

</details>

---

#### Dominic Vega (`66500`)

- **Problem:** Longest Substring Without Repeating Characters
- **Language:** python
- **Score:** 1/8 (Critical Error)
- **Grading status:** graded
- **Repair level:** aggressive
- **Files:** Dominic Vega - Candidate Form.txt (direct)

| Test Case | Result |
|-----------|--------|
| example1 | FAIL |
| all_same | FAIL |
| example3 | FAIL |
| empty | PASS |
| single_char | FAIL |
| all_unique | FAIL |
| spaces | FAIL |
| end_longest | FAIL |

<details>
<summary>Edits made by grader</summary>

- [syntax-only] Extracted function block from noisy file
- [ambiguous] Conservative re-indent: normalized indent levels to 4-space tiers
- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def lengthOfLongestSubstring(s): return 0`

</details>

<details>
<summary>Extracted Code (66500.py)</summary>

```python
# Dominic Vega

# Athulya Santhosh (Interviewer)

# Candidate Form

def lengthOfLongestSubstring(s: str) -> int:
    # init some variables
    letter_map = {}
    left_ptr = 0
    right_ptr = 0
    longest_sub = 0

    # empty string case
    if (str == ""): return 0

    # run through string, visiting each character once (O(n))
    for (right_ptr in range(len(str))):
        # what is the last time we saw this character? if it hasn't appeared, last_seen is None
        last_seen = letter_map.get(str[right_ptr])

        # if we've seen this character and the last time we saw it was in our window, adjust window
        if (last_seen != None and last_seen >= left_ptr):
            left_ptr = last_seen + 1
    
        # set the last time we've seen this letter to where it is right now
        letter_map[str[right_ptr]] = right_ptr
    
        # the longest substring is either what it currently is or the length of the current window
        longest_sub = max(longest_sub, right_ptr-left_ptr+1)

    #zhe returnne
    return longest_sub
```

</details>

<details>
<summary>Original Document (66500.txt)</summary>

```
# Dominic Vega

# Athulya Santhosh (Interviewer)

# Candidate Form

def lengthOfLongestSubstring(s: str) -> int:
	# init some variables
	letter_map = {}
	left_ptr = 0
	right_ptr = 0
	longest_sub = 0

	# empty string case
	if (str == ""): return 0

	# run through string, visiting each character once (O(n))
	for (right_ptr in range(len(str))):
		# what is the last time we saw this character? if it hasn't appeared, last_seen is None
		last_seen = letter_map.get(str[right_ptr])

		# if we've seen this character and the last time we saw it was in our window, adjust window
		if (last_seen != None and last_seen >= left_ptr):
			left_ptr = last_seen + 1
	
		# set the last time we've seen this letter to where it is right now
		letter_map[str[right_ptr]] = right_ptr
	
		# the longest substring is either what it currently is or the length of the current window
		longest_sub = max(longest_sub, right_ptr-left_ptr+1)

	#zhe returnne
	return longest_sub
```

</details>

---

#### Isabella Yang (`67686`)

- **Problem:** Longest Substring Without Repeating Characters
- **Language:** python
- **Score:** 8/8 (PASS)
- **Grading status:** graded
- **Files:** CS102 PAIRED TECHNICAL INTERVIEW.txt (direct)

| Test Case | Result |
|-----------|--------|
| example1 | PASS |
| all_same | PASS |
| example3 | PASS |
| empty | PASS |
| single_char | PASS |
| all_unique | PASS |
| spaces | PASS |
| end_longest | PASS |

<details>
<summary>Extracted Code (67686.py)</summary>

```python
def lengthOfLongestSubstring(s: str) -> int:
    left = maxLength = 0
    # right = 0
    stringSet = set()

    for right in range (len(s)):
        while s[right] in stringSet:
            stringSet.remove(s[left])
            left += 1

        stringSet.add(s[right])
        maxLength = max(maxLength, right - left + 1)

    return maxLength

# Approaching this problem using sliding window + set 
# The time complexity is O(n), even though there is a nested while loop, it's still in linear time since each character
# is added and removed at most once. The right pointer goes through everything and left goes through it n times
# The space complexity is O(min(n,k)) since  the memory usage depends on the smaller input of n, k
```

</details>

<details>
<summary>Original Document (67686.txt)</summary>

```
CS102 PAIRED TECHNICAL INTERVIEW

This is the template for what you are expected to submit for the CS102 PAIRED Technical Interview.
Please make sure you have your items in this order when you submit so the we can grade it easier🙏

Refer back to the Paired Technical Interview Print outs to the content you should submit.
In general, you should submit at least a number and some notes for the interviewer side, and your full code solution for the Candidate.

We encourage you to comment your code if you'd like!

Isabella Yang

Zeynep Sude Genc

Interviewer Form

Contains Duplicate II

1) Problem Understanding
	4

2) Communication & Collaboration
	4

3) Implementation & Technical Depth
	3

4) Team Fit & Working Style
	4

Final Evaluation
	15/16, Strong Hire

Final Decision
	I would hire this person! She is able to explain how to approach the solution and the process behind implementing it. Also super friendly!

Candidate Form

def lengthOfLongestSubstring(s: str) -> int:
    left = maxLength = 0
    # right = 0
    stringSet = set()

    for right in range (len(s)):
        while s[right] in stringSet:
            stringSet.remove(s[left])
            left += 1

        stringSet.add(s[right])
        maxLength = max(maxLength, right - left + 1)

    return maxLength

# Approaching this problem using sliding window + set 
# The time complexity is O(n), even though there is a nested while loop, it's still in linear time since each character
# is added and removed at most once. The right pointer goes through everything and left goes through it n times
# The space complexity is O(min(n,k)) since  the memory usage depends on the smaller input of n, k
```

</details>

---

#### Jiarong Zhang (`69558`)

- **Problem:** Longest Substring Without Repeating Characters
- **Language:** java
- **Score:** 1/8 (Critical Error)
- **Grading status:** graded
- **Repair level:** aggressive
- **Files:** CS102 PAIRED TECHNICAL INTERVIEW.txt (direct)

| Test Case | Result |
|-----------|--------|
| example1 | FAIL |
| all_same | FAIL |
| example3 | FAIL |
| empty | PASS |
| single_char | FAIL |
| all_unique | FAIL |
| spaces | FAIL |
| end_longest | FAIL |

<details>
<summary>Edits made by grader</summary>

- [syntax-only] Mechanical Java->Python transpile
- [syntax-only] Replaced || with or
- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Inserted `pass` into empty block at line 1
- [logic-affecting] Replaced unparseable code with stub `def lengthOfLongestSubstring(s): return 0`

</details>

<details>
<summary>Extracted Code (69558.java)</summary>

```java
if(s.length() == 0){
        return 0;    
    }
    int maxLen = 1;
    int currLen = 1;
    HashSet<Character> set = new HashSet<>();
    StringBuilder sb = new StringBuilder();
    for(int i = 0; i<s.length(); i++){
        char c = s.charAt(i);
        if(!set.contains(c)){
            sb.append(c);
            currLen++;
            set.add(c);
        }else{
            while(set.contains(c) || sb.length() > 0){
                char first = sb.charAt(0);
                set.remove(c);
            }
            currLen = 1;
            sb.append(c);
        }
        maxLen = Math.max(currLen, maxLen);
    }
    return maxLen;
```

</details>

<details>
<summary>Original Document (69558.txt)</summary>

```
CS102 PAIRED TECHNICAL INTERVIEW

This is the template for what you are expected to submit for the CS102 PAIRED Technical Interview.
Please make sure you have your items in this order when you submit so the we can grade it easier🙏

Refer back to the Paired Technical Interview Print outs to the content you should submit. The interviewer form & candidate reflection should be submitted on paper. The candidate code should be submitted with the format below:

We encourage you to comment your code if you'd like!

[Your Name]
Jiarong Zhang

[Your Partner's Name]
Gaven Chan

Interviewer Form

Candidate asked clarifying questions regarding the problem
Commented pseudocode before actually writing any code
Talked about his implementation and asked questions 
Asked questions whenever was stuck
Implementation was correct
	At first was not optimal but after some 

Candidate Form

[Insert Submitted Code]
if(s.length() == 0){
		return 0;	
	}
	int maxLen = 1;
	int currLen = 1;
	HashSet<Character> set = new HashSet<>();
	StringBuilder sb = new StringBuilder();
	for(int i = 0; i<s.length(); i++){
		char c = s.charAt(i);
		if(!set.contains(c)){
			sb.append(c);
			currLen++;
			set.add(c);
		}else{
			while(set.contains(c) || sb.length() > 0){
				char first = sb.charAt(0);
				set.remove(c);
			}
			currLen = 1;
			sb.append(c);
		}
		maxLen = Math.max(currLen, maxLen);
	}
	return maxLen;
```

</details>

---

#### Ryan Zhang (`75295`)

- **Problem:** Longest Substring Without Repeating Characters
- **Language:** python
- **Score:** 7/8 (Minor Error)
- **Grading status:** graded
- **Not optimal:** Nested loops instead of sliding window
- **Files:** CS102 PAIRED TECHNICAL INTERVIEW (1).txt (direct)

| Test Case | Result |
|-----------|--------|
| example1 | FAIL |
| all_same | PASS |
| example3 | PASS |
| empty | PASS |
| single_char | PASS |
| all_unique | PASS |
| spaces | PASS |
| end_longest | PASS |

<details>
<summary>Extracted Code (75295.py)</summary>

```python
def lengthOfLongestSubstring(s: str) -> int:
    chars = set()
    max = 0
    left = 0

    for i in range(len(s)):
        while s[i] in chars:
            chars.remove(s[left])
            left += 1
        chars.add(s[i])
        max = len(chars)
    return max

# I chose to create a hashset, which would only store unique characters in it. I defined a variable max for storing the max value, and left so that I could iterate through the string as sort of a sliding window. After iterating through everything, I returned the value stored in max. Should be O(n).
```

</details>

<details>
<summary>Original Document (75295.txt)</summary>

```
CS102 PAIRED TECHNICAL INTERVIEW

This is the template for what you are expected to submit for the CS102 PAIRED Technical Interview.
Please make sure you have your items in this order when you submit so the we can grade it easier🙏

Refer back to the Paired Technical Interview Print outs to the content you should submit.
In general, you should submit at least a number and some notes for the interviewer side, and your full code solution for the Candidate.

We encourage you to comment your code if you'd like!

Ryan Zhang

Tiffany Lin

Interviewer Form

Contains Duplicates

1) Problem Understanding
Score: 3
- Was slightly confused about the problem, asked for clarification about the test cases as a result
- otherwise was mostly able to understand what the problem was asking

2) Communication & Collaboration
Score: 3
- was very clear about her train of thought in approaching the problem
- was willing to cooperate in solving the problem very well

3) Implementation & Technical Depth
Score: 3
- solution was implemented very well, near identical to the sample code
- was able to identify the code as being O(n)
- needed a bit of nudging in the right direction

4) Team Fit & Working Style
Score: 3
- was willing to hear and accept feedback
- used feedback to guide her solution to the problem

Final Evaluation
Score: 12
Lean Hire

Final Decision
Candidate was able to think very logically about the problem, had a rough idea of how to approach the problem. However her initial interpretation of the problem was somewhat of a concern. This could be attributed to a slight oversight however, so overall it was fine. 

Candidate Form

def lengthOfLongestSubstring(s: str) -> int:
	chars = set()
	max = 0
	left = 0

	for i in range(len(s)):
		while s[i] in chars:
			chars.remove(s[left])
			left += 1
		chars.add(s[i])
		max = len(chars)
	return max

# I chose to create a hashset, which would only store unique characters in it. I defined a variable max for storing the max value, and left so that I could iterate through the string as sort of a sliding window. After iterating through everything, I returned the value stored in max. Should be O(n).
```

</details>

---

#### Christian Zuniga (`56934`)

- **Problem:** Longest Substring Without Repeating Characters
- **Language:** python
- **Score:** 1/8 (Critical Error)
- **Grading status:** graded
- **Repair level:** aggressive
- **Files:** CS102 PAIRED TECHNICAL INTERVIEW_FINAL.txt (direct)

| Test Case | Result |
|-----------|--------|
| example1 | FAIL |
| all_same | FAIL |
| example3 | FAIL |
| empty | PASS |
| single_char | FAIL |
| all_unique | FAIL |
| spaces | FAIL |
| end_longest | FAIL |

<details>
<summary>Edits made by grader</summary>

- [syntax-only] Replaced || with or
- [syntax-only] Added missing colons
- [syntax-only] Removed C-style braces
- [syntax-only] Extracted function block from noisy file
- [syntax-only] Appended 1 missing closing bracket(s)
- [ambiguous] Conservative re-indent: normalized indent levels to 4-space tiers
- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def lengthOfLongestSubstring(s): return 0`

</details>

<details>
<summary>Extracted Code (56934.py)</summary>

```python
class Solution:

    def lengthofLongestSubstring(s:str) -> int:
        counter = 0
        visited = {}

        for x in s:
            #Base Case
            if (len(s) < 0 || len(s) > 50000){
                        return 0
            }

            if(s{x] != visited):
                counter = counter + 1
                s[x] = visited #Add visited string to the dict.

        return counter
```

</details>

<details>
<summary>Original Document (56934.txt)</summary>

```
CS102 PAIRED TECHNICAL INTERVIEW

This is the template for what you are expected to submit for the CS102 PAIRED Technical Interview.
Please make sure you have your items in this order when you submit so the we can grade it easier🙏

Refer back to the Paired Technical Interview Print outs to the content you should submit. The interviewer form & candidate reflection should be submitted on paper. The candidate code should be submitted with the format below:

We encourage you to comment your code if you'd like!

Christian Zuniga

Kevin Yang

Candidate Form

class Solution:

    def lengthofLongestSubstring(s:str) -> int:
        counter = 0
        visited = {}

        for x in s:
            #Base Case
            if (len(s) < 0 || len(s) > 50000){
                        return 0
            }

            if(s{x] != visited):
                counter = counter + 1
                s[x] = visited #Add visited string to the dict.

        return counter
```

</details>

---

### Merge Two Sorted Lists

#### Alison Batz (`67454`)

- **Problem:** Merge Two Sorted Lists
- **Language:** python
- **Score:** 0/7 (Critical Error)
- **Grading status:** graded
- **Repair level:** aggressive
- **Files:** Python Mock-Interview.txt (direct)

| Test Case | Result |
|-----------|--------|
| example1 | FAIL |
| both_empty | FAIL |
| one_empty | FAIL |
| other_empty | FAIL |
| interleave | FAIL |
| all_same | FAIL |
| single_each | FAIL |

<details>
<summary>Edits made by grader</summary>

- [syntax-only] Fixed --> to ->
- [syntax-only] Fixed typo -> 'None'
- [syntax-only] Fixed typo -> 'True'
- [syntax-only] Removed C-style braces
- [ambiguous] Conservative re-indent: normalized indent levels to 4-space tiers
- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def mergeTwoLists(list1, list2): return 0`

</details>

<details>
<summary>Extracted Code (67454.py)</summary>

```python
def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode] -> Optional[ListNode]:


        #Compare the two linked lists -- starting with head

        #insert based on smaller to larger value 

        #Linked List will vary in size --> Nodes already set up


        #Special Cases: Both can be empty

        current1 = new_node()
        current1 = list1   #don't lose track of the head

        current2 = new_node()
        current2 = list2  #don't lose track of the second head 

        #Third List (result linked list)

        current3 = new_node()
        current3 = list3 #new list (currently empty)



        while (current1 != NULL and current2 != NULL){   #while both conditions are true 

                if current1.val > current2.val:  #current1 greater than current2

                current2.next = current1
                current3.next = current2
                #add to list3  

                elif current2.val < current1.val:  #current2 less than current1
                    current1.next = current2
                    current3.next = current1
                                    #add to list3 


        return list3
```

</details>

<details>
<summary>Original Document (67454.txt)</summary>

```
Python Mock-Interview



def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode] -> Optional[ListNode]:

	
	#Compare the two linked lists -- starting with head

	#insert based on smaller to larger value 

	#Linked List will vary in size --> Nodes already set up


	#Special Cases: Both can be empty

	current1 = new_node()
	current1 = list1   #don't lose track of the head

	current2 = new_node()
	current2 = list2  #don't lose track of the second head 

	#Third List (result linked list)

	current3 = new_node()
	current3 = list3 #new list (currently empty)

	

	while (current1 != NULL and current2 != NULL){   #while both conditions are true 
		
		if current1.val > current2.val:  #current1 greater than current2
			
		 current2.next = current1
		 current3.next = current2
		#add to list3  

		elif current2.val < current1.val:  #current2 less than current1
		  current1.next = current2
		  current3.next = current1
                  #add to list3 


	return list3
```

</details>

---

#### Stephania Calin (`68729`)

- **Problem:** Merge Two Sorted Lists
- **Language:** python
- **Score:** 7/7 (PASS)
- **Grading status:** graded
- **Files:** CS102 PAIRED TECHNICAL INTERVIEW.txt (direct)

| Test Case | Result |
|-----------|--------|
| example1 | PASS |
| both_empty | PASS |
| one_empty | PASS |
| other_empty | PASS |
| interleave | PASS |
| all_same | PASS |
| single_each | PASS |

<details>
<summary>Extracted Code (68729.py)</summary>

```python
def mergeTwoLists(list1, list2): 
    # changed the function parameters because its easier for me to follow
        dummy = ListNode(0)
        current = dummy
    
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        #now ill attach remaining list
        current.next = list1 if list1 else list2
    
        return dummy.next
```

</details>

<details>
<summary>Original Document (68729.txt)</summary>

```
CS102 PAIRED TECHNICAL INTERVIEW

This is the template for what you are expected to submit for the CS102 PAIRED Technical Interview.
Please make sure you have your items in this order when you submit so the we can grade it easier🙏

Refer back to the Paired Technical Interview Print outs to the content you should submit.
In general, you should submit at least a number and some notes for the interviewer side, and your full code solution for the Candidate.

We encourage you to comment your code if you'd like!

Stephania Calin

Naomi Sellam

Interviewer Form

[Problem Given] Reverse Polish Notation

1) Problem Understanding
3
Notes: While I did have to push Naomi in the right direction, she still understood it clearly with the help of examples. She understood the concept and the goal that was to be achieved by the end of the written code. She asked questions about the edge cases and any exceptions to ensure her code would be prepared for any input. I told her to be weary of the operators that don't work with the code.

2) Communication & Collaboration
4
Notes: Before she began coding, I asked her to walk me through what her thinking was. I found we both worked effectively where she would ask a question and I would give her an answer without giving away the whole problem and she immediately understood and communicated that well. While walking me through her thinking process, she attempted to match a pattern to this problem at first noticing that the operators act on the two most recently seen numbers which made her think of a stack with a LIFO queue. 

3) Implementation & Technical Depth
4
Notes: Her approach is to iterate through each token and if it's a number, to push it onto the stack. Or if it's an operator, to pop the top two values, apply the operation and push the result back. She demonstrated well versed leet code knowledge and concluded that the end the stack has only one value. She implemented her solution very well and it was clean and ran through all test cases successfully with strong optimization. She also traced through her code to make sure it worked and explained it to me line by line. She stated that the time complexity is O(N) because "one pass through the tokens, each push/pop is O(1)." The space complexity she stated was O(N) in the worst case. 

4) Team Fit & Working Style
4
Notes:
Based on this interview, I would want this person on my team because she demonstrated a calm and humble personality while also crushing the leet code and demonstrating her proficiency in it. She also seems to be a reliable candidate, showing up to the interview on time and quickly coding her program correctly too. 

Final Evaluation
Strong Hire 15/16

Final Decision
During the interview, Naomi demonstrated strong proficiency in rest of the answer on the paper.

Candidate Form

def mergeTwoLists(list1, list2): 
# changed the function parameters because its easier for me to follow
	dummy = ListNode(0)
	current = dummy
	
	while list1 and list2:
		if list1.val <= list2.val:
			current.next = list1
			list1 = list1.next
		else:
			current.next = list2
			list2 = list2.next
		current = current.next
	#now ill attach remaining list
	current.next = list1 if list1 else list2
	
	return dummy.next
```

</details>

---

#### Monica Gnajewski (`66827`)

- **Problem:** Merge Two Sorted Lists
- **Language:** python
- **Score:** 0/7 (Critical Error)
- **Grading status:** graded
- **Repair level:** aggressive
- **Files:** Mock Technical Interview MG.pdf (pdf)

| Test Case | Result |
|-----------|--------|
| example1 | FAIL |
| both_empty | FAIL |
| one_empty | FAIL |
| other_empty | FAIL |
| interleave | FAIL |
| all_same | FAIL |
| single_each | FAIL |

<details>
<summary>Edits made by grader</summary>

- [syntax-only] Fixed typo -> 'None'
- [syntax-only] Added missing colons
- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def mergeTwoLists(list1, list2): return 0`

</details>

<details>
<summary>Extracted Code (66827.py)</summary>

```python
mergeTwoLists(list1:
 
Optional[ListNode],
 
list2:
 
Optional[ListNode])
 
->
 
Optional[ListNode]:
 
 
newList
 
=
 
ListNode()
 
 
currNode
 
=
 
newList
  
 
while
 
list1
 
and
 
list2
 
!=
 
NULL:
 
 
 
if
 
list1.val
 
>
 
list2.val:
 
 
 
 
newList.next
 
=
 
list2
 
 
 
 
list2
 
=
 
list2.next
 
 
 
else:
 
 
 
 
newList.next
 
=
 
list1
 
 
 
 
list1
 
=
 
list1.next
 
 
 
 
currNode
 
=
 
currNode.next
 
 
 
 
if
 
list1:
 
 
 
 
currNode
 
=
 
list1.next
 
 
 
else:
 
 
 
 
currNode
 
=
 
list2.next
 
 
 
return
 
newList
```

</details>

<details>
<summary>Original Document (66827.txt)</summary>

```
CS102
 
PAIRED
 
TECHNICAL
 
INTERVIEW
 
 
Monica
 
Gnajewski
 
 
Giankyle
 
Vallarta
 
 
 
Interviewer
 
Form
 
 
Problem:
 
Evaluate
 
Reverse
 
Polish
 
Notation
 
 
1)
 
Problem
 
Understanding:
 
3/4
 
-
 
Understood
 
the
 
problem
 
well,
 
but
 
had
 
questions
 
about
 
the
 
input
 
format
 
-
 
Needed
 
hint
 
on
 
what
 
data
 
structure
 
to
 
use,
 
but
 
was
 
able
 
to
 
determine
 
he
 
needed
 
to
 
use
 
a
 
stack
 
 
-
 
Slight
 
confusion
 
on
 
which
 
element
 
to
 
pop
 
first
 
 
2)
 
Communication
 
&
 
Collaboration:
 
3/4
 
 
-
 
Communicated
 
about
 
his
 
thought
 
process
 
constantly,
 
making
 
it
 
easy
 
to
 
address
 
minor
 
errors
 
-
 
Receptive
 
to
 
hints
 
and
 
feedback
 
 
3)
 
Implementation
 
&
 
Technical
 
Depth:
 
3/4
 
-
 
Solution
 
was
 
mostly
 
correct,
 
aside
 
from
 
minor
 
errors
 
-
 
Forgot
 
the
 
final
 
else
 
statement
 
that
 
pushes
 
integers
 
onto
 
the
 
stack
 
 
4)
 
Team
 
Fit
 
&
 
Working
 
Style:
 
4/4
 
-
 
I
 
would
 
want
 
this
 
person
 
on
 
my
 
team
 
-
 
Although
 
there
 
were
 
errors,
 
he
 
was
 
very
 
receptive
 
to
 
feedback
 
and
 
remained
 
calm
 
-
 
He
 
asked
 
many
 
clarifying
 
questions
 
about
 
syntax
 
 
Final
 
Evaluation:
 
 
-
 
Lean
 
Hire
 
-
 
13/16
 
 
Final
 
Decision
 
-
 
I
 
would
 
consider
 
hiring
 
this
 
person.
 
They
 
seem
 
to
 
have
 
a
 
good
 
understanding
 
of
 
how
 
to
 
solve
 
problems
 
and
 
are
 
receptive
 
to
 
feedback.
 
He
 
may
 
need
 
to
 
brush
 
up
 
on
 
Python
 
syntax
 
and
 
data
 
structures
 
a
 
bit
 
more.
 
 
Candidate
 
Form
 
 
def
 
mergeTwoLists(list1:
 
Optional[ListNode],
 
list2:
 
Optional[ListNode])
 
->
 
Optional[ListNode]:
 
 
newList
 
=
 
ListNode()
 
 
currNode
 
=
 
newList
  
 
while
 
list1
 
and
 
list2
 
!=
 
NULL:
 
 
 
if
 
list1.val
 
>
 
list2.val:
 
 
 
 
newList.next
 
=
 
list2
 
 
 
 
list2
 
=
 
list2.next
 
 
 
else:
 
 
 
 
newList.next
 
=
 
list1
 
 
 
 
list1
 
=
 
list1.next
 
 
 
 
currNode
 
=
 
currNode.next
 
 
 
 
if
 
list1:
 
 
 
 
currNode
 
=
 
list1.next
 
 
 
else:
 
 
 
 
currNode
 
=
 
list2.next
 
 
 
return
 
newList
```

</details>

---

#### Varun Karamchandani (`74406`)

- **Problem:** Merge Two Sorted Lists
- **Language:** python
- **Score:** 0/7 (Critical Error)
- **Grading status:** graded
- **Files:** CS102 PAIRED TECHNICAL INTERVIEW.txt (direct)

| Test Case | Result |
|-----------|--------|
| example1 | FAIL |
| both_empty | FAIL |
| one_empty | FAIL |
| other_empty | FAIL |
| interleave | FAIL |
| all_same | FAIL |
| single_each | FAIL |

<details>
<summary>Extracted Code (74406.py)</summary>

```python
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def mergeTwoLists(list1, list2):
    dummy = ListNode(0)
    current = dummy
    
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    # attach whatever is left
    if list1:
        current.next = list1
    else:
        current.next = list2
    
    return dummy.next
```

</details>

<details>
<summary>Original Document (74406.txt)</summary>

```
CS102 PAIRED TECHNICAL INTERVIEW

Varun Kumar Karamchandani

Kushagra Singh

Interviewer Form
Evaluate Reverse Polish Notation

1. Problem Understanding: Identified stack as correct structure immediately 
Recognized operand ordering issue for - and / without hints
rating: 4

2.Communication & Collaboration: Explained approach clearly before writing code
Minimal guidance needed throughout
rating: 3

3.Implementation & Technical Depth: Handled all 4 operators correctly including division truncation
Stated O(n) time and O(n) space accurately
rating: 4

4.Team Fit & Working Style: Calm and composed under pressure
Organized thought process with no major missteps
rating: 4

Final Evaluation: Clean correct solution with strong communication

Final Decision: Hire

Candidate Form

merge 2 list

python

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def mergeTwoLists(list1, list2):
    dummy = ListNode(0)
    current = dummy
    
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    # attach whatever is left
    if list1:
        current.next = list1
    else:
        current.next = list2
    
    return dummy.next
```

</details>

---

#### Zhi Xiong Lu (`79884`)

- **Problem:** Merge Two Sorted Lists
- **Language:** python
- **Score:** 7/7 (PASS)
- **Grading status:** graded
- **Files:** CS102 PAIRED TECHNICAL INTERVIEW.txt (direct)

| Test Case | Result |
|-----------|--------|
| example1 | PASS |
| both_empty | PASS |
| one_empty | PASS |
| other_empty | PASS |
| interleave | PASS |
| all_same | PASS |
| single_each | PASS |

<details>
<summary>Extracted Code (79884.py)</summary>

```python
def mergeTwoLists(self, list1, list2):
        list3 = ListNode(0)
        current = list3

        while list1 and list2:
            
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
                
            else:
                current.next = list2
                list2 = list2.next
                
            current = current.next
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        return list3.next
```

</details>

<details>
<summary>Original Document (79884.txt)</summary>

```
CS102 PAIRED TECHNICAL INTERVIEW

This is the template for what you are expected to submit for the CS102 PAIRED Technical Interview.
Please make sure you have your items in this order when you submit so the we can grade it easier🙏

Refer back to the Paired Technical Interview Print outs to the content you should submit.
In general, you should submit at least a number and some notes for the interviewer side, and your full code solution for the Candidate.

We encourage you to comment your code if you'd like!

Zhi Xiong Lu

Park RPK

Interviewer Form

Merge Two Sorted Lists

1) Problem Understanding

Clarified what the program should do and what output should be. Asked clarifying question on it about number of guesses being returned. Demonstrated understanding of problems and restated in own words.

2) Communication & Collaboration

Offered an initial brute force solution, where value from 1-100 is checked. They clarified time complexity was o(n) time,w when asked if there was a more effective/efficient method they offered the binary search where the complexity is olog(n). Interviewee was able to explain both 

3) Implementation & Technical Depth

Startec clariying methods explained basic binary algorithm, and talked about what the code was doing as he programed solution walked through his code with example value while coding. Required a bit of prompting about position requirement and expect as program was running -1,0,1. Note theis was the most efficient method and reiterated olog(n) time complexity

4) Team Fit & Working Style

Candidate was receptive and integrated feedback. Persistent in trying and understanding cooperatively despite initial blip in communication at the start.

Final Evaluation

15/16

Final Decision

Strong hire

Candidate Form

The problem that was asked of me was 

Merge Two Sorted Lists

def mergeTwoLists(self, list1, list2):
        list3 = ListNode(0)
        current = list3

        while list1 and list2:
            
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
                
            else:
                current.next = list2
                list2 = list2.next
                
            current = current.next
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        return list3.next
```

</details>

---

#### Vikram Minhas (`70844`)

- **Problem:** Merge Two Sorted Lists
- **Language:** python
- **Score:** 1/7 (Critical Error)
- **Grading status:** graded
- **Files:** mockInterview.txt (direct)

| Test Case | Result |
|-----------|--------|
| example1 | FAIL |
| both_empty | FAIL |
| one_empty | PASS |
| other_empty | FAIL |
| interleave | FAIL |
| all_same | FAIL |
| single_each | FAIL |

<details>
<summary>Edits made by grader</summary>

- [syntax-only] Fixed typo -> 'None'
- [syntax-only] Extracted function block from noisy file

</details>

<details>
<summary>Extracted Code (70844.py)</summary>

```python
Time complexity of my problem: O(n+m)
My solution goes through each of the lists completely and since the lists aren't identical, we have list1 of length n and list2 of length m. We compare each of the values and then go through until no more left to search and then return the head. We choose the head of the list that has a bigger value and then we move the pointer and keep repeating until the comparison is done. 


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> optional[ListNode]:
    x = listNode()
    curr = x

    while list1 and list2 != null:
        if list1.val <= list2.val:
            curr.next = list1
            list1 = list1.next
        elif list1.val >= list2.val:
            curr.next = list2
            list2 = list2.next
        curr = curr.next

    return x
```

</details>

<details>
<summary>Original Document (70844.txt)</summary>

```
Vikram Minhas

Sean Carhart

Interviewer Form

Evaluate Reverse Polish notation

1) Problem Understanding
4

2) Communication & Collaboration
4
- clearly explained how each of the examples worked and how it should implemented 

3) Implementation & Technical Depth
4
- explained each part of their code as they wrote it

4) Team Fit & Working Style
4
- knew what they were doing and confident, would love to have on team

Final Evaluation
16/16
Strong hire

Final Decision
Understood the assignment right away, explained what the problem was asking clearly to me. Made sure to go through how each of the examples given to them worked and why the output was what it was. Wrote clear code with proper syntax and very clear on why he wrote what he wrote. 

Candidate Form
PROBLEM: Merge Two Sorted Lists
Time complexity of my problem: O(n+m)
My solution goes through each of the lists completely and since the lists aren't identical, we have list1 of length n and list2 of length m. We compare each of the values and then go through until no more left to search and then return the head. We choose the head of the list that has a bigger value and then we move the pointer and keep repeating until the comparison is done. 


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> optional[ListNode]:
	x = listNode()
	curr = x

	while list1 and list2 != null:
		if list1.val <= list2.val:
			curr.next = list1
			list1 = list1.next
		elif list1.val >= list2.val:
			curr.next = list2
			list2 = list2.next
		curr = curr.next

	return x
```

</details>

---

#### Kenneth Ng (`75928`)

- **Problem:** Merge Two Sorted Lists
- **Language:** java
- **Score:** 0/7 (Critical Error)
- **Grading status:** graded
- **Repair level:** aggressive
- **Files:** CS102 PAIRED TECHNICAL INTERVIEW.txt (direct)

| Test Case | Result |
|-----------|--------|
| example1 | FAIL |
| both_empty | FAIL |
| one_empty | FAIL |
| other_empty | FAIL |
| interleave | FAIL |
| all_same | FAIL |
| single_each | FAIL |

<details>
<summary>Edits made by grader</summary>

- [syntax-only] Mechanical Java->Python transpile
- [syntax-only] Fixed typo -> 'None'
- [syntax-only] Replaced && with and
- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def mergeTwoLists(list1, list2): return 0`

</details>

<details>
<summary>Extracted Code (75928.java)</summary>

```java
public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode head = new ListNode();
        ListNode current = head;

        while (list1 != null && list2 != null) {
                if (list1.value <= list2.value) {
                    current.next = list1;
                    list1 = list1.next;
                } else {
                    current.next = list2;
                    list2 = list2.next;
                }

                current = current.next;
        }
        current.next = list1 != null ? list1 : list2;

        return head.next;
}
```

</details>

<details>
<summary>Original Document (75928.txt)</summary>

```
CS102 PAIRED TECHNICAL INTERVIEW

This is the template for what you are expected to submit for the CS102 PAIRED Technical Interview.
Please make sure you have your items in this order when you submit so the we can grade it easier🙏

Refer back to the Paired Technical Interview Print outs to the content you should submit.
In general, you should submit at least a number and some notes for the interviewer side, and your full code solution for the Candidate.

We encourage you to comment your code if you'd like!

[Your Name] Kenneth Ng

[Your Partner's Name] Qianjun Ryan Zhou

Interviewer Form

[Problem Given] Guess Number Higher or Lower

1) Problem Understanding - 3
- understood the premise of the problem and identified the appropriate strategy
- needed small hints to fix binary search implementation details

2) Communication & Collaboration - 4
- ran through how the first loop of the binary search would work
- explained what all pseudocode did and why they were necessary
- asked about the input constraints

3) Implementation & Technical Depth - 4
- ran through simulated test cases verbally
- optimized the number of declarations of midpoint variable after discussion
- correctly identified time and space complexity

4) Team Fit & Working Style - 4
- very good at communicating ideas
- can implement ideas quickly
- calmly went through all steps and explained all relevant details

Final Evaluation
15/16 - Strong Hire

Final Decision
This candidate works well under pressure and can explain ideas clearly and calmly. However, he did need some hints to get him on track initially, but not a deal-breaker. Overall, clear-headed and good at explaining thought process.

Candidate Form

[Problem Given] Merge Two Sorted Lists

public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
    ListNode head = new ListNode();
    ListNode current = head;
  
    while (list1 != null && list2 != null) {
        if (list1.value <= list2.value) {
          current.next = list1;
          list1 = list1.next;
        } else {
          current.next = list2;
          list2 = list2.next;
        }
      
        current = current.next;
    }
    current.next = list1 != null ? list1 : list2;

    return head.next;
}
```

</details>

---

#### Ian Porto (`78282`)

- **Problem:** Merge Two Sorted Lists
- **Language:** python
- **Score:** 1/7 (Critical Error)
- **Grading status:** graded
- **Files:** done.txt (direct)

| Test Case | Result |
|-----------|--------|
| example1 | FAIL |
| both_empty | FAIL |
| one_empty | FAIL |
| other_empty | PASS |
| interleave | FAIL |
| all_same | FAIL |
| single_each | FAIL |

<details>
<summary>Extracted Code (78282.py)</summary>

```python
def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    #Initialize two nodes to step through list 1 and list 2
    cur1 = list1
    cur2 = list2


    #loop through list 1
    i = 0
    while cur1:
        i += 1 

        #Check to see if we have completed list2 or list1 is larger then just insert the next value of list1
        if (cur2 == None) or (cur1.next.val < cur2.val):

            #if current value is first then set the head
            if i == 1:
                head = cur1
            cur1 = cur1.next

        #insert next value of list2 into list1
        else:
            temp = cur2
            cur2.next = cur1.next
            cur1.next = cur2

            #if current value is first then set the head
            if i == 1:
                head = cur1

            cur2 = temp.next
            cur1 = cur1.next
    
    #if list1 ends before list2 then add list2 to the end
    if (cur2 != None):
        cur1.next = cur2

    return head
```

</details>

<details>
<summary>Original Document (78282.txt)</summary>

```
Ian Porto

Matthew Park

Candidate Form

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
	#Initialize two nodes to step through list 1 and list 2
	cur1 = list1
	cur2 = list2


	#loop through list 1
	i = 0
	while cur1:
		i += 1 

		#Check to see if we have completed list2 or list1 is larger then just insert the next value of list1
		if (cur2 == None) or (cur1.next.val < cur2.val):

			#if current value is first then set the head
			if i == 1:
				head = cur1
			cur1 = cur1.next

		#insert next value of list2 into list1
		else:
			temp = cur2
			cur2.next = cur1.next
			cur1.next = cur2

			#if current value is first then set the head
			if i == 1:
				head = cur1

			cur2 = temp.next
			cur1 = cur1.next
	
	#if list1 ends before list2 then add list2 to the end
	if (cur2 != None):
		cur1.next = cur2

	return head
```

</details>

---

#### Athulya Santhosh (`77421`)

- **Problem:** Merge Two Sorted Lists
- **Language:** python
- **Score:** 3/7 (Critical Error)
- **Grading status:** graded
- **Files:** Merge Two Sorted Lists.txt (direct)

| Test Case | Result |
|-----------|--------|
| example1 | FAIL |
| both_empty | PASS |
| one_empty | PASS |
| other_empty | PASS |
| interleave | FAIL |
| all_same | FAIL |
| single_each | FAIL |

<details>
<summary>Extracted Code (77421.py)</summary>

```python
def mergeTwoList(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    curr1 = list1
    curr2 = list2
    if list1 == None and list2 == None:
        return None
    elif list1 == None:
        return list2
    elif list2 == None:
        return list1
    while curr1 and curr2:
        if curr1.val <= curr2.val and curr1.next == None:
            curr1.next = curr2
            curr2 = curr2.next
        if curr1.val <= curr2.val and curr1.next != None and curr2.val < curr1.next.val:
            temp = curr1.next
            curr1.next = curr2
            curr2 = curr2.next
            curr1.next.next = temp
        curr1 = curr1.next
    return list1
```

</details>

<details>
<summary>Original Document (77421.txt)</summary>

```
def mergeTwoList(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
	curr1 = list1
	curr2 = list2
	if list1 == None and list2 == None:
		return None
	elif list1 == None:
		return list2
	elif list2 == None:
		return list1
	while curr1 and curr2:
		if curr1.val <= curr2.val and curr1.next == None:
			curr1.next = curr2
			curr2 = curr2.next
		if curr1.val <= curr2.val and curr1.next != None and curr2.val < curr1.next.val:
			temp = curr1.next
			curr1.next = curr2
			curr2 = curr2.next
			curr1.next.next = temp
		curr1 = curr1.next
	return list1
```

</details>

---

#### Kathryn Schauber (`75705`)

- **Problem:** Merge Two Sorted Lists
- **Language:** python
- **Score:** 3/7 (Critical Error)
- **Grading status:** graded
- **Files:** Interviewing notes (no-ext); techinterview.py (direct)

| Test Case | Result |
|-----------|--------|
| example1 | FAIL |
| both_empty | PASS |
| one_empty | PASS |
| other_empty | PASS |
| interleave | FAIL |
| all_same | FAIL |
| single_each | FAIL |

<details>
<summary>Edits made by grader</summary>

- [syntax-only] Extracted function block from noisy file

</details>

<details>
<summary>Extracted Code (75705.py)</summary>

```python
Date: 5/6/26
Problem Given: Contains Duplicate Interviewer

Problem Understanding: Partial understanding, some clarification needed
Notes: took a long time to realize i and j were indices

Communication and Collaberation: Very Unclear, stuggled with feedback
Notes: when I asked her to explain why she was doing what she was doing, she would say she didn't know, when she finally did tho, she realized what she was doing wrong, and fixed Interviewer

Implementation and Technical Depth: Mostly correct, reasonable testing, correct complexity analysis
Notes: correct code. did not trace through super throughly. Correct time complexity analysis

Team fit and working style: Friction-heavy, resistant to feedback or collaboration
Notes: kept trying to hint towards hashmap, eventually she figured out it was a hashmap, but was resistant to switching to hashmap and sticking to a two pointer approach. did eventually switch to hashmap

Hiring Recommendation: No hire
Key strenghts was once she switched to hashmap she completed the solution quickly. Key weakness was communication and collaberation, was very resistant. I made my decision because of the communication.
def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    #will be ediiting list 1
    #head = list1
    #prev = temp value

    #while list2:
            #if val2 is than val1, set the next node to be the node in list1, update previous or head value if necessesary

    if not list1 and not list2:
            return None
    if not list1:
            return list2
    if not list2:
            return list1

    head = list1            #1 - 2- 4
    prev = None

    while list2 and list1:       
            if list2.val <= list1.val:               
                list2.next = list1                
                if prev is None:
                    head = list2                #1 -1 -2- 4
                    prev = list2
                else:
                    prev.next = list2
                    prev = prev.next
                    list2 = list2.next
            else:
                list1 = list1.next
                prev = prev.next


    while list2:
            prev.next = list2
            prev = prev.next

    return head



# The time complexity of my code is O(n) because it iterates through each loop at least once, say the length of list1 is n an list2 is m the time complexity would be O(n + m) which is the same as linear time and 0(n)
# The space complexity of my code is O(1) because no new objects are created therefore constant space is used
# My solution is a two pointer solution that updates list one based on the value of list2. if the value of list2 is less than or equal 2 my code updates the previous node to point to the list2 node and the list2 node points to the current list1 pointer. the list2 pointer is moved forward
# if list2 value is greater than the list 1 pointer the list 1 pointer is moved forward and the prev node is updated.
# basically it insterts the list2 nodes in the correct spot of list1

# My interviewer guided me a little with edge cases and other small errors, did not feel antagonized.
```

</details>

<details>
<summary>Original Document (75705.txt)</summary>

```
Candidate Name: Maddie Broderick
Interviewer Name: 
Date: 5/6/26
Problem Given: Contains Duplicate Interviewer

Problem Understanding: Partial understanding, some clarification needed
Notes: took a long time to realize i and j were indices

Communication and Collaberation: Very Unclear, stuggled with feedback
Notes: when I asked her to explain why she was doing what she was doing, she would say she didn't know, when she finally did tho, she realized what she was doing wrong, and fixed Interviewer

Implementation and Technical Depth: Mostly correct, reasonable testing, correct complexity analysis
Notes: correct code. did not trace through super throughly. Correct time complexity analysis

Team fit and working style: Friction-heavy, resistant to feedback or collaboration
Notes: kept trying to hint towards hashmap, eventually she figured out it was a hashmap, but was resistant to switching to hashmap and sticking to a two pointer approach. did eventually switch to hashmap

Hiring Recommendation: No hire
Key strenghts was once she switched to hashmap she completed the solution quickly. Key weakness was communication and collaberation, was very resistant. I made my decision because of the communication.
def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    #will be ediiting list 1
    #head = list1
    #prev = temp value

    #while list2:
        #if val2 is than val1, set the next node to be the node in list1, update previous or head value if necessesary

    if not list1 and not list2:
        return None
    if not list1:
        return list2
    if not list2:
        return list1
    
    head = list1            #1 - 2- 4
    prev = None

    while list2 and list1:       
        if list2.val <= list1.val:               
            list2.next = list1                
            if prev is None:
                head = list2                #1 -1 -2- 4
                prev = list2
            else:
                prev.next = list2
                prev = prev.next
                list2 = list2.next
        else:
            list1 = list1.next
            prev = prev.next
    

    while list2:
        prev.next = list2
        prev = prev.next

    return head



 # The time complexity of my code is O(n) because it iterates through each loop at least once, say the length of list1 is n an list2 is m the time complexity would be O(n + m) which is the same as linear time and 0(n)
 # The space complexity of my code is O(1) because no new objects are created therefore constant space is used
 # My solution is a two pointer solution that updates list one based on the value of list2. if the value of list2 is less than or equal 2 my code updates the previous node to point to the list2 node and the list2 node points to the current list1 pointer. the list2 pointer is moved forward
 # if list2 value is greater than the list 1 pointer the list 1 pointer is moved forward and the prev node is updated.
 # basically it insterts the list2 nodes in the correct spot of list1

 # My interviewer guided me a little with edge cases and other small errors, did not feel antagonized.
```

</details>

---

#### Ryan Tsui (`69792`)

- **Problem:** Merge Two Sorted Lists
- **Language:** python
- **Score:** 7/7 (PASS)
- **Grading status:** graded
- **Files:** CS102 PAIRED TECHNICAL INTERVIEW (1).txt (direct)

| Test Case | Result |
|-----------|--------|
| example1 | PASS |
| both_empty | PASS |
| one_empty | PASS |
| other_empty | PASS |
| interleave | PASS |
| all_same | PASS |
| single_each | PASS |

<details>
<summary>Edits made by grader</summary>

- [syntax-only] Lowered keyword 'Return'

</details>

<details>
<summary>Extracted Code (69792.py)</summary>

```python
def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    #base cases so if these are none, I can just return the other list and save memory
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    #if the value of list1 is less than or equal to list 2, recursively call the function
    #Set list1.next to the merged result of the remaining nodes.
    #Return list1 as the current head.
    if list1.val <= list2.val:
        list1.next = self.mergeTwoLists(list1.next, list2)
        return list1
    #do the same with list2
    else: 
        list2.next = self.mergeTwoLists(list2.next, list1)
        return list2
```

</details>

<details>
<summary>Original Document (69792.txt)</summary>

```
CS102 PAIRED TECHNICAL INTERVIEW

This is the template for what you are expected to submit for the CS102 PAIRED Technical Interview.
Please make sure you have your items in this order when you submit so the we can grade it easier🙏

Refer back to the Paired Technical Interview Print outs to the content you should submit.
In general, you should submit at least a number and some notes for the interviewer side, and your full code solution for the Candidate.

We encourage you to comment your code if you'd like!

Ryan Tsui

Jake Steck

Interviewer Form

Longest Substring without Repeating Characters

1) Problem Understanding
3

2) Communication & Collaboration
4

3) Implementation & Technical Depth
4

4) Team Fit & Working Style
4

Final Evaluation
15/16

Final Decision
Hire

Candidate Form

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    #base cases so if these are none, I can just return the other list and save memory
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    #if the value of list1 is less than or equal to list 2, recursively call the function
    #Set list1.next to the merged result of the remaining nodes.
    #Return list1 as the current head.
    if list1.val <= list2.val:
        list1.next = self.mergeTwoLists(list1.next, list2)
        return list1
    #do the same with list2
    else: 
        list2.next = self.mergeTwoLists(list2.next, list1)
        return list2
```

</details>

---

#### Gabriel Yang (`79975`)

- **Problem:** Merge Two Sorted Lists
- **Language:** python
- **Score:** 1/7 (Critical Error)
- **Grading status:** graded
- **Files:** coding_102_solution.txt (direct)

| Test Case | Result |
|-----------|--------|
| example1 | FAIL |
| both_empty | PASS |
| one_empty | FAIL |
| other_empty | FAIL |
| interleave | FAIL |
| all_same | FAIL |
| single_each | FAIL |

<details>
<summary>Edits made by grader</summary>

- [syntax-only] Lowered keyword 'If'

</details>

<details>
<summary>Extracted Code (79975.py)</summary>

```python
def mergeTwoLists(list1, list2):
    dummy = ListNode()

    curr = dummy
    while list1 or list2:
        if list1.val <= list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next

    if list1:
        curr.next = list1
    elif list2:
        curr.next = list2

    return dummy.next

#Iterates through both list nodes until one of them is empty, adding the lesser nodes to the new head node. If one is empty, just  #append the non-empty list onto the end of the new head.
```

</details>

<details>
<summary>Original Document (79975.txt)</summary>

```
def mergeTwoLists(list1, list2):
    dummy = ListNode()

    curr = dummy
    while list1 or list2:
        if list1.val <= list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next

    if list1:
        curr.next = list1
    elif list2:
        curr.next = list2

    return dummy.next

#Iterates through both list nodes until one of them is empty, adding the lesser nodes to the new head node. If one is empty, just  #append the non-empty list onto the end of the new head.
```

</details>

---

#### Justin Yu (`78968`)

- **Problem:** Merge Two Sorted Lists
- **Language:** python
- **Score:** 0/7 (Critical Error)
- **Grading status:** graded
- **Repair level:** aggressive
- **Files:** Quiz 3 Interview.ipynb (ipynb)

| Test Case | Result |
|-----------|--------|
| example1 | FAIL |
| both_empty | FAIL |
| one_empty | FAIL |
| other_empty | FAIL |
| interleave | FAIL |
| all_same | FAIL |
| single_each | FAIL |

<details>
<summary>Edits made by grader</summary>

- [syntax-only] Extracted function block from noisy file
- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def mergeTwoLists(list1, list2): return 0`

</details>

<details>
<summary>Extracted Code (78968.py)</summary>

```python
# Time complexity O(n)

def mergeTwoList(list1, list2)
    my_node = None
    while list1.next != None and list2.next != None:
        if list1.val > list2.val:
            my_node.next = list1
            list1 = list1.next
            if list1 = None:
                my_node = list2.next
        else:
            my_node.next = list2
            list2 = list2.next
    return my_node
```

</details>

<details>
<summary>Original Document (78968.txt)</summary>

```
# Time complexity O(n)

def mergeTwoList(list1, list2)
    my_node = None
    while list1.next != None and list2.next != None:
        if list1.val > list2.val:
            my_node.next = list1
            list1 = list1.next
            if list1 = None:
                my_node = list2.next
        else:
            my_node.next = list2
            list2 = list2.next
    return my_node
```

</details>

---

#### Vincent Zheng (`79930`)

- **Problem:** Merge Two Sorted Lists
- **Language:** pseudocode
- **Score:** 0/7 (Critical Error)
- **Grading status:** graded
- **Repair level:** aggressive
- **Files:** vincent technical interview.txt (direct)

| Test Case | Result |
|-----------|--------|
| example1 | FAIL |
| both_empty | FAIL |
| one_empty | FAIL |
| other_empty | FAIL |
| interleave | FAIL |
| all_same | FAIL |
| single_each | FAIL |

<details>
<summary>Edits made by grader</summary>

- [syntax-only] Fixed typo -> 'None'
- [syntax-only] Removed trailing semicolons
- [syntax-only] Added missing colons
- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def mergeTwoLists(list1, list2): return 0`

</details>

<details>
<summary>Extracted Code (79930.py)</summary>

```python
def ListNode
mergeTwoList(ListNode list1, ListNode list2)


ListNode das = new LlistNode(
cur = das



while list1 and list2 not null:
list1.val
list2.val

if list1.val > list2.val
    current = list1.val;
```

</details>

<details>
<summary>Original Document (79930.txt)</summary>

```
def ListNode
mergeTwoList(ListNode list1, ListNode list2)


ListNode das = new LlistNode(
cur = das



while list1 and list2 not null:
list1.val
list2.val

if list1.val > list2.val
	current = list1.val;
```

</details>

---

### unknown

#### Kristen Lee (`68745`)

- **Problem:** unknown
- **Language:** pseudocode
- **Extraction status:** extracted
- **Files:** CS102QUIZ3.doc (doc)

*No code extracted.*

*No raw document available.*

---

#### Noel Maldonado (`70003`)

- **Problem:** unknown
- **Language:** empty
- **Extraction status:** manual-review
- **Files:** IMG_5859.jpeg (image); IMG_5860.jpeg (image); IMG_5861.jpeg (image); IMG_5862.jpeg (image)

*No code extracted.*

*No raw document available.*

---

#### Ryan Martin (`77206`)

- **Problem:** unknown
- **Language:** pseudocode
- **Extraction status:** empty
- **Files:** CS102 PAIRED TECHNICAL INTERVIEW.txt (direct)

*No code extracted.*

*No raw document available.*

---

#### Xinlin Wu (`69542`)

- **Problem:** unknown
- **Language:** empty
- **Extraction status:** manual-review
- **Files:** IMG_4908.JPG (image); IMG_4909.JPG (image); IMG_4910.JPG (image); IMG_4911.JPG (image)

*No code extracted.*

*No raw document available.*

---

#### Elaine Zou (`66867`)

- **Problem:** unknown
- **Language:** pseudocode
- **Extraction status:** extracted
- **Files:** MockTechnical.doc (doc)

*No code extracted.*

*No raw document available.*

---
