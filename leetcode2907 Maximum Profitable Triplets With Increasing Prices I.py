from typing import List

# the O(N * log(N)) segment tree solution is way too overkill for a real interview.
class Solution:
    def maxProfit(self, prices: List[int], profits: List[int]) -> int:
        n = len(prices)
        # initially stores the max profit after choosing 2 indexes
        dp = [-1] * n
        for i in range(1, n):
            for j in range(i):
                if prices[i] > prices[j]:
                    dp[i] = max(dp[i], profits[i] + profits[j])

        # get the max profit after choosing 3 indexes
        nextDp = [-1] * n
        for i in range(2, n):
            for j in range(1, i):
                if dp[j] == -1 or prices[i] <= prices[j]:
                    continue
                nextDp[i] = max(nextDp[i], dp[j] + profits[i])

        return max(nextDp)
