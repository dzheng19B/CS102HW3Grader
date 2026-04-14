def max_valid_window_sum(nums, k):
    n = len(nums)
    if n < k:
        return 0
    
    current_sum = 0
    neg_count = 0
    max_sum = float('-inf')
    found_valid = False
    
    for i in range(k):
        current_sum += nums[i]
        if nums[i] < 0:
            neg_count += 1
            
    if neg_count <= 1:
        max_sum = current_sum
        found_valid = True
        
    for i in range(k, n):
        current_sum += nums[i]
        if nums[i] < 0:
            neg_count += 1
            
        outgoing = nums[i - k]
        current_sum -= outgoing
        if outgoing < 0:
            neg_count -= 1
            
        if neg_count <= 1:
            max_sum = max(max_sum, current_sum)
            found_valid = True
            
    return max_sum if found_valid else 0