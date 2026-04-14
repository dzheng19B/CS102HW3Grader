class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        positions = {}
        ans = float('inf')

        # Store all positions of each number
        for i, num in enumerate(nums):
            if num not in positions:
                positions[num] = []
            positions[num].append(i)

        # Check every consecutive group of 3 equal elements
        for indices in positions.values():
            if len(indices) >= 3:
                for i in range(len(indices) - 2):
                    ans = min(ans, 2 * (indices[i + 2] - indices[i]))

        return -1 if ans == float('inf') else ans