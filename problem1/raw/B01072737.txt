def max_valid_window_sum(nums, k):
	negs = 0
	sum = 0
	result = 0

	for i in range(k):
		if nums[i] < 0:
			negs += 1
		sum += nums[i]

	if negs <= 1:
		result = sum

	for right in range(k, len(nums)):
		left = right - k

		if nums[right] < 0:
			negs += 1
		sum += nums[right]

		if nums[left] < 0:
			negs -= 1
		sum -= nums[left]

		if negs <= 1:
			result = max(result, sum)

	return result

