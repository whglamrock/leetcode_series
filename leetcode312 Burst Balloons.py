from typing import List

# an extremely hard DP problem. The interview standards should be coming up with dfs + memoization. optimal O(N^3)
# DP solution isn't a must. See explanation: https://leetcode.com/problems/burst-balloons/solutions/76228/share-some-analysis-and-explanations/
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        # dp[i][j] means the max score by bursting balloons nums[i + 1:j]
        dp = [[0 for j in range(n)] for i in range(n)]

        # k is length of the range of [i:j]
        for k in range(2, n):
            for l in range(n - k):
                r = l + k
                # i loops through the balloons we are actually gonna burst
                # when i == l + 1, dp[l + 1][l] actually means no balloon to burst as (l + 1) + 1 > l - 1
                for i in range(l + 1, r):
                    dp[l][r] = max(dp[l][r], nums[l] * nums[i] * nums[r] + dp[l][i] + dp[i][r])

        return dp[0][n - 1]


print(Solution().maxCoins([2, 1, 9, 3, 6]))
print(Solution().maxCoins([3, 1, 5, 8]))
print(Solution().maxCoins([1, 5]))
print(Solution().maxCoins([5]))
