def count_pairs(nums, T):
    start= 0
    end = len(nums) -1
    pairs = 0

    
    while start < end:
        if nums[start] + nums[end] <= T:
            pairs += (end - start)
            start += 1
        else:
            end -= 1

    
    return pairs