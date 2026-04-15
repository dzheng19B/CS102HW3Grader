# Online Python - IDE, Editor, Compiler, Interpreter
def max_valid_window_sum(nums, k):
    #debug
    # print("nums = ", nums)
    # print("k = ", k)
    #if empty/None/0/negative
    if (k <= 0) or (not nums):
        return 0
    sum = 0
    negativeCount = 0
    maxSum = 0
    maxSumExists = False#maxSum may be < 0
    #initialize vars
    for n in range(k):
        sum += nums[n]
        if nums[n] < 0:
            negativeCount += 1
    if negativeCount <= 1:
        maxSum = sum
        maxSumExists = True
    rightPointer = k - 1
    #leftPointer = r - k + 1
    while rightPointer + 1 < len(nums):
        rightPointer += 1
        #right
        sum += nums[rightPointer]
        if nums[rightPointer] < 0:
            negativeCount += 1
        #left
        sum -= nums[rightPointer - k]
        if nums[rightPointer - k] < 0:
            negativeCount -= 1
        if negativeCount <= 1:
            maxSum = max(maxSum, sum)
            maxSumExists = True
            
        #debug
        # print("rightPointer = ", rightPointer)
        # print("negativeCount = ", negativeCount)
        # print("sum = ", sum)
        # print("maxSum = ", maxSum)
        # print("maxSumExists = ", maxSumExists)
    if maxSumExists:
        return maxSum
    else:
        return 0
        