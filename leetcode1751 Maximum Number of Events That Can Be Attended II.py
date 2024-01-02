from functools import lru_cache
from typing import List

# the time complexity for knapsack problem is O(n * k), so the overall complexity here is O(n * log(n) + n * k)
class Solution:
    def __init__(self):
        self.events = []

    def maxValue(self, events: List[List[int]], k: int) -> int:
        self.events = events
        self.events.sort(key=lambda x: x[1])
        return self.dfs(k, len(self.events) - 1, 0)

    @lru_cache(None)
    def dfs(self, k: int, i: int, profit: int) -> int:
        if k == 0 or i < 0:
            return profit

        # initialize if with case where we don't use events[i]
        maxProfit = self.dfs(k, i - 1, profit)
        maxIndexEarlier = self.findMaxIndexSmallerOrEqualThan(self.events[i][0], 0, i - 1)
        if maxIndexEarlier != -1:
            profitOfUsingI = self.dfs(k - 1, maxIndexEarlier, profit + self.events[i][2])
            maxProfit = max(maxProfit, profitOfUsingI)

        else:
            maxProfit = max(maxProfit, profit + self.events[i][2])
        return maxProfit

    def findMaxIndexSmallerOrEqualThan(self, target: int, l: int, r: int) -> int:
        while l <= r:
            if l == r:
                if self.events[l][1] >= target:
                    return -1
                else:
                    return l
            m = (l + r + 1) // 2
            if self.events[m][1] >= target:
                r = m - 1
            else:
                l = m

        return -1


print(Solution().maxValue(events=[[1, 2, 4], [3, 4, 3], [2, 3, 1]], k=2))
print(Solution().maxValue(events=[[1, 2, 4], [3, 4, 3], [2, 3, 10]], k=2))
print(Solution().maxValue(events=[[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]], k=3))
