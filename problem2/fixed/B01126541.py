def count_pairs(nums, T):
    num_pairs = 0
    i =  0
    j = len(nums) - 1

    while i < j: 
        sum = nums[i] + nums[j]
        if sum <= T:
            num_pairs += j - i
            i += 1
        else:
            j -= 1

    return num_pairs
