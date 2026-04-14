def max_valid_window_sum(nums, k):
    neg_count = sum(1 for x in nums[:k] if x < 0)
    window_sum = sum(nums[:k])
    max_sum = window_sum if neg_count <= 1 else float('-inf')
    
    for i in range(1, len(nums) - k + 1):
        window_sum += nums[i + k - 1] - nums[i - 1]
        if nums[i + k - 1] < 0:
            neg_count += 1
        if nums[i - 1] < 0:
            neg_count -= 1
        if neg_count <= 1:
            max_sum = max(max_sum, window_sum)
    return 0 if max_sum == float('-inf') else max_sum
