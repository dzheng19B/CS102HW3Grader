class Solution(object):
    def minimumDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict
        index_map = defaultdict(list)
        for i, num in enumerate(nums):
            index_map[num].append(i)

        min_distance = float('inf')

        for indices in index_map.values():
            if len(indices) >= 3:
                for i in range(len(indices) - 2):
                    distance = 2 * (indices[i + 2] - indices[i])
                    min_distance = min(min_distance, distance)
        return min_distance if min_distance != float('inf') else -1