class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1
        mn = -1

        dist = {}
        
        for i, val in enumerate(nums):
            if val in dist:
                dist[val].append(i)
            else:
                dist[val] = [i]
        
            
        for key, val in dist.items():
            if len(val) < 3:
                continue
            i = 0
            i1 = 2

            while (i1 < len(val)):
                tmp = 2*(val[i1] - val[i])
                if tmp < mn or mn == -1:
                    mn = tmp
                i+=1
                i1+=1
          
        return mn