
"""
O(n^2) time & space. palindrome can only grow from palindromes. Ultimately the most basic palindrome forms from
1 char or r chars
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''

        n = len(s)
        # dp[i][j] means whether s[i: j + 1] is a palindrome
        dp = [[0 for j in xrange(n)] for i in xrange(n)]
        for i in xrange(n):
            dp[i][i] = 1

        # deal with situation like 'aa', 'bb'
        for i in xrange(1, n):
            if s[i] == s[i - 1]:
                dp[i - 1][i] = 1

        # then all palingdromes can grow from 1 char or 2 chars
        # the new palinfromes found from this point will be at least 3 chars long
        for i in xrange(2, n):
            for j in xrange(1, i):
                if dp[j][i - 1] == 1 and s[j - 1] == s[i]:
                    dp[j - 1][i] = 1

        maxLen = 0
        ans = [0, 0]
        for i in xrange(n):
            for j in xrange(i, n):
                if dp[i][j] == 1 and j - i > maxLen:
                    ans = [i, j]
                    maxLen = j - i

        return s[ans[0]: ans[1] + 1]



Sol = Solution()
s = "bb"
print Sol.longestPalindrome(s)










