def max_valid_window_sum(nums, k):
    n = len(nums)
    if n < k: return 0 
    
    curr_sum = sum(nums[:k])
    neg_count = sum(1 for x in nums[:k] if x < 0)
    
    max_ans = -float('inf')
    found = False
    
    if neg_count <= 1:
        max_ans = curr_sum
        found = True
        
    for i in range(k, n):
        if nums[i] < 0: neg_count += 1
        curr_sum += nums[i]
        
        if nums[i-k] < 0: neg_count -= 1
        curr_sum -= nums[i-k]
        
        if neg_count <= 1:
            max_ans = max(max_ans, curr_sum)
            found = True
            
    return max_ans if found else 0