from typing import List


# O(N * target) time solution. There is no way you can do better.
class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        # dp[i] stores the max length of subsequence that sums up to i
        dp = [-1] * (target + 1)
        dp[0] = 0
        for i, num in enumerate(nums):
            if num > target:
                continue
            # need to go backwards to avoid incorrect update
            for j in range(target, num - 1, -1):
                if dp[j - num] == -1:
                    continue
                dp[j] = max(dp[j], dp[j - num] + 1)

        return dp[-1]
