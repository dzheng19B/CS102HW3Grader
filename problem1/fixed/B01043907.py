def max_valid_window_sum(nums, k):
    l = 0
    r = k - 1
    currentSum = 0
    maxSum = 0
    numNegative = 0
    for i in range(0,k): #initial check to get value of numNegative for first window
        currentSum += nums[i]
        if nums[i] < 0:
            numNegative +=1
    while r < len(nums):
        if numNegative <=1:
                maxSum = max(maxSum, currentSum)
        if nums[l] <0:
            numNegative -=1
        if r < len(nums)-1: #edge case for when r is at the end of the array to avoid out of bounds error
            if nums[r+1] <0:
                numNegative +=1
            currentSum = currentSum - nums[l] + nums[r+1]
        l+=1
        r+=1
    return maxSum
