
# most important thing is find the range of previous states where we generate dp[i] from. i.e., not how many times A[j]
    # is used in this block, but rather how long the current block(that ends with A[j], inclusive) can be

class Solution(object):
    def maxSumAfterPartitioning(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        n = len(A)
        dp = [0] * n

        for i in xrange(K):
            dp[i] = max(A[:i + 1]) * (i + 1)

        for i in xrange(K, n):
            maxFromRightToLeft = 0
            # j iterate from i - 1 to i - K
            for j in range(i - K, i)[::-1]:
                maxFromRightToLeft = max(maxFromRightToLeft, A[j + 1])
                dp[i] = max(dp[i], dp[j] + maxFromRightToLeft * (i - j))

        return dp[-1]