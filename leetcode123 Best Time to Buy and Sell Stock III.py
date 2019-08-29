
from collections import deque

# O(N) time & space idea. In real interview this solution would be good enough.
# See DP idea for generalized question for k transactions: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/39608/A-clean-DP-solution-which-generalizes-to-k-transactions

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) == 1:
            return 0
        n = len(prices)

        # get a curr minimum from left to right
        mins = []
        currMin = 2147483647
        for i in xrange(n):
            currMin = min(currMin, prices[i])
            mins.append(currMin)

        # get a curr maximum from right to left
        maxs = deque()
        currMax = -2147483648
        for i in xrange(n - 1, -1, -1):
            currMax = max(currMax, prices[i])
            maxs.appendleft(currMax)

        # if we sell stock at day i, what's maxProfit if we buy it in any day earlier
        maxProfitLeftToRight = []
        for i in xrange(n):
            maxProfitLeftToRight.append(prices[i] - mins[i])

        # if we buy stock at day i, what's maxProfit if we sell in any day later
        maxProfitRightToLeft = deque()
        for i in xrange(n - 1, -1, -1):
            maxProfitRightToLeft.appendleft(maxs[i] - prices[i])

        # the maxProfit of buy 1 and sell 1 in days <= i
        maxProfitInLeft = []
        currMax = -2147483648
        for i in xrange(n):
            currMax = max(currMax, maxProfitLeftToRight[i])
            maxProfitInLeft.append(currMax)

        # the maxProfit of buy 1 and sell 1 in days >= i
        maxProfitInRight = deque()
        currMax = -2147483648
        for i in xrange(n - 1, -1, -1):
            currMax = max(currMax, maxProfitRightToLeft[i])
            maxProfitInRight.appendleft(currMax)

        return max([(maxProfitInLeft[i] + maxProfitInRight[i]) for i in xrange(n)])



print Solution().maxProfit([1, 4, 5, 2, 9, 16])
print Solution().maxProfit([7, 1, 5, 3, 6, 4])
print Solution().maxProfit([1, 2, 3, 4, 5])
print Solution().maxProfit([7, 6, 4, 3, 1])
