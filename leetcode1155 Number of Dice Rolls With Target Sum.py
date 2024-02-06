class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [0] * (target + 1)
        for i in range(1, min(k + 1, target + 1)):
            dp[i] = 1

        mod = 10 ** 9 + 7
        for _ in range(n - 1):
            nextDp = [0] * (target + 1)
            for j in range(1, min(k + 1, target + 1)):
                for i in range(1, target + 1):
                    if dp[i] == 0 or i + j > target:
                        continue
                    nextDp[i + j] += dp[i]
                    nextDp[i + j] %= mod
            dp = nextDp

        return dp[target]
