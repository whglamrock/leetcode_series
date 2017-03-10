# instruction is super unclear, actually you can sell/buy one stock within the same day without cooldown.
class Solution(object):
    def maxProfit(self, prices):

        if (not prices): return 0

        i = len(prices)-1
        maxprof = 0
        while i > 0:
            if prices[i] - prices[i-1] > 0:
                maxprof += prices[i] - prices[i-1]
            i -= 1

        return maxprof

Sol = Solution()
prices = [1,4,5,2,9,16]
print Sol.maxProfit(prices)