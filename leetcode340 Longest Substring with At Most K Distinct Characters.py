from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0

        window = defaultdict(int)
        l = 0
        maxLen = 1
        for r, char in enumerate(s):
            window[char] += 1
            while len(window) > k:
                window[s[l]] -= 1
                if not window[s[l]]:
                    del window[s[l]]
                l += 1
            maxLen = max(r - l + 1, maxLen)

        return maxLen


print(Solution().lengthOfLongestSubstringKDistinct('eceba', 3))
print(Solution().lengthOfLongestSubstringKDistinct('eceba', 6))
print(Solution().lengthOfLongestSubstringKDistinct('aa', 1))
