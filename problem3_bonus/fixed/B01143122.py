def minimumDistance(self, nums: List[int]) -> int:
    valToIndex = defaultdict(list)

    for i, num in enumerate(nums):
        valToIndex[num].append(i) 
    minDist = float('inf')
    for val, indices in valToIndex.items():
        for i in range(2, len(indices)):
            minDist = min(minDist, 2 * (indices[i] - indices[i - 2]))
    if minDist < float('inf'):
        return minDist
    return -1

#given: array nums
#find: triplets where values are equal and total distance is largest

#Brute force: O(n^3)
#hash map:  O(n) space
# Keep a list of indices and iterate through. For each one, the min has to be 3 consecutive ones in the hashmap's list