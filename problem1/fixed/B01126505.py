def maxValidWindowSum(nums, k):
    l = 0
    windowsum = 0
    negative = 0
    max = 0

    for r in range(0, len(nums)):
        windowsum += nums[r]
        if nums[r]<0:
            negative += 1

            if r-l+1>k:
                if nums[l]<0:
                    negative -= 1
                    windowsum -= nums[l]
                    l += 1

                    if r-l+1 == k and negative <=1:
                        max = max(max, windowsum)


                        return max