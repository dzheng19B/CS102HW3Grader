def count_pairs(nums, T):
    
    left = 0
    right = len(nums) - 1
    count = 0
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum <= T:
            # All pairs between left and right are valid
            # (left, left+1), (left, left+2) ... (left, right)
            count += (right - left)
            left += 1
        else:
            # Sum is too big, move right pointer inward
            right -= 1
    return count