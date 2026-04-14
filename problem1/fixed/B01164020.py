def max_valid_window_sum(nums, k):
    max_sum = 0
    negative = 0
    window_sum = 0
    for o in range(k):
        window_sum = window_sum + nums[o]
        if nums[o] < 0:
            negative = negative + 1
    
    
	# Go through all indexes within nums
    for left in range(len(nums)-(k)):
        right = left + k 

        
		# Check if window is valid
        if negative <= 1 and window_sum > max_sum:
            max_sum = window_sum
            
		# Summing the Window
        window_sum = window_sum - nums[left] + nums[right]
        
        
		# Changing Negative counter
        if nums[left] < 0:
            negative = negative - 1
        if nums[right] <0:
            negative = negative + 1
    
	# Check last window
    if negative <= 1 and window_sum > max_sum:
            max_sum = window_sum
    return max_sum