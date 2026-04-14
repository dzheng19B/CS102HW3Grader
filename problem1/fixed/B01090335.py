def max_valid_window_sum(nums, k):
    max_sum = float('-inf')
    current_sum = 0
    neg_count = 0
    found_valid = False

    for i in range(len(nums)):
        current_sum += nums[i]
        if nums[i] < 0:
            neg_count += 1
        
        if i >= k:
            outgoing = nums[i - k]
            current_sum -= outgoing
            if outgoing < 0:
                neg_count -= 1
        
        if i >= k - 1:
            if neg_count <= 1:
                max_sum = max(max_sum, current_sum)
                found_valid = True
                
    return max_sum if found_valid else 0