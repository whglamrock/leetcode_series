
# you just need to record last index of a, b, c. The minimum of them is the rightmost left index of such substring
# the leftmost left index of such substring is obviously 0.
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        letterToLastIndex = {}
        ans = 0
        for i, char in enumerate(s):
            letterToLastIndex[char] = i
            if len(letterToLastIndex) == 3:
                rightmostStartIndex = min(letterToLastIndex['a'], letterToLastIndex['b'], letterToLastIndex['c'])
                ans += rightmostStartIndex + 1

        return ans
