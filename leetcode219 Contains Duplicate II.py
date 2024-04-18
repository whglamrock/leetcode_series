from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numToIndex = {}
        for i, num in enumerate(nums):
            if num in numToIndex and i - numToIndex[num] <= k:
                return True
            numToIndex[num] = i

        return False
