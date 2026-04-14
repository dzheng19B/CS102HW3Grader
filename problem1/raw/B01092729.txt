def max_valid_window_sum(nums, k):
    totalSum = 0
    leftptr = 0
    rightptr = 0
    tempSum = nums[0]
    negCount = 0
    if (tempSum < 0):
        negCount = 1

    while (rightptr < len(nums)-1):
        if ((rightptr - leftptr + 1) == k):
            if (nums[leftptr] < 0):
                negCount-=1
            tempSum -= nums[leftptr]
            leftptr+=1
        rightptr+=1
        if (nums[rightptr] < 0):
            negCount+=1
        tempSum += nums[rightptr]
        if (negCount <= 1 and (rightptr - leftptr + 1) == k):
            totalSum = max(totalSum, tempSum)
    return totalSum;