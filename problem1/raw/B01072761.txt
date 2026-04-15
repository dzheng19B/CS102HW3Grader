def max_valid_window_sum(nums, k):
    window_sum = 0
    neg_count = 0
    best = 0
    left = 0

    for right in range(len(nums)):
        window_sum += nums[right]
        if nums[right] < 0:
            neg_count += 1

        # Shrink if window is too big
        if right - left + 1 > k:
            if nums[left] < 0:
                neg_count -= 1
            window_sum -= nums[left]
            left += 1

        # Check valid window of exact size k
        if right - left + 1 == k and neg_count <= 1:
            best = max(best, window_sum)

    return best