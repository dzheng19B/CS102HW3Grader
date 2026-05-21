def containsNearbyDuplicate(nums, k):
    dup = {}
    for i, val in enumerate(nums):
        if val in dup and i - dup[val] <= k:
            return True
        else:
            dup[val] = i
    return False
