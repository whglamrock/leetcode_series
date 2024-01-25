from math import inf
from typing import List

# dp[i][j] means after considered cost[:i], the minimum cost to paint j walls
class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        # dp[i][j] = inf means we won't be able to pain j walls with only considering cost[:i]
        dp = [[inf for j in range(n + 1)] for i in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 0

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                notTake = dp[i - 1][j]
                # if we take i, it buys time[i] amount of time when we can use free painter
                # so total walls painted is time[i] + 1
                take = dp[i - 1][max(j - time[i - 1] - 1, 0)] + cost[i - 1]
                dp[i][j] = min(notTake, take)

        return dp[n][n]


print(Solution().paintWalls([26, 53, 10, 24, 25, 20, 63, 51], [1, 1, 1, 1, 2, 2, 2, 1]))
print(Solution().paintWalls([1, 2, 3, 2], [1, 2, 3, 2]))
print(Solution().paintWalls([2, 3, 4, 2], [1, 1, 1, 1]))
