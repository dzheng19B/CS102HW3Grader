def max_valid_window_sum(nums, k):
    curr_sum = 0
    neg_count = 0
    max_sum = 0

    for i in range(k):
        curr_sum += nums[i]
        if nums[i] < 0:
            neg_count += 1
    if neg_count <= 1:
        max_sum = curr_sum

    for i in range(k, len(nums)):
        curr_sum += nums[i]
        if nums[i] < 0:
            neg_count += 1
        if nums[i - k] < 0:
            neg_count -= 1
        curr_sum -= nums[i - k]
        if neg_count <= 1:
            if curr_sum > max_sum:
                max_sum = curr_sum

    return max_sum