#i chose to write in python for all my answers

def max_valid_window_sum(nums, k):
    window_sum = sum(nums[:k])
    neg_count = sum(1 for x in nums[:k] if x < 0)

    max_sum = window_sum if neg_count <= 1 else 0

    for i in range(k, len(nums)):
        incoming = nums[i]
        outgoing = nums[i - k]

        window_sum += incoming - outgoing

        if incoming < 0:
            neg_count += 1
        if outgoing < 0:
            neg_count -= 1

        if neg_count <= 1:
            max_sum = max(max_sum, window_sum)

    return max_sum