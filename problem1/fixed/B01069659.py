def maxValidWindowSum(nums, k):
    sum = 0
    neg = 0
    max = 0
    for i in range(0, k):
        sum += nums[i]
        if nums[i]<0:
            neg += 1
            if neg<=1:
                max = sum
                for i in range(1, len(nums)-k):
                    sum = sum + nums[i+k-1] - nums[i-1]
                    if nums[i+k-1] < 0:
                        neg += 1
                        if nums[i-1] < 0:
                            neg -= 1
                            if neg<=1 and sum>max:
                                max = sum
                                return max