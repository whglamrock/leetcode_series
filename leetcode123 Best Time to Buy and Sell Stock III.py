from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # get the max profit from selling first stock
        maxFirstProfit = [0] * n
        minFromLeft = prices[0]
        for i in range(1, n):
            maxFirstProfit[i] = max(prices[i] - minFromLeft, maxFirstProfit[i - 1])
            minFromLeft = min(minFromLeft, prices[i])

        # iterate from right to left, get the maxProfit of buying at i
        maxPriceFromRight = prices[-1]
        maxSecondProfit = [0] * n
        for i in range(n - 2, -1, -1):
            maxSecondProfit[i] = max(maxSecondProfit[i + 1], maxPriceFromRight - prices[i])
            maxPriceFromRight = max(maxPriceFromRight, prices[i])

        ans = 0
        for i in range(n):
            if i == 0:
                ans = max(ans, maxSecondProfit[i])
            else:
                ans = max(ans, maxFirstProfit[i - 1] + maxSecondProfit[i])
        return ans


print(Solution().maxProfit([1, 4, 5, 2, 9, 16]))
print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
print(Solution().maxProfit([1, 2, 3, 4, 5]))
print(Solution().maxProfit([7, 6, 4, 3, 1]))
