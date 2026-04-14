def count_pairs(nums, T):
    i = 0
    j = len(nums) - 1
    pairs = 0

    while i < j:
        if nums[i] + nums[j] <= T:
            pairs += (j - i)
            i += 1
        else:
            j -= 1

    return pairs