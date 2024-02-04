from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [2147483647] * 366
        dp[0] = 0
        daysSet = set(days)
        for i in range(1, days[-1] + 1):
            if i not in daysSet:
                dp[i] = dp[i - 1]
                continue
            # buy one day pass
            dp[i] = dp[i - 1] + costs[0]
            # buy weekly pass
            dp[i] = min(dp[i], dp[max(i - 7, 0)] + costs[1])
            dp[i] = min(dp[i], dp[max(i - 30, 0)] + costs[2])

        return dp[days[-1]]
