def maxValidWindowSum(nums, k):
    first = True
    sum = 0
    ans = 0
    numNeg = 0
    left = 0
    right = 0
    while right < len(nums):
        if right - left < k:
            if nums[right] < 0:
                numNeg += 1
                sum += nums[right]
                right += 1
            else:
                if numNeg <= 1:
                    if first:
                        ans = sum
                    else:
                        ans = max(ans,sum)
                        first = False
                        if nums[left] < 0:
                            numNeg -= 1
                            if nums[right] < 0:
                                numNeg += 1
                                sum -= nums[left]
                                sum += nums[right]
                                left += 1
                                right += 1
                                if numNeg <= 1:
                                    if first:
                                        ans = sum
                                    else:
                                        ans = max(ans,sum)
                                        return ans