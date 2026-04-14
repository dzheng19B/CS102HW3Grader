Maximum Valid Window Sum:
You are given an array of integers nums and an integer k.
A valid window of size k is a contiguous subarray of length k that contains at most one negative number.
Return the maximum sum among all valid windows.
Constraints:


If no valid window exists, return 0.


It is guaranteed that the input array nums will be at least size k


The time complexity of your solution must be faster than o(n*k)



Example 1
Input: nums = [2, -1, 3, 4, -2, 6], k = 3
Windows of size 3:


[2, -1, 3] → valid (1 negative), sum = 4


[-1, 3, 4] → valid (1 negative), sum = 6


[3, 4, -2] → valid (1 negative), sum = 5


[4, -2, 6] → valid (1 negative), sum = 8


Output: 8
Example 2: nums = [-1, -10, 3, -4, -2, 6], k = 4
Windows of size 4:


There are no valid windows of size 4


Output: 0


Python Function Signature:
def max_valid_window_sum(nums, k):
	# Paste this into your answer if you want to use python

Java Function Signature:
public static int maxValidWindowSum(int[] nums, int k) {
    // Paste this into your answer if you want to use Java
}