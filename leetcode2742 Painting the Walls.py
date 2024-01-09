from math import inf
from typing import List

# dp[i] means the min cost of painting i walls. See: https://leetcode.com/problems/painting-the-walls/solutions/3650707/java-c-python-7-lines-knapsack-dp/
class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        dp = [0] + [inf] * n

        for i in range(n):
            # the reason we fill dp backwards is because we need to avoid using cost[i] multiple times
            for j in range(n, 0, -1):
                dp[j] = min(dp[j], dp[max(j - time[i] - 1, 0)] + cost[i])
            # print(dp)

        return dp[n]


print(Solution().paintWalls([26, 53, 10, 24, 25, 20, 63, 51], [1, 1, 1, 1, 2, 2, 2, 1]))
print(Solution().paintWalls([1, 2, 3, 2], [1, 2, 3, 2]))
print(Solution().paintWalls([2, 3, 4, 2], [1, 1, 1, 1]))
