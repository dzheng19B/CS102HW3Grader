def lengthOfLongestSubstring(s):
    left, max_len = 0, 0
    x = set()
    for i in range(len(s)):
        while s[i] in x:
            x.remove(s[left])
            left += 1
        x.add(s[i])
        max_len = max(max_len, i - left + 1)
    return max_len
