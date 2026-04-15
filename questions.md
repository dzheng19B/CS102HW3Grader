As discussed in class, if you’re looking to land a software engineering internship/job at a big tech company, you will need to reliably solve technical interview problems. Not allocating time for this preparation is one of the single biggest reasons Binghamton cs students fail to land the best SWE jobs and internships.  

​

While you will need to complete a majority of this work on your own (i.e., outside of classes and during the summer), we would like to supplement your learning with this and future homework assignments.

​

In this assignment, you will be given multiple choice/select questions along with 2 technical interview questions with the option to answer in Python, Java, or pseudocode. While in a real interview, the interviewer will almost certainly make you answer in a real programming language, we want to be generous as you begin to learn how to think about and solve LeetCode problems. 

While this assignment is presented as a quiz in Brightspace (so we have access to the autograder for M/C questions), it will be graded as a normal homework assignment.

Multiple Choice Questions:
You will be presented with a series of multiple-choice questions and will receive full credit for selecting the correct answer.


For these problems, you can consult your notes and the slides (try to answer them on your own first), but you may NOT use AI, as the goal of these problems is to begin building an intuition for technical interviewing (where, as of now, you do not have access to AI).

Question 1 (10 points) 
During a technical interview, why is it important to first clarify inputs, outputs, and edge cases, and relate the problem to a known pattern before writing code?

Question 1 options:

To create a solution that looks more complicated and "clever" than necessary, regardless of whether it actually handles all scenarios correctly.


Because you want to impress the interviewer by talking a lot, even if you don't fully understand the problem yet.


It's optional; once you've completed enough LeetCode problems, you've seen enough of the pattern to start programming correctly without asking questions, so this step just wastes time.


To avoid writing code that fails on special cases and to connect the problem to a familiar algorithmic pattern, allowing you to explain why this approach works and how it solves the problem efficiently.

Question 2 (10 points) 
After writing code in a technical interview, why should you trace an example and analyze Big O complexity?

Question 2 options:

Because the interviewer mostly cares about whether the code compiles and runs fast on small examples, and this method emulates that.


To make your solution appear complicated and sophisticated, hoping to impress the interviewer.


Trick question - you shouldn't. It is more important to show the interviewer that you can quickly write code and move on.


To ensure your code works for all cases, including edge cases, and that you can explain why it works step by step, demonstrating a deep understanding of the algorithm.

Question 3 (10 points) 
You have an array of n  numbers. You write a series of loops that compare every number to every other number to brute-force check for duplicates. Which of the following best describes the time complexity of this algorithm, and why does it matter?

Question 3 options:

O(log n) – because checking duplicates can be done by dividing the array repeatedly.


O(1) – because checking for duplicates is a single-step operation.


O(n^2) – because each number is compared to every other number, which grows quickly as n increases.


O(n) – because it only loops through the array once, so we see all n numbers.

Question 4 (10 points) 
Which of the following best describes time complexity?

Question 4 options:

The exact number of seconds an algorithm will take to run on your computer.


How the running time of an algorithm grows as the size of the input increases.


The amount of memory an algorithm uses as the input grows.


A measure of how fast an algorithm feels to the user when running.

Multiple Select
You will be presented with a series of multiple-select questions and will receive full credit for selecting only the correct answers. Partial credit will be given if some of your responses are incorrect, but some are correct. 


For these problems, you can consult your notes and the slides  (try to answer them on your own first), but you may NOT use AI, as the goal of these problems is to begin building an intuition for technical interviewing (where, as of now, you do not have access to AI).

Question 5 (10 points) 
One of the MOST IMPORTANT skills in technical interviewing is pattern recognition. Which of the following are “hints” in a LeetCode problem that might indicate you should use the two pointer pattern?

Question 5 options:

You're asked to rearrange or reverse elements in an array without extra memory (in place)


When you know you need logarithmic [O(log(n))] time or better


The problem is asking you to check for palindromes or symmetry


Finding the next greatest (or smallest) element in a sequence


The data is sorted, and you need to find pairs or triplets that meet a condition


You're looking for a position in the list that satisfies some condition

Question 6 (10 points) 
Building off the previous question, recognizing when to use specific problem-solving patterns can make LeetCode self-study SO MUCH easier. Which of the following are “hints” in a LeetCode problem that might indicate you should use the sliding window pattern?

Question 6 options:

You're asked to find the longest or shortest substring, subarray, etc that meets some condition (such as a large or small sum).


Calculating the value for a continuous or consecutive set of elements


When you know you need logarithmic [O(log(n))] time or better


The problem involves two sorted arrays and finding pairs that sum to a target.


You have to count the number of substrings/subarrays of length k that meet a condition


The input data is guaranteed to be sorted, so you know you can always use sliding windows to reduce the time complexity


The input is a linear data structure, and a potential window size is mentioned (i.e., k)

