def lengthOfLongestSubstring(s: str) -> int:
    left = maxLength = 0
    # right = 0
    stringSet = set()

    for right in range (len(s)):
        while s[right] in stringSet:
            stringSet.remove(s[left])
            left += 1

        stringSet.add(s[right])
        maxLength = max(maxLength, right - left + 1)

    return maxLength

# Approaching this problem using sliding window + set 
# The time complexity is O(n), even though there is a nested while loop, it's still in linear time since each character
# is added and removed at most once. The right pointer goes through everything and left goes through it n times
# The space complexity is O(min(n,k)) since  the memory usage depends on the smaller input of n, k