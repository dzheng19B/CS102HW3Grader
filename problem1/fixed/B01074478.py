def max_valid_window_sum(nums, k):
   p1, p2, res = 0, k-1, 0
   tempSum = sum(nums[:k])
   for x in nums[p1:p2+1] :
      if x < 0:
         numNeg += 1
   while p2 < len(nums) :
      if numNeg < 2:
         res = max(res, tempSum)
      if nums[p1] < 0:
         numNeg -= 1
      tempSum -= nums[p1]
      if nums[p2+1] < 0:
         numNeg += 1
      tempSum += nums[p2+1]
      p1, p2 = p1 + 1, p2 + 1
   return res