from typing import List

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        smallerCount, biggerCount, targetCount = 0, 0, 0
        for num in nums:
            if num == target:
                targetCount += 1
            elif num < target:
                smallerCount += 1
            else:
                biggerCount += 1

        if targetCount == 0:
            return []

        return range(smallerCount, len(nums) - biggerCount)
