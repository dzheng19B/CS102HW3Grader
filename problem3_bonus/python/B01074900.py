# [force-runnable] original code was unparseable; all lines commented below.
# This was the Problem of the Day for Sunday April 12th (Minimum Distance to the Target Element), which was when I started it (I grabbed my screenshot the next day.) The time complexity should be O(n) as I iterated through the array and checked the conditions at each index. I keep track of the minimum value of abs(i - start) I checked at each iteration if the conditions are smaller than the saved minimum value. If it was then I updated it. I started the minimum as -1 as this was an invalid distance, to look for the first case.
# 
# 
# 
# class Solution:
# public:
# getMinDistance(vector& nums, int target, int start)
# 
# distance = 0
# minDistance = -1
# 
# for i in range(0, nums.size()):
# if nums[i] == target:
# 
# distance = i - start
# if distance <= 0:
# distance *= -1
# 
# if minDistance == -1:
# minDistance = distance
# 
# if distance < minDistance:
# minDistance = distance
# 
# if(distance == 0){ return 0;}:
# 
# if minDistance == -1:
# return 0
# 
# return minDistance
