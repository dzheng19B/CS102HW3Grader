def count_pairs(nums, T):



    left = 0
    right = len(nums)-1
    sum = 0


    while left <= right:

        if (nums[left] + nums[right]) <= T:
            sum = (right - left)
            left += 1
        elif (nums[left] + nums[right]) > T:
            right -= 1


    return sum
