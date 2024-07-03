from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        # dp[i][j] means number of combinations to reach amount j with at most i coins;
        dp = [[0 for j in range(amount + 1)] for i in range(n + 1)]
        # we always have one way to reach amount 0
        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(1, n + 1):
            coin = coins[i - 1]
            for j in range(1, amount + 1):
                dp[i][j] = dp[i - 1][j]
                if j - coin >= 0:
                    dp[i][j] += dp[i][j - coin]

        return dp[-1][-1]


print(Solution().change(5, [1, 2, 5]))
