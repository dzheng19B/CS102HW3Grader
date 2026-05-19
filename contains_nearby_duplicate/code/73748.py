def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    d = {}
    for i , var in enumerate(nums):
        if var in d and i-d[var] <= k:
            return True
        else:
            d[var]=i
    return False

#time complexity for this solution is O(n). turns list into a dictionary(hashmap), 
#then looped through variables using sliding windows. if satisfies the condition return true
# else add to the dictionary(hashmap) and continue to loop. at the end of the loop if condition
# did not met return false