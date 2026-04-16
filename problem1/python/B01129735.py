def max_valid_window_sum(nums, k):
    def max_value_window_sums(nums, k):
        max_sum = 0
        curr_sum = 0
        negs = 0
        start = 0
        end = k

        for i in range(k):
            curr_sum += nums[i]
            if nums[i] < 0:
                negs+=1
        
        if negs <= 1:
            max_sum = curr_sum


        while(end < len(nums)):
            curr_sum += nums[end]
            if nums[end] < 0:
                negs += 1
        
            curr_sum -= nums[start]
            if nums[start] < 0:
                negs -= 1
        
            if negs <= 1:
                if curr_sum > max_sum:
                    max_sum = curr_sum
        
            start += 1
            end += 1
    
        return max_sum