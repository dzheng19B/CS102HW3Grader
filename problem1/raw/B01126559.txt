def max_valid_window_sum(nums, k):
    window_sum = 0
    negative_count = 0
    max_sum = 0

    for i in range(k):
        window_sum += nums[i]
        if nums[i] < 0:
            negative_count += 1

    if negative_count <= 1:
        max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i]
        if nums[i] < 0:
            negative_count += 1

        if nums[i - k] < 0:
            negative_count -= 1
        window_sum -= nums[i - k]

        if negative_count <= 1:
            max_sum = max(max_sum, window_sum)

    return max_sum