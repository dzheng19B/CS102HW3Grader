# [force-runnable] original code was unparseable; all lines commented below.
# ```ts
# 
# 
# function minimumDistance(nums: number[]): number
# const lastSeen = new Map<number, number[]>()
# let minDistance = Infinity
# 
# for (let i = 0; i < len(nums); i += 1):
# const num = nums[i]
# 
# if !lastSeen.has(num):
# lastSeen.set(num, [i])
# continue = 0
# 
# const seen = lastSeen.get(num) not as [number, number]
# if seen.length !== 2:
# lastSeen.set(num, [seen[0], i])
# continue = 0
# 
# const [j, k] = seen
# const distance = abs(i - j) + abs(j - k) + abs(k - i)
# minDistance = min(distance, minDistance)
# 
# lastSeen.set(num, [k, i])
# 
# (-1 if return minDistance === Infinity else minDistance)
# ```
# 
# My solution has O(n) time complexity because it loops through `nums` once and O(n) space complexity because it uses a hashmap of all previously seen numbers. It works by going through `nums` and checking if it's been seen twice previously; if it hasn't, then store it in the hashmap. If it has, compute the distance of the 3 indices (the current and the 2 stored indices) and store that in `minDistance`. Then, replace the oldest index in the "previously seen" hashmap with the current index, since the furthest index can't possibly produce a smaller distance in the future.
