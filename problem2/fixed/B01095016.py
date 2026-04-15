def count_pairs(nums, T):
    count = 0
    l = 0
    r = len(nums)-1
    while l < r:
        if nums[l] + nums[r] <= T:
            count += (r-l)
            l += 1
        else:
            r -= 1
    return count