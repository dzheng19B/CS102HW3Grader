def maxValidWindowSum(nums, k):
    windowSum = 0
    negativeCount = 0
    maxSum = float('-inf')


    for i in range(0, k):
        windowSum += nums[i]
        if nums[i] < 0:
            negativeCount += 1

            if negativeCount <= 1:
                maxSum = windowSum

                for i in range(k, len(nums)):
                    if nums[i - k] < 0:
                        negativeCount -= 1
                        windowSum -= nums[i - k]
                        windowSum += nums[i]
                        if nums[i] < 0:
                            negativeCount += 1
                            if negativeCount <= 1:
                                maxSum = max(maxSum, windowSum)


                                return (0 if maxSum == float('-inf') else maxSum)


