def count_pairs(nums, T):
	n_pairs = 0 
	
	l = 0 
	r = len(nums) - 1 
	while l < r:
		if nums[l] + nums[r] > T:
			r -= 1
		elif nums[l] + nums[r] <= T:
			n_pairs += r - l
			l += 1
	
	return n_pairs