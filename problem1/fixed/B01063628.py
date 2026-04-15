def max_valid_window_sum(nums, k):
     curr = 0
     maxSum = 0
     neg = 0
     left = 0

     for right in range(len(nums)):
          curr = curr + nums[right]
          if nums[right] < 0:
                    neg += 1

          if (right - left) + 1 > k:
                    if nums[left] < 0:
                              neg -= 1
                    curr -= nums[left]
                    left += 1

          if (right - left) + 1 == k and neg <= 1:
                    maxSum = max(maxSum, curr)
     
     return maxSum



              



     