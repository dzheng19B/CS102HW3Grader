def max_valid_window_sum(nums, k):
       l = r = window_sum = max_sum = negative_count = 0

       for r in range(k):
             window_sum += nums[r]
             if nums[r] < 0:
                negative_count += 1
       if negative_count <=1:
             max_sum = window_sum

       for r in range(k, len(nums)):
             if nums[l] < 0:
                 negative_count -=1
             window_sum -= nums[l]
             l += 1

             window_sum += nums[r]
             if nums[r] < 0:
                negative_count +=1
             if negative_count <= 1:
                max_sum = max(max_sum, window_sum)
       return max_sum