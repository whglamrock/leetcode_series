
from collections import deque

# See dp idea at the bottom

# O(N) time & space idea. In real interview this solution would be good enough.

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



'''
# brilliant dp idea to solve the question with at most k transactions 

class Solution(object):
    def maxProfit(self, prices):
    	if not prices or len(prices) == 0:
    		return 0

    	maxProf = 0
    	n = len(prices)
    	k = 2
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
'''
