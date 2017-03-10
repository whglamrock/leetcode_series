
# Question from: http://www.lintcode.com/zh-cn/problem/dices-sum/

class Solution:
    # @param {int} n an integer
    # @return {tuple[]} a list of tuple(sum, probability)
    def dicesSum(self, n):

        if not n:
            return []

        dp = [0 for i in xrange(6 * n + 1)]
        for i in xrange(1, 7):
            dp[i] = 1

        for i in xrange(2, n + 1):
            newdp = [0 for _ in xrange(6 * n + 1)]
            for j in xrange(6 * n + 1):
                if dp[j] != 0:
                    for k in xrange(1, 7):
                        if j + k < 6 * n + 1:
                            newdp[j + k] += dp[j]
            dp = newdp

        dividee = 6 ** n
        ans = []
        for i, count in enumerate(dp):
            if count != 0:
                ans.append([i, float(count) / float(dividee)])

        return ans