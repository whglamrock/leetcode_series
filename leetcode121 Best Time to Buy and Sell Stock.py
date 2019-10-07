
# keep the min prices of previous days

class Solution(object):
    def maxProfit(self, prices):

        if not prices:
            return 0

        ans = 0
        minPrice = 2147483647
        for price in prices:
            minprice = min(minPrice, price)
            ans = max(ans, price - minprice)

        return ans



print Solution().maxProfit([2, 6, 1, 4, 9])





