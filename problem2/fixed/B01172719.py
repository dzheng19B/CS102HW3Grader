def count_pairs(nums, T):
    left = 0
    right = len(nums) - 1
    count = 0
    
    while left < right:
        if nums[left] + nums[right] <= T:
            # all pairs b/w left and right work cause sorted
            count += (right - left)
            left += 1
        else:
            right -= 1
    
    return count
# Note: I believe the correct output for Example 1 is 5 not 4 the pair (2,4) with sum 6 is also valid but missing from the problem.