def containsNearbyDuplicate(nums:List[int],k:int) --> bool:
    d = {}
    
    for i,j in enumerate(nums):
        if j in d and i - d[j] <= k:
            return true
        else:
            d[j] = i   
            
        return false