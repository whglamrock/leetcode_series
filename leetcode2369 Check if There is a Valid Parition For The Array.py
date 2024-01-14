from typing import List

class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        if nums[0] == nums[1]:
            dp[1] = True
        if len(nums) >= 3 and nums[0] == nums[1] == nums[2]:
            dp[2] = True
        if len(nums) >= 3 and nums[2] == nums[1] + 1 and nums[1] == nums[0] + 1:
            dp[2] = True

        for i in range(3, n):
            if nums[i] == nums[i - 1] and dp[i - 2]:
                dp[i] = True
                continue
            if nums[i] == nums[i - 1] == nums[i - 2] and dp[i - 3]:
                dp[i] = True
                continue
            if nums[i] == nums[i - 1] + 1 and nums[i - 1] == nums[i - 2] + 1 and dp[i - 3]:
                dp[i] = True

        return dp[-1]


print(Solution().validPartition([1, 1, 1, 2]))
print(Solution().validPartition([4, 4, 4, 5, 6, 7, 8, 8, 9, 9, 9, 10, 11]))
