from typing import List

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        isIncreasing = True
        isDecreasing = True
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                isDecreasing = False
            elif nums[i - 1] > nums[i]:
                isIncreasing = False

            if not isDecreasing and not isIncreasing:
                break

        return isIncreasing or isDecreasing
