def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    dict = {}
    for i,val in enumerate(nums):
        if val in dict and i-dict[val] <= k:
            return True
        else:
            dict[val] = i

    return False