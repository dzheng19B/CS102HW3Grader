def max_valid_window_sum(nums, k):
    max_sum = 0
    window_sum = sum(nums[:k])
    neg_count = 0
    for x in nums[:k]:
        if x < 0:
            neg_count += 1

            if neg_count <= 1:
                max_sum = window_sum

                for i in range(k, len(nums)):
                    # add incoming element
                    window_sum += nums[i]
                    if nums[i] < 0:
                        neg_count += 1

                        # remove outgoing element
                        window_sum -= nums[i - k]
                        if nums[i - k] < 0:
                            neg_count -= 1

                            if neg_count <= 1:
                                max_sum = max(max_sum, window_sum)

                                return max_sum