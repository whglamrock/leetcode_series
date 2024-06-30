from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        # dp[i][j] means the length of the longest common suffix of nums1[:i] and nums2[:j]
        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1

        maxLen = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                maxLen = max(maxLen, dp[i][j])

        return maxLen


print(Solution().findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]))
