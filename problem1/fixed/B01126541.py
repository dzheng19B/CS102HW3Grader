def max_valid_window_sum(nums, k):
    curr_sum = 0
    max_sum = -1 * math.inf
    num_neg = 0

    
    for i, num in enumerate(nums):
        curr_sum += num 

        if num < 0:
            num_neg += 1

        if i >= k - 1:
            if num_neg == 1:
                print("i = " + str(i) + " sum = " + str(curr_sum))
                max_sum = max(max_sum, curr_sum)

            curr_sum -= nums[i - k + 1]

            if nums[i - k + 1] < 0:
                num_neg -= 1


    if max_sum == -1 * math.inf:
        max_sum = 0
    
    return max_sum