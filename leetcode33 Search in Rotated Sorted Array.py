from typing import List


# In such question, always try to find the pivot (smallest) index first.
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        pivotIndex = self.findPivot(nums)
        # look for target in [0, pivot]
        candidateIndexInBiggerHalf = self.binarySearch(nums, 0, pivotIndex - 1, target)
        if candidateIndexInBiggerHalf != -1:
            return candidateIndexInBiggerHalf

        return self.binarySearch(nums, pivotIndex, len(nums) - 1, target)

    def findPivot(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[l] < nums[r]:
                return l
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1

        return l

    def binarySearch(self, nums: List[int], l: int, r: int, target: int) -> int:
        while l <= r:
            m = (l + r) // 2
            if l == r:
                if nums[m] == target:
                    return m
                return -1
            if nums[m] < target:
                l = m + 1
            else:
                r = m

        return -1


print(Solution().search([4, 5, 6, 7, 3], 3))
