def count_pairs(nums, T):
# Paste this into your answer if you want to use Python
    count = 0
    left = 0
    right = len(nums) - 1
    
    while left < right:
        if nums[left] + nums[right] <= T:
            count += (right - left)
            left += 1
        else:
            right -= 1
            
    return count


