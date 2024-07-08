from typing import List


# the trick for O(NK) solution is maintaining the min & second min cost of the previous house, and their corresponding colors
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n, k = len(costs), len(costs[0])
        # dp[i][j] means the min cost of painting i houses where the ith house is in color j
        dp = [[2147483647 for j in range(k)] for i in range(n)]
        for j in range(k):
            dp[0][j] = costs[0][j]

        for i in range(1, n):
            minPrevCost, secondMinPrevCost = 2147483647, 2147483647
            minPrevCostColor, secondMinPrevCostColor = -1, -1
            # find the min and second min cost for (i - 1)'th house
            for j in range(k):
                if dp[i - 1][j] < minPrevCost:
                    secondMinPrevCost = minPrevCost
                    secondMinPrevCostColor = minPrevCostColor
                    minPrevCost = dp[i - 1][j]
                    minPrevCostColor = j
                elif dp[i - 1][j] < secondMinPrevCost:
                    secondMinPrevCost = dp[i - 1][j]
                    secondMinPrevCostColor = j

            for j in range(k):
                if j == minPrevCostColor:
                    dp[i][j] = dp[i - 1][secondMinPrevCostColor] + costs[i][j]
                else:
                    dp[i][j] = dp[i - 1][minPrevCostColor] + costs[i][j]

        return min(dp[-1])


print(Solution().minCostII([[1, 5, 3], [2, 9, 4]]))
print(Solution().minCostII([[1, 3], [2, 4]]))
print(Solution().minCostII([
    [15, 17, 15, 20, 7, 16, 6, 10, 4, 20, 7, 3, 4],
    [11, 3, 9, 13, 7, 12, 6, 7, 5, 1, 7, 18, 9]]))
