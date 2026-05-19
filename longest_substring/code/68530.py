def lengthOfLongestSubstring(s: str) -> int:
    set_of_chars = set() #create a HashSet to track chars (make sure no repeats)
    left = 0 #track elements (2-pointer method start left pointer at index 0)
    length = 0 #keep track of return value (start at 0)
    for i in range(len(s)): #iterate through the elements(characters) of the given string s 
        while s[i] in set_of_chars: # if the element is in the set, execute the following
            set_of_chars.remove(s[left]) #remove the character from the set 
            left += 1 #increment left pointer 
        set_of_chars.add(s[i]) #add the element back to set after removing duplicates  
        length = max(length, i - left + 1) # to return the correct length, take max 
        #of the current length and (the difference between the right and left pointer indices + 1)  
    return length #return the length of the string without duplicates 
# time complexity is O(n) because I utilized a HashSet and iterated through each element in the given string using # the two-pointer method (the left pointer starts at zero and increments by 1 to the right)