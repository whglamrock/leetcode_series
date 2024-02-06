from typing import List

# idea exactly same as lc1235: Maximum Profit in Job Scheduling
class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        offers.sort(key=lambda x: x[1])
        n = len(offers)
        # dp[i] means the max profit after reviewing first i offers. the ith offer may or may not be taken
        dp = [0 for i in range(n)]
        dp[0] = offers[0][2]

        for i in range(1, n):
            dp[i] = max(offers[i][2], dp[i - 1])
            j = self.findMaxIndexWithSmallerEnd(offers, i - 1, offers[i][0])
            if j != -1:
                dp[i] = max(dp[i], dp[j] + offers[i][2])

        return max(dp)

    def findMaxIndexWithSmallerEnd(self, offers: List[List[int]], r: int, target: int) -> int:
        l = 0
        while l <= r:
            m = (l + r + 1) // 2
            if l == r:
                if offers[m][1] < target:
                    return m
                else:
                    return -1
            if offers[m][1] >= target:
                r = m - 1
            else:
                l = m

        return -1


print(Solution().maximizeTheProfit(
    5,
    [[0, 0, 1], [0, 1, 3], [1, 1, 4], [0, 2, 2], [1, 3, 2], [2, 3, 1], [4, 4, 8], [2, 4, 18]]))
