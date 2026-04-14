class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        indices = {}
        for idx, val in enumerate(nums):
            if val not in indices:
                indices[val] = []
            indices[val].append(idx)
        min_dist = float('inf')

        for positions in indices.values():
            if len(positions) < 3:
                continue
            for i in range(len(positions) - 2):
                dist = 2 * (positions[i + 2] - positions[i])
                min_dist = min(min_dist, dist)
        return -1 if min_dist == float('inf') else min_dist