Question 7 (Bonus) (5 points) 
Bonus
How are you going to prepare for the fall recruiting season (which starts late August 2026) this coming summer? 

As long as you answer the question honestly (even if that means you claim you won’t prepare 😢) you will receive full credit. 

Question 7 options:
Question 7 options:
Technical Interview Questions
Given the following two Technical Interview problems, write the solution in Java, Python, or Pseudocode. If you choose to answer in Java or Python, you will not lose points for syntax errors or small logic errors.

For these problems, you can consult your notes and the slides, but you may NOT use AI, as the goal of these problems is to begin practicing for interviews (where, as of now, you do not have access to AI).


Pseudocode is inherently ambiguous, so we have outlined the types of pseudocode we will accept with an example.


Problem: FizzBuzz Given an array of integers, do the following:

Ignore all negative numbers. For each non-negative number:

If it is divisible by 3, print "Fizz"

If it is divisible by 5, print "Buzz"

If it is divisible by both 3 and 5, print "FizzBuzz"

Otherwise, print the number itself

Example input:
[3, -1, 5, 15, 7, 10, 0]

Example Output:
Fizz, Buzz, FizzBuzz, 7, Buzz, FizzBuzz


Acceptable pseudocode: Clearly describes the step-by-step logic using structured statements (e.g., loops, conditions) so someone could easily translate it into real code. If you write your pseudocode detailed like this, you can expect full credit. The expectation here is that you are very precise with your logic and handle edge cases.

For each number in the array:

    If number is less than 0:

        Skip to the next iteration

 

    If number is divisible by 3 AND number is divisible by 5:

        Print "FizzBuzz"

    Else if number is divisible by 3:

        Print "Fizz"

    Else if number is divisible by 5:

        Print "Buzz"

    Else:

        Print the number


Unacceptable pseudocode: Is vague, skips key logic, or only describes the goal without showing how to achieve it.  If you write your pseudocode like this, you are unlikely to receive much credit, as you’re not handling edge cases, logic is unclear, and it is very imprecise. 


Problem: FizzBuzz 

For each number in the array:

If the number is not negative:

Check if it is divisible by 3 or 5

If so, print FizzBuzz or Fizz or Buzz depending on case

Otherwise just print the number

Else ignore it



That being said, Python would be the best choice (if possible) as that’s most likely what you’d use in the real interview!  

Question 8 (20 points) 
Maximum Valid Window Sum:

You are given an array of integers nums and an integer k.

A valid window of size k is a contiguous subarray of length k that contains at most one negative number.

Return the maximum sum among all valid windows.

Constraints:

If no valid window exists, return 0.

It is guaranteed that the input array nums will be at least size k

The time complexity of your solution must be faster than o(n*k)

Example 1
Input:
nums = [2, -1, 3, 4, -2, 6], k = 3

Windows of size 3:

[2, -1, 3] → valid (1 negative), sum = 4

[-1, 3, 4] → valid (1 negative), sum = 6

[3, 4, -2] → valid (1 negative), sum = 5

[4, -2, 6] → valid (1 negative), sum = 8

Output: 8


Example 2:
nums = [-1, -10, 3, -4, -2, 6], k = 4
Windows of size 4:

There are no valid windows of size 4

Output: 0


Python Function Signature:

def max_valid_window_sum(nums, k):
	# Paste this into your answer if you want to use python
Java Function Signature:

public static int maxValidWindowSum(int[] nums, int k) {
    // Paste this into your answer if you want to use Java
}
Question 8 options:
Question 8 options:
Question 9 (20 points) 
Count Valid Pairs With Constraint
You are given a sorted array nums and an integer T.

Return the number of pairs (i, j) such that:

i < j

nums[i] + nums[j] <= T

Constraints:

The array is sorted in non-decreasing order

Must run in O(n) time

It is guaranteed that the length of nums >= 2

 

Example 1:

Input:
nums = [1, 2, 3, 4, 6], T = 6

Valid pairs:

(0,1), (0,2), (0,3), (1,2), (1,3)

Output: 5

Example 2:

Input:
nums = [0, 1, 2, 3], T = 3

Valid pairs:

(0,1), (0,2), (0,3), (1,2)

Output: 4

Java Signature
public static int countPairs(int[] nums, int T) {
    // Paste this into your answer if you want to use Java
}
Python Signature
def count_pairs(nums, T):
	# Paste this into your answer if you want to use Python
Question 9 options:
Question 9 options:
Question 10 (15 points) 
Bonus
Complete the problem of the day on https://leetcode.com/problemset/ and paste your solution along with an image of your successful submission. Then, explain in a few sentences the time complexity of your solution and how the solution solves the problem (the "E" step in UMPIRE). 

Note: While the problem of the day rotates daily it is often easier earlier in the month and harder later in the month. 

Question 10 options:
Question 10 options: