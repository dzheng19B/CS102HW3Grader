def max_valid_window_sum(nums, k):
    max = 0
    for i in range(len(nums)-k):
         if sum(nums[i:k]) > max:
               max = sum(nums[i:k])
    return max
	