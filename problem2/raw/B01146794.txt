def count_pairs(nums, T): #use two pointers
    pairs = 0 
    left = 0  
    right = len(nums)-1
    while(left < right): # loop until left is less than right
        if(nums[left] + nums[right] < T): # if nums[left] + nums[right] is less than or equal T  update the number of valid pairs and increment the left 
            pairs += right-left 
            left += 1 
        else: #if not valid pair decrease the right
            right -= 1
    print(pairs)