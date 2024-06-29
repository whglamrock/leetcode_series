from typing import List


# Intuition came from: https://leetcode.com/problems/selling-pieces-of-wood/solutions/2168148/java-c-python-bottom-up-dp/
# 1) One key sentence: "To cut a piece of wood, you must make a vertical or horizontal cut across the entire height
# or width of the piece to split it into two smaller pieces"
# 2) Also, we need to be able to realize that the shape we cut in the middle of the board == the shape in top left corner
# so we can have transition formula: dp[h][w] = max(dp[h][w], dp[a][w] + dp[h - a][w]) where the h - a part is considered
# to be moved to the top left corner.
class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
        for h, w, p in prices:
            dp[h][w] = p

        for h in range(1, m + 1):
            for w in range(1, n + 1):
                # a is where we cut
                for a in range(1, h + 1):
                    dp[h][w] = max(dp[h][w], dp[a][w] + dp[h - a][w])
                for a in range(1, w + 1):
                    dp[h][w] = max(dp[h][w], dp[h][a] + dp[h][w - a])

        return dp[m][n]
