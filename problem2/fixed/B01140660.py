def count_pairs(nums, T):
    def count_valid_pairs(nums, T):
        count = 0
        L = 0
        R = len(nums) - 1
    
        while L < R:
            current_sum = nums[L] + nums[R]
        
            if current_sum <= T:
                count += (R - L)
                L += 1
            else:
                R -= 1
            
        return count