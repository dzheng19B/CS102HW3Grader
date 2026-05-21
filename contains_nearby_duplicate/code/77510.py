def containsNearbyDuplicate(nums, k):
    s = {}
    for i in range(len(nums)):
        if nums[i] in s:
            if abs(i - s[nums[i]]) <= k:
                return True
        s[i] = nums[i]
    return False
