def count_pairs(nums, T):
    left = 0
    right = len(nums) - 1
    count = 0
    
    while left < right:
        current_sum = nums[left] + nums[right]
        
        if current_sum <= T:
            # If nums[left] + nums[right] is valid, 
            # then nums[left] paired with any element 
            # between left and right is also valid.
            count += (right - left)
            # Move left pointer to check next set of pairs
            left += 1
        else:
            # Sum is too large, decrease the right pointer
            # to reduce the total sum
            right -= 1
            
    return count