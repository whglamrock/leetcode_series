from typing import List

class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
        dp = [0] * (budget + 1)
        for currPrice, futurePrice in zip(present, future):
            profit = futurePrice - currPrice
            # the reason we need to loop through the amount we spent on current stock is because
            # dp[i - currPrice] is from the previous round.
            for i in range(budget, currPrice - 1, -1):
                dp[i] = max(dp[i], dp[i - currPrice] + profit)

        return dp[-1]
