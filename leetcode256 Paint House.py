from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        dpRed, dpBlue, dpGreen = [2147483647 for i in range(n)], [2147483647 for i in range(n)], [2147483647 for i in range(n)]
        dpRed[0], dpBlue[0], dpGreen[0] = costs[0][0], costs[0][1], costs[0][2]

        for i in range(1, n):
            dpRed[i] = min(dpBlue[i - 1], dpGreen[i - 1]) + costs[i][0]
            dpBlue[i] = min(dpRed[i - 1], dpGreen[i - 1]) + costs[i][1]
            dpGreen[i] = min(dpBlue[i - 1], dpRed[i - 1]) + costs[i][2]

        return min(dpRed[-1], dpBlue[-1], dpGreen[-1])
