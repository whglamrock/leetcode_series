
# the only way to avoid TLE in OJ is to use dp

class Solution(object):
    def numDecodings(self, s):

        if not s: return 0

        dp = [0] * (len(s) + 1)
        dp[0] = 1
        if s[0] != '0':
            dp[1] = 1

        for i in xrange(2, len(s) + 1):
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            if '10' <= s[i - 2: i] <= '26':
                dp[i] += dp[i - 2]

        return dp[-1]



'''
# typical DFS solution that got TLE:

class Solution(object):
    def numDecodings(self, s):

        if not s: return 0

        self.ans = 0
        letters = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        def helper(s, path):
            #print s, path
            if not s:
                if path:
                    self.ans += 1
                return
            if s[0] != '0':
                helper(s[1:], path + letters[int(s[0])])
            else:
                return
            if len(s) > 1 and int(s[:2]) <= 26:
                helper(s[2:], path + letters[int(s[:2])])

        helper(s, '')
        return self.ans
'''


