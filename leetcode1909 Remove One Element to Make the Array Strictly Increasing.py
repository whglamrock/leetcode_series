from typing import List


# O(1) space solution.
class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            currNum, nextNum = nums[i], nums[i + 1]
            if currNum < nextNum:
                continue

            canMakeIncreaseRemovingCurr = self.isStrictlyIncreasing(nums, i + 1)
            if i - 1 >= 0:
                canMakeIncreaseRemovingCurr = canMakeIncreaseRemovingCurr and nextNum > nums[i - 1]

            canMakeIncreaseRemovingNext = self.isStrictlyIncreasing(nums, i + 2)
            if i + 2 < len(nums):
                canMakeIncreaseRemovingNext = canMakeIncreaseRemovingNext and nums[i + 2] > currNum

            return canMakeIncreaseRemovingCurr or canMakeIncreaseRemovingNext

        return True

    def isStrictlyIncreasing(self, nums: List[int], startIndex: int) -> bool:
        if startIndex >= len(nums) - 1:
            return True

        for i in range(startIndex, len(nums) - 1):
            currNum, nextNum = nums[i], nums[i + 1]
            if currNum >= nextNum:
                return False

        return True
