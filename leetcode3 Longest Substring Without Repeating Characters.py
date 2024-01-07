class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        l, r = 0, 0
        n = len(s)

        maxLen = 0
        while r < n:
            if s[r] in window:
                prevIndex = window[s[r]]
                while l <= prevIndex:
                    del window[s[l]]
                    l += 1
            window[s[r]] = r
            r += 1
            maxLen = max(maxLen, len(window))

        return maxLen


print(Solution().lengthOfLongestSubstring('abba'))
print(Solution().lengthOfLongestSubstring('abceba'))
print(Solution().lengthOfLongestSubstring('pwwkew'))