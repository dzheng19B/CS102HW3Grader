def max_valid_window_sum(nums, k):
    window_sum = 0
    neg_count = 0
    
    # first window
    for i in range(k):
        window_sum += nums[i]
        if nums[i] < 0:
            neg_count += 1
    
    if neg_count <= 1:
        max_sum = window_sum
    else:
        max_sum = float('-inf')
    
    # slide window
    for i in range(k, len(nums)):
        window_sum += nums[i]
        if nums[i] < 0:
            neg_count += 1
        
        old = nums[i - k]
        window_sum -= old
        if old < 0:
            neg_count -= 1
        
        if neg_count <= 1:
            max_sum = max(max_sum, window_sum)
    
    return max_sum if max_sum != float('-inf') else 0