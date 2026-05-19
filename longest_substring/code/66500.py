# Dominic Vega

# Athulya Santhosh (Interviewer)

# Candidate Form

def lengthOfLongestSubstring(s: str) -> int:
    # init some variables
    letter_map = {}
    left_ptr = 0
    right_ptr = 0
    longest_sub = 0

    # empty string case
    if (str == ""): return 0

    # run through string, visiting each character once (O(n))
    for (right_ptr in range(len(str))):
        # what is the last time we saw this character? if it hasn't appeared, last_seen is None
        last_seen = letter_map.get(str[right_ptr])

        # if we've seen this character and the last time we saw it was in our window, adjust window
        if (last_seen != None and last_seen >= left_ptr):
            left_ptr = last_seen + 1
    
        # set the last time we've seen this letter to where it is right now
        letter_map[str[right_ptr]] = right_ptr
    
        # the longest substring is either what it currently is or the length of the current window
        longest_sub = max(longest_sub, right_ptr-left_ptr+1)

    #zhe returnne
    return longest_sub