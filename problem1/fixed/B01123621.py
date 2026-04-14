def max_valid_window_sum(nums, k):
     max = 0
     current = 0
     neg = 0
     valid = False
     for i in range(k):
          current += nums[i]
          if nums[i] < 0:
               neg += 1
     if neg == 1:
          max_sum += current
          valid = True
     for i in range(k, len(nums)):
          if nums[i] < 0:
               neg += 1
          current += nums[i]
          if nums[i-k] < 0:
               neg -= 1
          current -= nums[i-k]
          if neg == 1:
               if current >= max_sum:
                    max_sum = current
               valid = True
     if valid:
          return max_sum
     return 0