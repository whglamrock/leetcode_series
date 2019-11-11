
# O(n) time, O(1) space solution

class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if not prices or len(prices) < 2:
            return 0

        n = len(prices)
        has0, has1 = 0, -prices[0]

        for i in xrange(1, n):
            prev_has0, prev_has1 = has0, has1
            has0 = max(prev_has0, prev_has1 + prices[i] - fee)
            has1 = max(prev_has1, prev_has0 - prices[i])

        return has0



print Solution().maxProfit([1, 3, 2, 8, 4, 9], 2)
