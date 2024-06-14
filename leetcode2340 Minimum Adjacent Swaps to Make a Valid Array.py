from typing import List


class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        minVal, maxVal = min(nums), max(nums)
        if minVal == maxVal:
            return 0

        n = len(nums)
        rightMostIndexOfMax = None
        for i in range(n - 1, -1, -1):
            if nums[i] == maxVal:
                rightMostIndexOfMax = i
                break

        leftMostIndexOfMin = None
        for i in range(n):
            if nums[i] == minVal:
                leftMostIndexOfMin = i
                break

        if leftMostIndexOfMin < rightMostIndexOfMax:
            return leftMostIndexOfMin + (n - 1 - rightMostIndexOfMax)
        else:
            return leftMostIndexOfMin + (n - 1 - rightMostIndexOfMax) - 1
