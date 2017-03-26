
# keep the min prices of previous days

class Solution(object):
    def maxProfit(self, prices):

        if not prices:
            return 0

        maxprofit = 0
        minprice = prices[0]
        for i in xrange(1, len(prices)):
            newprofit = prices[i] - minprice
            maxprofit = max(maxprofit, newprofit)
            minprice = min(minprice, prices[i])

        return maxprofit



a = [2,6,1,4,9]
Sol = Solution()
print Sol.maxProfit(a)





