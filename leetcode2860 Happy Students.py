from typing import List

# It shouldn't be too hard to observe that:
# 1) Assume nums[i] is the max of the numbers you choose, you HAVE TO choose all nums[:i + 1]. so we just check if
# the total number of numbers chosen (i + 1) is bigger than nums[i]
# 2) Then just check for such nums[i], whether the next number nums[i + 1] > total number of numbers chosen (i + 1).
class Solution:
    def countWays(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        # when we don't choose any students, min(nums) can't be 0
        ans = 1 if nums[0] != 0 else 0
        for i, num in enumerate(nums):
            if num <= i and (i == n - 1 or i + 1 < nums[i + 1]):
                ans += 1

        return ans
