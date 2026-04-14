class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        #create dic
        dic = {key: list() for key in nums} #line 4
        #print(dic)
        for i, key in enumerate(nums):
            dic[key].append(i) #line 8
            #print(dic)
        #print(dic)
        minDistance = 1000000 #line 11
        for value in dic.values():
            if(len(value) >= 3):
                #find distance
                #2 pointer sliding window
                i = 2#index of value - represents right index
                while i < len(value):
                    minDistance = min((value[i] - value[i-2]) * 2, minDistance)
                    i += 1
        if minDistance == 1000000:
            return -1 #line 21
        return minDistance