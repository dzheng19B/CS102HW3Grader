#A valid window of size k is a contiguous subarray of length k that contains at most one negative number. Return the maximum sum among all valid windows.

def max_valid_window_sum(nums, k):
    sum = 0

    count = 0
    maxSum = 0
    arraySize = len(nums)

    for i in range(k):
        sum += nums[i]
        if nums[i] < 0:
            count += 1

            if count <= 1:
                maxSum = sum

                for i in range(k, arraySize):
                    maxSum += nums[i]
                    if nums[i] < 0:
                        count += 1
                        if nums[i-k] < 0:
                            count -= 1
                            sum -= nums[i-k]

                            if count <= 1:
                                sum = max(maxSum, sum)
                                return maxSum

                                if count > 1:
                                    return 0
