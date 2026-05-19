def lengthOfLongestSubstring(s):
    left = 0
    maxlength = 0
    substring = set()

    for right in range(len(s)):
        while s[right] in substring:
            substring.remove(s[left])
            left+=1
        substring.add(s[right])
        maxlength = max(substring, right - left + 1)

    return maxlength

# Michael DiNapoli O(n^2)