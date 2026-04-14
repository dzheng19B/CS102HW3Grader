def count_pairs(nums, T):
    l = 0
    r = len(nums) - 1
    num = 0
    while l < r:
        if nums[l] + nums[r] <= T:
            num += (r - l)
            l += 1
        else:
            r-= 1