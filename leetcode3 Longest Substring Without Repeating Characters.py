
# it's easy to think of sliding window idea. P.S.: the only tricky point is to remember to
    # compare the l with the previous l. e.g., "abba"

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        l = 0
        maxLen = 0
        letterToIndex = {}

        for i, c in enumerate(s):
            if c in letterToIndex:
                j = letterToIndex[c]
                # important!, don't forget to compare l with j + 1
                l = max(l, j + 1)
            letterToIndex[c] = i
            maxLen = max(maxLen, i - l + 1)
            # print l, i

        return maxLen



print Solution().lengthOfLongestSubstring('abba')
print Solution().lengthOfLongestSubstring('abceba')
print Solution().lengthOfLongestSubstring('pwwkew')