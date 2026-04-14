def count_valid_pairs(nums, T):

    left = 0
    right = len(nums) - 1
    count = 0
    
    while left < right:
        currentsum = nums[left] + nums[right]
        
        if currentsum <= T:
            count += (right - left)
            left += 1
        else:
            right -= 1
    
    return count