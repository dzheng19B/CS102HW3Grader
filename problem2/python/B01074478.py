def count_pairs(nums, T):
   p1, p2, res = 0, len(nums) - 1, 0
   while p1 < p2:
      if nums[p1] + nums[p2] > T :
         p2 -= 1
      else:
         res += p2 - p1
         p1 += 1
   return res