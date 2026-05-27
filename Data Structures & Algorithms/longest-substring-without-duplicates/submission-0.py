class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxlen = 0
        last = {}

        for right in range(len(s)):
            if s[right] in last and last[s[right]] >= left:
                left = last[s[right]] + 1

            last[s[right]] = right
            maxlen = max(maxlen, right - left + 1)

        return maxlen
