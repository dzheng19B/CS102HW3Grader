def max_valid_window_sum(nums, k):
    cnt = 0
    negcnt = 0

    for i in range(k):
        if nums[i] < 0:
            negcnt += 1
    if negcnt <= 1:
        cnt += 1

    for i in range(1, len(nums) - k + 1):
        if nums[i - 1] < 0:
            negcnt -= 1
        if nums[i + k - 1] < 0:
            negcnt += 1
        if negcnt <= 1:
            cnt += 1
    
    return cnt