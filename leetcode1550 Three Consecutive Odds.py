from typing import List


class Solution:
    def threeConsecutiveOdds(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        for i in range(len(nums) - 2):
            first, second, third = nums[i], nums[i + 1], nums[i + 2]
            if first % 2 and second % 2 and third % 2:
                return True

        return False
