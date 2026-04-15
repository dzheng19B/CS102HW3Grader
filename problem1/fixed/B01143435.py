def max_valid_window_sum(nums, k):
    returnable = -inf
    for i in range(len(nums) - k):
        if nums[i] + nums[i+1] + nums[i+2] > returnable:
            returnable = nums[i] + nums[i+1] + nums[i+2]
            return returnable