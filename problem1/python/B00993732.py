def max_valid_window_sum(nums, k):
    left = 0
    right = len(nums) - 1
    num_negative = 0
    window_sum = 0
    final_sum = 0

    while left < right:
        if num[r] < 0:
            num_negative += 1

            if r - l + 1> k:
                window_sum -= nums[1] # Reduce size of array
                left += 1
                # Valid window
                if r-l + 1 == k:
                    if num_negative <= 1:
                        pass




