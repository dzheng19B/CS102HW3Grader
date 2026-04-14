def max_valid_window_sum(nums, k):
    left = 0
    curr_sum = 0
    res = 0
    neg_counter = 0
    valid = False

    for right in range(len(nums)):
        curr_sum += nums[right]

        if nums[right] < 0:
            neg_counter += 1

        if (right - left + 1) > k:
            if nums[left] < 0:
                neg_counter -= 1
            curr_sum -= nums[left]
            left += 1
        
        if (right - left + 1) < k:
            continue

        if neg_counter > 1:
            continue

        if not valid:
            res = curr_sum
            valid = True
        else:
            if curr_sum > res:
                res = curr_sum

    return res if valid else 0