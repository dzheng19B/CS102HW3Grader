def lengthOfLongestSubstring(s: str) -> int
    dict = {}
    right, left = 0, 0
    max = 0
    while right < len(s):
        if not s[right] in dict:
            dict[s[right]] = 0
            right+=1
            temp = right - left
            if temp > max:
                max = temp
        else:             left+=1
            del dict[s[left]]

    return max