
"""
This O(n^2) algorithm is based on: every time the substring grows, it can only grow by ONE
charater or TWO. The proof can be found on: https://leetcode.com/discuss/21332/python-o-n-2-method-with-some-optimization-88ms
"""

class Solution(object):
    def longestPalindrome(self, s):

        if (not s) or len(s) == 0:
            return s

        n = len(s)
        maxlen = 1
        start, end = 0, 0
        i = 1
        while i < n:
            if i - maxlen > 0 and s[i - maxlen - 1: i + 1] == s[i - maxlen - 1: i + 1][::-1]:
                start, end = i - maxlen - 1, i
                maxlen += 2
            elif i - maxlen >= 0 and s[i - maxlen: i + 1] == s[i - maxlen: i + 1][::-1]:
                start, end = i - maxlen, i
                maxlen += 1
            #print i, maxlen
            i += 1

        return s[start: end + 1]



Sol = Solution()
s = "bb"
print Sol.longestPalindrome(s)










