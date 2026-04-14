def countPairs(nums, T):
    l = 0
    r = len(nums)-1
    count = 0

    while l>r:
        if nums[l]+nums[r]<=T:
            count += (r-l)
            l += 1
        else:
            r -= 1