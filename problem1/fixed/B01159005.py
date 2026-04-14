def max_valid_window_sum(nums, k):
    i = 0
    j = k 
    result = 0
    while j <= len(nums):
        negative = 0 
        placeholder = 0
        for x in range(i,j):
            if nums[x]<0:
                negative = negative +1 
            placeholder = placeholder + nums[x] 
        if negative < 2:
            result = placeholder
        i = i +1 
        j = j+1
    return result
                
        
            
            