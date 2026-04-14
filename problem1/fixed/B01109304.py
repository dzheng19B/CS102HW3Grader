def max_valid_window_sum(nums, k):
    n = len(nums)
    max_sum = 0
    
    for i in range(n - k + 1):
        current_sum = sum(nums[i:i+k])
        negatives = 0
        for x in nums[i:i+k]:
            if x < 0:
                negatives += 1
        
        if negatives <= 1:
            max_sum = max(max_sum, current_sum)
    
    return max_sum