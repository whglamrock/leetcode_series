from functools import lru_cache
from typing import List


# An untypical knapsack problem, time complexity is O(N * K * log(N)).
class Solution:
    def __init__(self):
        self.events = []

    def maxValue(self, events: List[List[int]], k: int) -> int:
        # sort by end date
        self.events = sorted(events, key=lambda x: x[1])
        n = len(events)
        # dp[i][j] stores the max value after attending at most i events by considering the events[:j + 1]
        dp = [[0 for j in range(n)] for i in range(k + 1)]
        for i in range(1, k + 1):
            dp[i][0] = self.events[0][2]

        for i in range(1, k + 1):
            for j in range(1, n):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], self.events[j][2])
                indexOfLastEarlierEvent = self.findLastEventEndsEarlierThan(self.events[j][0])
                if indexOfLastEarlierEvent == -1:
                    continue
                dp[i][j] = max(dp[i][j], dp[i - 1][indexOfLastEarlierEvent] + self.events[j][2])

        return dp[-1][-1]

    @lru_cache(None)
    def findLastEventEndsEarlierThan(self, target: int) -> int:
        l, r = 0, len(self.events) - 1
        while l <= r:
            m = (l + r + 1) // 2
            if l == r:
                if self.events[m][1] < target:
                    return m
                return -1
            if self.events[m][1] < target:
                l = m
            else:
                r = m - 1

        return -1


print(Solution().maxValue(events=[[1, 2, 4], [3, 4, 3], [2, 3, 1]], k=2))
print(Solution().maxValue(events=[[1, 2, 4], [3, 4, 3], [2, 3, 10]], k=2))
print(Solution().maxValue(events=[[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]], k=3))
