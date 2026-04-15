class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        indices = {}
        for i in range(len(nums)):
            if nums[i] not in indices:
                indices[nums[i]] = []
            indices[nums[i]].append(i)
        
        min_dist = float('inf')
        
        for value in indices:
            idx_list = indices[value]
            if len(idx_list) < 3:
                continue
            
            for i in range(len(idx_list) - 2):
                p = idx_list[i]
                q = idx_list[i + 1]
                r = idx_list[i + 2]
                dist = 2 * (r - p)
                min_dist = min(min_dist, dist)
        
        return min_dist if min_dist != float('inf') else -1
