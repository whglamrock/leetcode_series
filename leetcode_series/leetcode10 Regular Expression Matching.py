'''
In this problem, we assume that there is no "." or "*" in s, the p does not start with "*",
there won't be consecutive '*'s in p, the * can only eliminates one preceding char.
'''

# idea from: https://discuss.leetcode.com/topic/22948/my-dp-approach-in-python-with-comments-and-unittest
# In the propagation condition, we can always consider the scenario as that the transformed p[:i]
# lack one char to match the s[:j] so we need to the '*' to clone the preceding char to make
# current p[:i] one char longer. "p[i - 2] == s[j - 1] or p[i - 2] == '.' " means we can clone
# the char p[i - 2] to match s[j - 1], "dp[i][j - 1] = True" means p[:i] matches s[:j - 1]

# For continuous cloning process, consider the clone process of test case 'bbbbb & b*'
# and 'bbbcb & b*'.

class Solution(object):
    def isMatch(self, s, p):

        dp = [[False for j in xrange(len(s) + 1)] for i in xrange(len(p) + 1)]
        dp[0][0] = True

        for i in xrange(2, len(p) + 1):
            dp[i][0] = dp[i - 2][0] and p[i - 1] == '*'  # elimination

        for i in xrange(1, len(p) + 1):
            for j in xrange(1, len(s) + 1):
                if p[i - 1] == s[j - 1] or p[i - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[i - 1] == '*':
                    # elimination (when * matches zero of the preceding element or eliminates
                    # the preceding element). e.g., 'ab & ab*' and 'a & ab*'
                    dp[i][j] = dp[i - 1][j] or dp[i - 2][j]
                    # the propagation propagates not the element but the matching status
                    # the following if statement rules out the elimination case like "aab & c*a*b"
                    # when we need to kill the preceding unmatched char pairs, but the
                    # test case like "bb & bbb*" also accords to this condition
                    if i >= 2 and (p[i - 2] == s[j - 1] or p[i - 2] == '.'):
                        # dp[i][j] |= dp[i - 1][j - 1] doesn't work
                        # try test case: "aaa & .*", "bbb & b*"
                        dp[i][j] |= dp[i][j - 1]

        return dp[-1][-1]



a = 'aba'
b = '.*'
c = 'bb'
d = 'bbb*'  # or 'bbbb*'
Sol = Solution()
print Sol.isMatch(a,b)
print Sol.isMatch(c,d)



'''
# practice:

class Solution(object):
    def isMatch(self, s, p):

        if s == None or p == None:
            return False

        m, n = len(s), len(p)
        # dp[i][j] means whether s[:i] matches p[:j]
        dp = [[False for j in xrange(n + 1)] for i in xrange(m + 1)]
        dp[0][0] = True

        # elimination and propagation
        for j in xrange(2, n + 1):
            dp[0][j] = dp[0][j - 2] and p[j - 1] == '*'

        for i in xrange(1, m + 1):
            for j in xrange(1, n + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] |= dp[i][j - 1]
                    dp[i][j] |= dp[i][j - 2]
                    if j >= 2 and p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] |= dp[i - 1][j]

        return dp[-1][-1]
'''




