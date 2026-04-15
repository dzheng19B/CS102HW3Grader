# [force-runnable] original code was unparseable; all lines commented below.
# class Solution:
# public:
# 
# minimumDistance(vector& nums)
# unordered_map<int, vector> indexMap
# for i in range(0, nums.size()):
# indexMap[nums[i]].push_back(i)
# minDist = INT_MAX
# for (auto& [val, indices] : indexMap)
# if (indices.size() < 3) continue:
# for (int t = 0; t + 2 < indices.size(); t += 1):
# i = indices[t]
# j = indices[t + 1]
# k = indices[t + 2]
# dist = 2 * (k - i)
# minDist = min(minDist, dist)
# (-1 if return minDist == INT_MAX else minDist)
# 
# 
# 
# I group indices by value using a hash map, then for each value with at least 3 occurrences, I slide over consecutive triples and compute 2 * (k - i) as the simplified distance. Since indices are stored in sorted order, consecutive triples always minimize k - i, guaranteeing the optimal result. Overall time complexity is O(n) since every index is visited at most once.
