def count_pairs(nums, T):
    count = 0
    left = 0
    right = len(nums) - 1
    
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum <= T:
            count += (right - left)
            left += 1
        else:
            right -= 1
            
    return count