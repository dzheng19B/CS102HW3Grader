def count_pairs(nums, T):
    #print("nums = ", nums, "T = ", T)
    #problem does not say what to happens if T is uninitialized, so i'm returning -1
    if T is None:
        return -1
    l = 0
    r = len(nums) - 1
    numPairs = 0
    while l < r:
        sum = nums[l] + nums[r]
        if sum <= T:
            #all pairs (l, x) work l < x <= r
            numPairs += r - l
            #print("numPairs += ", str(r - l), ", r = ", r, "l = ", l)
            
            #inc l
            l += 1
        else:
            #dec r
            r -= 1
            #print("dec r")
    return numPairs