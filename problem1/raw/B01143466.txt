def max_valid_window_sum(nums, k):
    max_sum = 0
    curr = sum(nums[0:k])
    nc = 0
    
    for x in nums[0:k]:
        if x < 0:
            nc += 1
    
    if nc <= 1:
        max_sum = max(max_sum, curr)
    
    for i in range(len(nums) - k):
        curr = curr - nums[i] + nums[i + k]
        
        if nums[i] < 0:
            nc -= 1
        if nums[i + k] < 0:
            nc += 1
        
        if nc <= 1:
            max_sum = max(max_sum, curr)
    
    return max_sum
        