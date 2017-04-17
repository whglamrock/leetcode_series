
# keep the min prices of previous days

class Solution(object):
    def maxProfit(self, prices):

        if not prices:
            return 0

        ans = 0
        minprice = prices[0]
        for price in prices:
            minprice = min(minprice, price)
            ans = max(ans, price - minprice)

        return ans



a = [2,6,1,4,9]
Sol = Solution()
print Sol.maxProfit(a)





