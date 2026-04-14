def max_valid_window_sum(nums, k):
    sum = 0
    num_negative = 0
    max_sum = float('-inf')
    valid_window = False

    for i in range(k):
        sum += nums[i]
        if nums[i] < 0:
            num_negative += 1

    if num_negative <= 1:
        max_sum = sum
        valid_window = True

    for i in range(k, len(nums)):
        outgoing = nums[i - k]
        sum -= outgoing
        if outgoing < 0:
            num_negative -= 1

        incoming = nums[i]
        sum += incoming
        if incoming < 0:
            num_negative += 1

        if num_negative <= 1:
            max_sum = max(max_sum, sum)
            valid_window = True

    return max_sum if valid_window else 0