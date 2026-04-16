def max_valid_window_sum(nums, k):

    #initialize the sum and count
    window_sum = 0
    max_sum = 0
    negative_count = 0

    #set up first window
    for i in range(k):
        window_sum += nums[i]
        if nums[i] < 0:
            negative_count += 1

    if negative_count <=1:
        max_sum = window_sum

    #set up slide window
    for i in range(k, len(nums)):
        #add the new element
        window_sum += nums[i]
        if nums[i] < 0:
            negative_count += 1

        #remove the old element
        window_sum -= nums[i - k]
        if nums[i - k] < 0:
            negative_count -= 1

        #check if the window is valid
        if negative_count <=1:
            max_sum = max(max_sum, window_sum)

    return max_sum