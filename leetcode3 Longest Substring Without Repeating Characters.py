class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        l = 0
        ans = 0
        for r, char in enumerate(s):
            if char in window:
                prevIndex = window[char]
                while l <= prevIndex:
                    del window[s[l]]
                    l += 1
            window[char] = r
            ans = max(ans, r - l + 1)

        return ans


print(Solution().lengthOfLongestSubstring('abba'))
print(Solution().lengthOfLongestSubstring('abceba'))
print(Solution().lengthOfLongestSubstring('pwwkew'))