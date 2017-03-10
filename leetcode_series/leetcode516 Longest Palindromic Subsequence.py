
# REMEMBER THIS SOLUTION FOR REAL INTERVIEW

# A non-dp fast solution
# still O(n^2) time complexity because of the string slicing operator but much faster
#   with memoization and dealing with string(instead of dp list)

class Solution(object):
    def longestPalindromeSubseq(self, s):

        if not s: return 0
        dic = {}

        def helper(s):

            if s not in dic:
                maxL = 0
                for c in set(s):
                    i, j = s.find(c), s.rfind(c)
                    if i != j:
                        maxL = max(maxL, 2 + helper(s[i + 1:j]))
                    else:
                        maxL = max(maxL, 1)
                dic[s] = maxL

            return dic[s]

        return helper(s)



Sol = Solution()
s = 'abasfba'
print Sol.longestPalindromeSubseq(s)



'''
# standard dp solution that can pass in real interview but got TLE in fucking stupid leetcode

class Solution(object):
    def longestPalindromeSubseq(self, s):

        if not s:
            return 0

        n = len(s)
        dp = [[1 for j in xrange(n)] for i in xrange(n)]

        for i in xrange(1, len(s)):
            for j in xrange(i - 1, -1, -1):
                if s[i] == s[j]:
                    dp[j][i] = dp[j + 1][i - 1] + 2 if i - j > 1 else 2
                else:
                    dp[j][i] = max(dp[j][i - 1], dp[j + 1][i])

        return dp[0][-1]
'''
