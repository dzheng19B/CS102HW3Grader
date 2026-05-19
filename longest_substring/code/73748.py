2) Communication & Collaboration
    3

3) Implementation & Technical Depth
    4

4) Team Fit & Working Style
    4

Final Evaluation
    15/16

Final Decision
    I am hiring her 

Candidate Form

def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    d = {}
    for i , var in enumerate(nums):
        if var in d and i-d[var] <= k:
            return True
        else:
            d[var]=i
    return False

#time complexity for this solution is O(n). turns list into a dictionary(hashmap), 
#then looped through variables using sliding windows. if satisfies the condition return true
# else add to the dictionary(hashmap) and continue to loop. at the end of the loop if condition
# did not met return false