from typing import List

# Idea:
# 1) Count the number of the most frequent element. If it's <= half all of them can be pair removed. But if not,
# some of them cannot be removed (2 * numOfMiddleNum - n, actually).
# 2) If there's any number that's more than half of the array, it must be the middle number. So we use binary search
# to find the first and last index of it.
class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        middleNum = nums[n // 2]
        firstIndex, lastIndex = self.findFirstIndexOf(nums, middleNum), self.findLastIndexOf(nums, middleNum)
        numOfMiddleNum = lastIndex - firstIndex + 1
        if 2 * numOfMiddleNum > n:
            return 2 * numOfMiddleNum - n
        else:
            return n % 2

    def findLastIndexOf(self, nums: List[int], target: int) -> int:
        l, r = len(nums) // 2, len(nums) - 1
        while l <= r:
            m = (l + r + 1) // 2
            if l == r:
                return m
            if nums[m] > target:
                r = m - 1
            else:
                l = m

        return l

    def findFirstIndexOf(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) // 2
        while l <= r:
            m = (l + r) // 2
            if l == r:
                return m
            if nums[m] < target:
                l = m + 1
            else:
                r = m

        return l
