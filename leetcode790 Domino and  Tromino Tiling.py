
# it shouldn't be too hard to deduct from drawing the tiles that:
# dp[n] = dp[n - 1] + dp[n - 2] + 2 * (dp[n - 3] + ... + d[0]), but we need can simply the equation into:
# dp[n] = 2 * dp[n - 1] + dp[n - 3]. See: https://leetcode.com/problems/domino-and-tromino-tiling/solutions/116581/detail-and-explanation-of-o-n-solution-why-dp-n-2-d-n-1-dp-n-3/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def numTilings(self, n: int) -> int:
        # n can be at most 1000
        dp = [0] * (1000 + 1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        dp[3] = 5
        for i in range(4, n + 1):
            dp[i] = 2 * dp[i - 1] + dp[i - 3]

        return dp[n] % (10 ** 9 + 7)


print(Solution().numTilings(88))
