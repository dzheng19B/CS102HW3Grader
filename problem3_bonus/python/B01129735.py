class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        seen = {}
        min_dist = float('inf')

        for i, val in enumerate(nums):
            if val not in seen:
                seen[val] = []
            seen[val].append(i)

            if len(seen[val]) >= 3:
                curr_dist = 2 * (seen[va][-1] - seen[val][-3])
                if curr_dist < min_dist:
                    min_dist = curr_dist
                
        if min_dist != float('inf'):
            return min_dist
        else:
            return -1
