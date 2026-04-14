def count_pairs(nums, T):
     left = 0
     right = len(nums)-1
     num_pairs = 0
     while left < right:
          if nums[left] + nums[right] <= T:
               nums_pairs += (right - left)
               left += 1
          else:
               right -= 1
     return num_pairs