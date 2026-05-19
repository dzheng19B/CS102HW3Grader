def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    mapp = {}
    j = 0
    for j in len(nums):
        if nums[j] in mapp:
            if j - mapp[nums[j]] <= k:
                return True
        mapp[nums[j]] = j
    return False
        
# Time complexity: O(n) because it runs through the array once
# Solves the problem by running through the list and adding values
# to the hashmap. If the value already exist, it checks if abs(i-j) <= k


            