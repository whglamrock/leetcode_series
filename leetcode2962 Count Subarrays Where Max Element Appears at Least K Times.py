from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxElement = max(nums)
        maxElementIndexes = []
        ans = 0
        for i, num in enumerate(nums):
            if num == maxElement:
                maxElementIndexes.append(i)
            if len(maxElementIndexes) >= k:
                ans += maxElementIndexes[len(maxElementIndexes) - k] + 1

        return ans
