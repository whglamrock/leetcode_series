from typing import List

class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
        dp = [0] * (budget + 1)
        for currPrice, futurePrice in zip(present, future):
            profit = futurePrice - currPrice
            if profit <= 0:
                continue
            # the reason we need to loop backwards through the amount we spent on current stock is because
            # dp[i - currPrice] is from the previous round.
            for i in range(budget, currPrice - 1, -1):
                dp[i] = max(dp[i], dp[i - currPrice] + profit)

        return dp[-1]


'''
# more straightforward cached dfs solution that's definitely OK in real interview but got TLE in stupid leetcode
class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
        self.prices = []
        for currPrice, futurePrice in zip(present, future):
            profit = futurePrice - currPrice
            if profit <= 0:
                continue
            self.prices.append([currPrice, profit])
        
        return self.dfs(0, budget)
    
    @lru_cache(None)
    def dfs(self, index: int, budget: int) -> int:
        if index >= len(self.prices) or budget < 0:
            return 0
        
        maxProfit = 0
        for i in range(index, len(self.prices)):
            currPrice, profit = self.prices[i]
            if budget >= currPrice:
                maxProfit = max(maxProfit, profit + self.dfs(i + 1, budget - currPrice))
        
        return maxProfit
'''