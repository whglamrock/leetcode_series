from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        indexOfTarget = self.binarySearchToFindTarget(nums, target)
        if indexOfTarget == -1:
            return [-1, -1]
        firstIndex = self.findFirstIndex(nums, target, 0, indexOfTarget)
        lastIndex = self.findLastIndex(nums, target, indexOfTarget, len(nums) - 1)
        return [firstIndex, lastIndex]

    def binarySearchToFindTarget(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            if l == r:
                if nums[l] == target:
                    return l
                else:
                    return -1
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return -1

    # nums[l:r + 1] <= target
    def findFirstIndex(self, nums: List[int], target: int, l: int, r: int):
        while l <= r:
            if l == r:
                return l
            m = (l + r) // 2
            if nums[m] == target:
                r = m
            # nums[m] < target
            else:
                l = m + 1

        return r

    # nums[l:r + 1] >= target
    def findLastIndex(self, nums: List[int], target: int, l: int, r: int):
        while l <= r:
            if l == r:
                return l
            m = (l + r + 1) // 2
            if nums[m] == target:
                l = m
            # nums[m] > target
            else:
                r = m - 1

        return l


print(Solution().searchRange([2, 2], 2))
print(Solution().searchRange([], 0))
print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))
print(Solution().searchRange([5, 7, 7, 8, 8, 10], 6))
