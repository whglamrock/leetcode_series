
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) == 0:
            return 0

        maxProf = 0
        n = len(prices)

        # stupid leetcode will give corner case where k >> n
        if k >= n - 1:
            for i in xrange(n - 1):
                if prices[i + 1] > prices[i]:
                    maxProf += prices[i + 1] - prices[i]
            return maxProf

        # dp[i][j] means maxProfit using i transcations until prices[j]
            # i.e., if we are going to use the ith transactions at prices[j], we sell at j
        dp = [[0 for j in xrange(n)] for i in xrange(k + 1)]

        for i in xrange(1, k + 1):
            # remember at this point we already used i - 1 transactions so we have the maxProfix until each j
            tmpMax = dp[i - 1][0] - prices[0]
            for j in xrange(1, n):
                # consider we sell at j or not
                dp[i][j] = max(dp[i][j - 1], prices[j] + tmpMax)

                # tmpMax is the max of (maxProfix using i - 1 transactions until j, and buy prices[j])
                    # among all previous j's
                tmpMax = max(tmpMax, dp[i - 1][j] - prices[j])
                maxProf = max(maxProf, dp[i][j])

        return maxProf



print Solution().maxProfit(3, [1, 4, 5, 2, 9, 16])
print Solution().maxProfit(2, [7, 1, 5, 3, 6, 4])
print Solution().maxProfit(3, [1, 2, 3, 4, 5])
print Solution().maxProfit(4, [7, 6, 4, 3, 1])