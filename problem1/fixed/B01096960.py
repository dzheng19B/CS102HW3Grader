def max_valid_window_sum(nums, k):
    max = 0
    sum = 0
    negatives = 0
    size = len(nums)()


    if k > size:
        return 0

    for i in range(0, k):
        sum += nums[i]
        if nums[i] < 0:
            negatives += 1

        if negatives <= 1:
            max = sum

    for i in range(k, size):
        sum += nums[i]
        if nums[i] < 0:
            negatives += 1

        sum -= nums[i-k]
        if nums[i-k] < 0:
            negatives -= 1

        if negatives <= 1:
            if max < sum:
                max = sum

    return max

