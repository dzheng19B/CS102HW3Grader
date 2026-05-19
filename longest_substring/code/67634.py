def lengthOfLongestSubstring(s: str) -> int:

    l = 0

    windowSum = 0

    h = set()

    for right in range(len(s)):
        while s[right] in h:
            h.remove(s[l])
            l += 1
        h.add(s[right])
        windowSum = max(windowSum, right - l + 1)

    return windowSum