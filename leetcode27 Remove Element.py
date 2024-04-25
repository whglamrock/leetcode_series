from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, 0
        n = len(nums)
        while i < n and j < n:
            while j < n and nums[j] == val:
                nums[j] = -1
                j += 1

            if i < n and j < n:
                nums[i] = nums[j]
                i += 1
                j += 1

        # maybe optional, depending on the requirement in the interview
        while len(nums) > i:
            nums.pop()

        return i
