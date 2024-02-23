from typing import List

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        # dp[i][j] means the max dot product you can get from nums1[:i] & nums2[:j]
        dp = [[-2147483648 for j in range(n + 1)] for i in range(m + 1)]
        maxProduct = -2147483648
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = nums1[i - 1] * nums2[j - 1]
                dp[i][j] = max(dp[i][j], dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + nums1[i - 1] * nums2[j - 1])
                maxProduct = max(maxProduct, dp[i][j])

        return maxProduct
