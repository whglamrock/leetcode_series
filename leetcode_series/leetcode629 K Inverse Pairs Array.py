
# see explanation from: https://discuss.leetcode.com/topic/93815/java-dp-o-nk-solution/9

class Solution(object):
    def kInversePairs(self, n, k):

        if k > n * (n - 1) / 2 or k < 0:
            return 0
        if k == n * (n - 1) / 2 or k == 0:  # contains the case when n == 1
            return 1

        dp = [[0 for j in xrange(k + 1)] for i in xrange(n + 1)]
        dp[2][0] = 1
        dp[2][1] = 1
        bigmodnumber = 10 ** 9 + 7

        # According to the deduction,
        #   dp[n][k] = dp[n - 1][k] + dp[n - 1][k - 1] + dp[n - 1][k - 2] + ... + dp[n - 1][k - (n - 1)]
        #   so replacing k with k + 1, we can have:
        #   dp[n][k + 1] = dp[n - 1][k + 1] + dp[n - 1][k], dp[n - 1][k + 1] + ... + dp[n - 1][k + 1 - (n - 1)]
        # then dp[n][k + 1] = dp[n - 1][k + 1] + dp[n][k] - dp[n - 1][k - (n - 1)]
        # we can analogize n to i, j to k + 1: dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - i]
        for i in xrange(3, n + 1):
            dp[i][0] = 1
            for j in xrange(1, min(k, i * (i - 1) / 2) + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                # when j < i, dp[i - 1][j - i] would be invalid, so in practice dp[i - 1][j - i] would be 0
                if j >= i:
                    dp[i][j] -= dp[i - 1][j - i]
                # remember this weird operation to handle overflow big numbers
                dp[i][j] = (dp[i][j] + bigmodnumber) % bigmodnumber

        return dp[n][k]



Sol = Solution()
print Sol.kInversePairs(7, 10)


