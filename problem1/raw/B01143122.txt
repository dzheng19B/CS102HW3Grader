def max_valid_window_sum(nums, k):
    lengthNow = 0
    numNegatives = 0
    maxm = float('-inf')
    foundValid = False
    for i in range(k):
        lengthNow += nums[i]
        if nums[i] < 0:
            numNegatives += 1
    if numNegatives <= 1:
        maxm = lengthNow
        foundValid = True
    for i in range(k, len(nums)):
        lengthNow += nums[i]
        if nums[i] < 0:
            numNegatives += 1
        lengthNow -= nums[i - k]
        if nums[i - k] < 0:
            numNegatives -= 1
        if numNegatives <= 1:
            maxm = max(maxm, lengthNow)
            foundValid = True

    return maxm if foundValid else 0