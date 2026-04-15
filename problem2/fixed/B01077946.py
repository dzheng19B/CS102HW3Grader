def count_pairs(nums, T):
    res = 0
    left = 0
    right = len(nums) - 1

    while left < right:
        if nums[left] + nums[right] <= T:
            res += (right - left)
            left += 1
        else:
            right -= 1
    
    return res