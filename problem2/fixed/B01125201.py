#for the first example shouldn't the output be 5 because 2 + 4 = 6 <= T?

def count_pairs(nums, T):
    cnt = 0
    i = 0
    j = len(nums) - 1

    while i < j:
        if nums[i] + nums[j] > T:
            j -= 1
        else:
            cnt += j - i
            i += 1

    return cnt