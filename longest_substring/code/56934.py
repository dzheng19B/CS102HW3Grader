class Solution:

    def lengthofLongestSubstring(s:str) -> int:
        counter = 0
        visited = {}

        for x in s:
            #Base Case
            if (len(s) < 0 || len(s) > 50000){
                        return 0
            }

            if(s{x] != visited):
                counter = counter + 1
                s[x] = visited #Add visited string to the dict.

        return counter