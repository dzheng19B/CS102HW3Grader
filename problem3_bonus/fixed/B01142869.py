class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        for q in queries:
            idx = q[0]

            while idx <= q[1]:
                nums[idx] = (nums[idx] * q[3]) % (10**9 + 7)
                idx += q[2]

        xor = 0
        for num in nums:
            xor = xor ^ num

        return xor