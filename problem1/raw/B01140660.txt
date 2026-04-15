def max_valid_window_sum(nums, k):
    currsum = sum(nums[:k])
    numofnegs = sum(1 for x in nums[:k] if x < 0)
    max_sum = -float('inf')
    found_valid = False
    if numofnegs <= 1:
        max_sum = currsum
        found_valid = True    
    for i in range(k, len(nums)):
        currsum += nums[i]
        if nums[i] < 0:
            numofnegs += 1            
        old_val = nums[i - k]
        currsum -= old_val
        if old_val < 0:
            numofnegs -= 1        
        if numofnegs <= 1:
            if currsum > max_sum:
                max_sum = currsum
            found_valid = True
    if found_valid:
        return max_sum
    else:
        return 0