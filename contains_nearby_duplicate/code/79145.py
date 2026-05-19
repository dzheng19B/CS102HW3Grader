def containsNearbyDuplicate(nums: List[int], k:int) -> bool:
    s = set()
    d = {}
    
    for i in range(len(nums)):
    
        if nums[i] in s:
            if abs(d[nums[i]] - i) <= k:
                return True
            else:
                d[nums[i]] = i
        else:
            s.append(nums[i]) 
            d[nums[i]] = i
    
    return False
            
# Time complexity is O(n) because set and dictionary lookup is O(1) so only the for loop O(n) applies.
# This solves the problem by creating a set to detect duplicates and the dictionary to keep track of indices. It works by iterating through the array until it finds a duplicate. When it finds a duplicate, it looks up the previous indice with the dictionary and does the abs(i - j) <= k operation to return True or continue if False until it reaches the end of the array.