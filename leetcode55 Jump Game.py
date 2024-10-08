from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        currFarthest = 0

        for i, num in enumerate(nums):
            if i > currFarthest:
                return False
            currFarthest = max(currFarthest, i + num)
            if currFarthest >= len(nums) - 1:
                return True

        return False


print(Solution().canJump(nums=[2, 3, 1, 1, 4]))
print(Solution().canJump(nums=[3, 2, 1, 0, 4]))
