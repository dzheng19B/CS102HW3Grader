def count_pairs(nums, T):
    num_pair = 0
    left = 0
    right = len(nums) - 1

    while left < right:
        if nums[left] + nums[right] <= T:
            num_pair = num_pair + (right - left)
            left = left + 1
        else:
            right = right - 1

    return num_pair