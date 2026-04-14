class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        dicton = {} # mmm map
        for i in range(len(nums)):
            if nums[i] not in dicton:
                dicton[nums[i]] = [] # make array at nums[i] in dicton to store copies
            dicton[nums[i]].append(i) # put i as entry

        minDist = -1 # in case find nothing
        for pos in dicton.values(): # just the lists
            if len(pos) >= 3: # skip non triples
                for i in range(len(pos) - 2): # -2 to avoid out of bounds
                    first = pos[i]
                    third = pos[i+2]
                    dist = 2*(third-first)
                    if minDist == -1 or dist < minDist:
                        minDist = dist
        return minDist