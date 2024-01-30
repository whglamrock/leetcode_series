from collections import deque
from typing import List

class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n, k = len(costs), len(costs[0])
        # dp[i][j] means the min cost of painting i houses and the ith house is painted with color j
        dp = [[2147483647 for j in range(k)] for i in range(n + 1)]
        for j in range(k):
            dp[0][j] = 0

        minCostFromLeft, minCostFromRight = [], deque()
        for i in range(1, n + 1):
            currMin = 2147483647
            nextMinCostFromLeft, nextMinCostFromRight = [], deque()
            for j in range(k):
                if not minCostFromLeft:
                    dp[i][j] = dp[i - 1][j] + costs[i - 1][j]
                else:
                    if j - 1 >= 0:
                        dp[i][j] = min(dp[i][j], minCostFromLeft[j - 1] + costs[i - 1][j])
                    if j + 1 < k:
                        dp[i][j] = min(dp[i][j], minCostFromRight[j + 1] + costs[i - 1][j])
                currMin = min(currMin, dp[i][j])
                nextMinCostFromLeft.append(currMin)

            # scanning from right to left
            currMin = 2147483647
            for j in range(k - 1, -1, -1):
                currMin = min(currMin, dp[i][j])
                nextMinCostFromRight.appendleft(currMin)

            minCostFromLeft, minCostFromRight = nextMinCostFromLeft, nextMinCostFromRight

        return min(dp[-1])


print(Solution().minCostII([[1, 5, 3], [2, 9, 4]]))
print(Solution().minCostII([[1, 3], [2, 4]]))
print(Solution().minCostII([
    [15, 17, 15, 20, 7, 16, 6, 10, 4, 20, 7, 3, 4],
    [11, 3, 9, 13, 7, 12, 6, 7, 5, 1, 7, 18, 9]]))
