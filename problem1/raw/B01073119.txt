def max_valid_window_sum(nums, k):
        windowSum =  sum(nums[:k])
        countNeg = sum(1 for x in nums[:k] if x < 0)

        maxSum = windowSum if countNeg <= 1 else 0

        for i in range(k, len(nums)):
           incoming = nums[i]
           outgoing = nums[i - k]

           windowSum += incoming - outgoing

           if incoming < 0:
               countNeg += 1
           if outgoing < 0:
               countNeg -= 1
           if countNeg <= 1:
               maxSum = max(maxSum, windowSum)

        return maxSum