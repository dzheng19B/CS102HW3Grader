def count_pairs(nums, T):
    num_pairs = 0
    left = 0
    right = len(nums) - 1

    while left < right:
        if nums[left] + nums[right] <= T:
            num_pairs += (right - left)
            left += 1
        else:
            right -= 1

    return num_pairs
