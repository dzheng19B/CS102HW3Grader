def max_valid_window_sum(nums, k):
    curr_sum = sum (nums[:k])
    neg_count = sum(1 for x in nums[:k] if x < 0)
    max_sum = curr_sum if neg_count <= 1 else float('-inf')


    for i in range (k, len(nums))):

        curr_sum += nums [i] - (nums [i-k] < 0)
        neg_count += (nums [i] < 0) - (nums[i-k] < 0)

        if neg_count <= 1:
            max_sum = max(max_sum, curr_sum)

            return max_sum if max_sum != float('-inf') else 0

