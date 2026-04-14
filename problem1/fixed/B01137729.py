sum = sum of nums[0] through nums[k -1]

negCount = 0
for i from 0 to k - 1:
    if nums[i] < 0:
        negCount++

        total= 0

        if negCount <= 1:
            total = sum
            for i from k to len(nums) - 1:
                sum += nums[i]
                sum -= nums[i - k]
                if nums[i] <0:
                    negCount++
                    if nums[i - k] < 0:
                        negCount--
                        if negCount <= 1:
                            total = maxOf(total, sum)

                            return total