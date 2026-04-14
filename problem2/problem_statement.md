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
Input: nums = [1, 2, 3, 4, 6], T = 6
Valid pairs:


(1,2), (1,3), (1,4), (2,3)


Output: 4

Example 2:
Input: nums = [0, 1, 2, 3], T = 3
Valid pairs:


(0,1), (0,2), (0,3), (1,2)


Output: 4

Python Signature
public static int countPairs(int[] nums, int T) {
    // Paste this into your answer if you want to use Java
}

Java Signature
def count_pairs(nums, T):
	# Paste this into your answer if you want to use Python