from typing import List

# O(n * k) time dp solution. There is no way to do better than this.
class Solution:
    def maxSumAfterPartitioning(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # dp[i] means max of such sum after partitioning nums[:i + 1]
        dp = [0] * n
        dp[0] = nums[0]

        for i in range(1, n):
            maxOfK = nums[i]
            # j is the starting index of last partition
            for j in range(i, max(-1, i - k), -1):
                maxOfK = max(maxOfK, nums[j])
                if j == 0:
                    dp[i] = max(dp[i], maxOfK * (i - j + 1))
                else:
                    dp[i] = max(dp[i], dp[j - 1] + maxOfK * (i - j + 1))

        return dp[-1]
