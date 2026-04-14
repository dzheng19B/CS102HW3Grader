def max_valid_window_sum(nums, k):
    left = 0
    right = 0
    negatives = 0
    while right < len(nums):
        if left - right < valid window size:
            right ++
            if right number is negative:
                negatives++
                if there is more than one negative:
                    if left number is negative:
                        negatives--
                        left++
                        if there is one negative AND size of window < k:
                            solution = []
                            for i in range(left, right + 1, 1):
                                solution.append(num[i])
                                print solution