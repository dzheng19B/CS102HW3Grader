def max_valid_window_sum(nums, k):
    n = len(nums)

    Initialize the first window
    window_sum = sum(nums[:k])
    neg_count = sum(1 for x in nums[:k] if x < 0)

    Track the best result
    max_sum = window_sum if neg_count <= 1 else 0
    found_valid = neg_count <= 1

    Slide the window
    for i in range(k, n):
        Add the new element entering the window
        window_sum += nums[i]
        if nums[i] < 0:
            neg_count += 1

            Remove the element leaving the window
            window_sum -= nums[i - k]
            if nums[i - k] < 0:
                neg_count -= 1

                Check if this window is valid
                if neg_count <= 1:
                    if not found_valid:
                        max_sum = window_sum
                        found_valid = True
                    else:
                        max_sum = max(max_sum, window_sum)

                        return max_sum if found_valid else 0