class Solution(object):
    def minimumDistance(self, nums):
        positions = {}
        
        for i in range(len(nums)):
            val = nums[i]
            if val not in positions:
                positions[val] = []
            positions[val].append(i)
        
        ans = -1 
        
        for val in positions:
            idxs = positions[val]
            
            if len(idxs) < 3:
                continue
            
            for i in range(len(idxs) - 2):
                distance = 2 * (idxs[i + 2] - idxs[i])
                
                if ans == -1 or distance < ans:
                    ans = distance
        
        return ans