from typing import List

# idea came from: https://leetcode.com/problems/house-robber-ii/solutions/893957/python-just-use-house-robber-twice/
class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0] + self.robHouse(nums[2:len(nums) - 1]), self.robHouse(nums[1:]))

    def robHouse(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        # dp1 stores the max money you can rob if you rob i
        dp1 = [0] * n
        # dp2 stores the max money you can rob if you don't rob i
        dp2 = [0] * n
        for i, num in enumerate(nums):
            if i == 0:
                dp1[i] = num
                continue
            # if you rob i, you must not rob i - 1
            dp1[i] = dp2[i - 1] + num
            dp2[i] = max(dp2[i - 1], dp1[i - 1])

        return max(dp1[-1], dp2[-1])
