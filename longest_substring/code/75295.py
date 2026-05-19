def lengthOfLongestSubstring(s: str) -> int:
    chars = set()
    max = 0
    left = 0

    for i in range(len(s)):
        while s[i] in chars:
            chars.remove(s[left])
            left += 1
        chars.add(s[i])
        max = len(chars)
    return max

# I chose to create a hashset, which would only store unique characters in it. I defined a variable max for storing the max value, and left so that I could iterate through the string as sort of a sliding window. After iterating through everything, I returned the value stored in max. Should be O(n).