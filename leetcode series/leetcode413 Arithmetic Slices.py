# the second for loop is the most important one.
class Solution(object):
    def numberOfArithmeticSlices(self, A):

        if (not A) or len(A) < 3:
            return 0

        dp = [0] * len(A)
        ans = 0
        for i in xrange(2, len(A)):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                dp[i] = dp[i - 1] + 1

        for i in xrange(2, len(dp)):
            if dp[i] > 0:
                dp[i] = (dp[i] + 1) * dp[i] / 2

        #print dp
        for i in xrange(2, len(dp)):
            if dp[i] > 0:
                ans += dp[i] - dp[i - 1]

        return ans

