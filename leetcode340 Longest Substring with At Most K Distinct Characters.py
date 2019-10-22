
from collections import defaultdict, deque

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s:
            return 0

        letterToIndices = defaultdict(deque)
        l = 0
        maxLen = 0

        for i, char in enumerate(s):
            letterToIndices[char].append(i)
            while len(letterToIndices) > k:
                leftChar = s[l]
                letterToIndices[leftChar].popleft()
                if not letterToIndices[leftChar]:
                    del letterToIndices[leftChar]
                l += 1
            maxLen = max(maxLen, i - l + 1)

        return maxLen



print Solution().lengthOfLongestSubstringKDistinct('eceba', 3)
print Solution().lengthOfLongestSubstringKDistinct('eceba', 6)
print Solution().lengthOfLongestSubstringKDistinct('aa', 1)
