from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0
        n = len(nums)
        while i < n:
            # find the next non 0 elements
            while j < n and nums[j] == 0:
                j += 1
            if j >= n:
                break
            nums[i] = nums[j]
            i += 1
            j += 1

        while i < n:
            nums[i] = 0
            i += 1
