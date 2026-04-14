def max_valid_window_sum(nums, k):
      l = 0
      r = 0
      window_sum = nums[0]
      max_valid = 0
      negatives = 1 if window_sum < 0 else 0
      for i in range(k - 1):
         r += 1
         window_sum += nums[r]
         if nums[r] < 0:
            negatives += 1
      if negatives <= 1:
         max_valid = max(max_valid, window_sum)
      while r < len(nums) - 1:
         if negatives <= 1:
            max_valid = max(max_valid, window_sum)
         r += 1
         if nums[r] < 0:
            negatives += 1
         window_sum += nums[r]
         if nums[l] < 0:
            negatives -= 1
         window_sum -= nums[l]
         l += 1
      return max_valid
         
     
       