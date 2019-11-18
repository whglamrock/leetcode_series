
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) < 2:
            return 0

        n = len(prices)

        # stupid leetcode will give corner case where k >> n
        if k >= n - 1:
            maxProfix = 0
            for i in xrange(1, n):
                if prices[i] > prices[i - 1]:
                    maxProfix += prices[i] - prices[i - 1]
            return maxProfix

        # use k + 1 instead of k is for easy reference of dp[i - 1][j]
        # dp[i][j] means with i transactions the maxProfit we can get at j (we don't have to sell at j
            # and it's possible that we have used up i transactions before j)
        # Most importantly, since dp[i][j] means the maxProfit, at that point we must have no stock in hand
        dp = [[0 for j in xrange(n)] for i in xrange(k + 1)]

        for i in xrange(1, k + 1):
            tmpMax = dp[i - 1][0] - prices[0]
            for j in xrange(1, n):
                # consider we sell at j or (we can't do anything we using up i transactions at j - 1)
                dp[i][j] = max(dp[i][j - 1], tmpMax + prices[j])
                # tmpMax is the max of (maxProfit using i - 1 transactions until j, and buy prices[j])
                    # among all previous j's
                # this step can also be placed above the dp[i][j] update
                tmpMax = max(tmpMax, dp[i - 1][j] - prices[j])

        return dp[-1][-1]



print Solution().maxProfit(3, [1, 4, 5, 2, 9, 16])
print Solution().maxProfit(2, [7, 1, 5, 3, 6, 4])
print Solution().maxProfit(3, [1, 2, 3, 4, 5])
print Solution().maxProfit(4, [7, 6, 4, 3, 1])