def lengthOfLongestSubstring(s: str) -> int:
    charSet = set()
    result = 0
    length = len(s)
    left = 0
    
    for right in range(length):
        while s[right] in charSet:
            charSet.remove(s[left])
            left += 1
        charSet.add(s[right])
        result = max(result, right - left + 1)
    return result