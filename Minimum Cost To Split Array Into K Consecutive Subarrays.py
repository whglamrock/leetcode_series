from typing import List

# Below solution is O(k * n * n). We may have room to further optimize, tho
class Solution:
    def minCostToSplitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # dp[i][j] means the min cost to split nums[:j + 1] into i parts
        dp = [[2147483647 for j in range(n)] for i in range(k + 1)]
        # when i == 1
        prefixMax = nums[0]
        for j in range(n):
            prefixMax = max(prefixMax, nums[j])
            dp[1][j] = prefixMax
            dp[0][j] = 0

        for i in range(2, k + 1):
            # j is the right index of the last subarray
            for j in range(i - 1, n):
                lastCost = nums[j]
                # jj is the left index of the last subarray
                for jj in range(j, i - 2, -1):
                    lastCost = max(lastCost, nums[jj])
                    dp[i][j] = min(dp[i][j], dp[i - 1][jj - 1] + lastCost)

        return dp[k][n - 1]


print(Solution().minCostToSplitArray([150, 200, 400, 350, 250], 3))

