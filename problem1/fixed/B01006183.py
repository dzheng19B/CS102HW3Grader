def max_valid_window_sum(nums, k):
    # Paste this into your answer if you want to use python

    if k > len(nums):
        return 0

        curr_sum = sum(nums[:k])
        neg_count = sum(1 for i in range(k) if nums[i] <0)

        max_sum = 0

        for i in range(k, n):
            if nums[i] < 0:
                curr_sum += nums[i]

                if nums[i-k] < 0:
                    curr_sum -= nums[i-k]

                    return max_sum
