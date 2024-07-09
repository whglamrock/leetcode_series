from typing import List


# Below is the one DP array solution, where dp[i] stores the max money you can rob by considering the first i houses
# You can also use 2 dp array: dp1[i] = max money by robbing house i, dp2[i] = max money by not robbing house i.
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        if len(nums) > 1:
            dp[1] = max(nums[1], nums[0])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]


print(Solution().rob([2, 7, 1, 3, 9]))
print(Solution().rob([1, 2, 3, 1]))
