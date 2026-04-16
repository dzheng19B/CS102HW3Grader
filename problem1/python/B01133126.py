def max_valid_window_sum(nums, k):
    n = len(nums)
    if n < k:
        return 0
    
    windowsum = 0
    negcount = 0
 
    for i in range(k):
        windowsum += nums[i]
        if nums[i] < 0:
            negcount += 1


    maxsum = windowsum if negcount <= 1 else float('-inf')
    

    for i in range(k, n):
        windowsum += nums[i]
        if nums[i] < 0:
            negcount += 1
  

        left = nums[i - k]
        windowsum -= left
        if left < 0:
            negcount -= 1
        
        if negcount <= 1:
            maxsum = max(maxsum, windowsum)
    
    return maxsum if maxsum != float('-inf') else 0