class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        result = float('inf')
        for num in set(nums):
            
            indces = [i for i in range(len(nums)) if nums[i] == num]
            for m in range(len(indces) - 2):
                result = min(result, 2 * (indces[m + 2] - indces[m]))
        if result != float('inf'):

            return result 
        else:
            return -1
