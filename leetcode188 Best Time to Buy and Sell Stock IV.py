from typing import List

# The most important thing is to understand how to set up the tmpMax variable.:
# 1) At transaction i and stock j, you want to sell stock j to gain a profit, but there are a lot of spots
# before j where you can buy.
# 2) We want the the buy price low, but also maximize the total profit gained in previous i - 1 transactions.
# 3) How do you do it? You build variable dp[i - 1][x] + (-prices[x]) and try to maximize it. This way you find the
# best combination of (low prices and big profit with i - 1 transactions before j).
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0

        # to deal with leetcode edge cases where leetcode gives very big k
        if k >= n - 1:
            maxProfit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    # you can still buy and sell stock at the same day
                    maxProfit += prices[i] - prices[i - 1]
            return maxProfit

        dp = [[0 for j in range(n)] for i in range(k + 1)]
        for i in range(1, k + 1):
            tmpMax = -prices[0]
            for j in range(1, n):
                dp[i][j] = max(dp[i][j - 1], tmpMax + prices[j])
                # dp[i - 1][j] means with at most i - 1 transactions the max profit at j - 1
                # any dp[i - 1][j]'s corresponding profit has to correspond to a state where
                # you don't hold any stocks. Thus, you are free to buy stock at j
                tmpMax = max(tmpMax, dp[i - 1][j] - prices[j])

        return dp[-1][-1]


print(Solution().maxProfit(3, [1, 4, 5, 2, 9, 16]))
print(Solution().maxProfit(2, [7, 1, 5, 3, 6, 4]))
print(Solution().maxProfit(3, [1, 2, 3, 4, 5]))
print(Solution().maxProfit(4, [7, 6, 4, 3, 1]))
