def max_valid_window_sum(nums, k):
    #how i would go with this
    #sliding window approach b/c it will run in o(n) time complexity
    initialize the values of window, negative count, and max sum to 0
    window = 0
    count = 0
    maxSum = 0
    length = len(nums)

    for the first k elements (for i in range(k)):
        add each number to the window (meaning window += nums[i])
        if number is less than 0: nums[i] < 0:
            increment negative: count += 1

            if count is less than or equal to 1:
                set maxSum to the window
                if count <= 1:
                    maxSum = window

                    for each index i from k to the end of the array:
                        add nums[i] to window
                        if nums[i] is less than 0:
                            increment count (+=)
                            if nums[i - k] is less than 0:
                                decrement count (-=)
                                subtract nums[i - k] from window
                                if count is less or equal to 1:
                                    set maxSum to the max sum and window (max(maxSum, window)

                                    return maxSum