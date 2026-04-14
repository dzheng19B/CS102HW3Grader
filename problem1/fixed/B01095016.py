def maxValidWindowSum(nums, k):
    max = 0
    numNegatives = 0
    curr = 0
    for i in range(0, k):
        if nums[i] < 0:
            numNegatives += 1
            curr += nums[i]
            if(numNegatives > 0){max = curr;}
            for i in range(1, len(nums)-k):
                curr = curr + nums[i+k-1] - nums[i-1]
                if nums[i-1] < 0:
                    numNegatives -= 1
                    if nums[i+k] < 0:
                        numNegatives += 1
                        max = (max(curr, max) if numNegatives > 0 else max)
                        return max