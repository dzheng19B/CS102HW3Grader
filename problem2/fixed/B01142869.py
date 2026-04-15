def count_pairs(nums, T):
    l = 0
    r = len(nums) - 1
    valid_pairs = 0

    while l < r:
        if nums[l] + nums[r] <= T:
            valid_pairs += (r - l)
            l += 1
        else:
            r -= 1

    return valid_pairs