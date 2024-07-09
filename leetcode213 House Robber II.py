from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dpRob1st, dpNotRob1st = [0] * len(nums), [0] * len(nums)
        dpRob1st[0] = nums[0]
        if len(nums) > 1:
            dpRob1st[1], dpNotRob1st[1] = nums[0], nums[1]

        for i in range(2, len(nums)):
            if i < len(nums) - 1:
                dpRob1st[i] = max(dpRob1st[i - 1], nums[i] + dpRob1st[i - 2])
            else:
                dpRob1st[i] = dpRob1st[i - 1]
            dpNotRob1st[i] = max(dpNotRob1st[i - 1], nums[i] + dpNotRob1st[i - 2])

        return max(dpRob1st[-1], dpNotRob1st[-1])


'''
# Alternative solution. Idea came from: https://leetcode.com/problems/house-robber-ii/solutions/893957/python-just-use-house-robber-twice/
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
'''