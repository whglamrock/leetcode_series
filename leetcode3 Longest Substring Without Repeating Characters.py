
# it's easy to think of sliding window idea. the only tricky point is to remember to
    # compare the l with the previous l. e.g., "abba"

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        l, r = 0, 0
        ans = 0
        letterToIndex = {}

        for i, char in enumerate(s):
            if char not in letterToIndex:
                r = i
            else:
                # don't forget to compare with the previous l
                l = max(l, letterToIndex[char] + 1)
                r = i

            # print l, r
            letterToIndex[char] = i
            ans = max(r - l + 1, ans)

        return ans



print Solution().lengthOfLongestSubstring('abba')
print Solution().lengthOfLongestSubstring('abceba')
print Solution().lengthOfLongestSubstring('pwwkew')