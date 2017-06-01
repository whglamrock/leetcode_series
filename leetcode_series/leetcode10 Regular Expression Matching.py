
'''
In this problem, we assume that there is no "." or "*" in s, the p does not start with "*",
there won't be consecutive '*'s in p, the * can only eliminates one preceding char.
Also, the description is vague, without telling that the '*' can actually eliminate one preceding char
'''

# idea from: https://discuss.leetcode.com/topic/22948/my-dp-approach-in-python-with-comments-and-unittest
# In the propagation condition, we can always consider the scenario as that the transformed p[:j]
# lack one char to match the s[:i] so we need to the '*' to clone the preceding char to make
# current p[:j] one char longer. "p[j - 2] == s[i - 1] or p[j - 2] == '.' " means we can clone
# the char p[j - 2] to match s[i - 1].

# For continuous cloning process, consider the clone process of test case 'bbbbb & b*'
# and 'bbbcb & b*'.

class Solution(object):
    def isMatch(self, s, p):

        if s == None or p == None:
            return False

        m, n = len(s), len(p)
        # dp[i][j] defines whether s[:i] matches p[:j]
        dp = [[False for j in xrange(n + 1)] for i in xrange(m + 1)]
        dp[0][0] = True

        for j in xrange(2, n + 1):
            dp[0][j] = dp[0][j - 2] and p[j - 1] == '*'

        for i in xrange(1, m + 1):
            for j in xrange(1, n + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    # it is directly "equals to", not "|="
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':   # in this case j >= 2 because the p won't start with '*'
                    # matches zero chars
                    dp[i][j] |= dp[i][j - 1]
                    # elimination
                    dp[i][j] |= dp[i][j - 2]
                    # when p[:j] is one char short to match s[:i], we need the '*' to propagate p[j - 2]
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] |= dp[i - 1][j]

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




