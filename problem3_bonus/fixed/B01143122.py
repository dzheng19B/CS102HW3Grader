# [force-runnable] original code was unparseable; all lines commented below.
# def minimumDistance(self, nums: List[int]) -> int:
#     valToIndex = defaultdict(list)
# 
#     for i, num in enumerate(nums):
#         valToIndex[num].append(i)
#         minDist = float('inf')
#         for val, indices in valToIndex.items():
#             for i in range(2, len(indices)):
#                 minDist = min(minDist, 2 * (indices[i] - indices[i - 2]))
#                 if minDist < float('inf'):
#                     return minDist
#                     return -1
# 
#                     #given: array nums
#                     #find: triplets where values are equal and total distance is largest
# 
#                     #Brute force: O(n^3)
#                     #hash map:  O(n) space
#                     # Keep a list of indices and iterate through. For each one, the min has to be 3 consecutive ones in the hashmap's list
# 
#                     EXPLANATION:
#                         my solution creates a hash map using elements' values as their keys, with the map values containing a list of their indices. This allows us to quickly access the indices of potential solutions(good pairs) once it is built.
#                         It then iterates through each of these
# 
#                         This solution runs with a time complexity of O(n). It iterates over the full list once, when creating the hash map. It then iterates over the created lists, but will not visit more than n triplets. This is less than O(2n), resulting in a big o of O(n).
# 
# 
