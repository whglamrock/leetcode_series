from typing import List

class Solution:
    def findSpecialInteger(self, nums: List[int]) -> int:
        n = len(nums)
        for targetIndex in [n // 4, n // 2, 3 * n // 4, n - 1]:
            target = nums[targetIndex]
            firstIndex = self.findFirstIndex(nums, target, targetIndex)
            lastIndex = self.findLastIndex(nums, target, targetIndex)
            if lastIndex - firstIndex + 1 > n / 4:
                return target

        return -1

    def findFirstIndex(self, nums: List[int], target: int, targetIndex: int) -> int:
        l, r = 0, targetIndex
        while l < r:
            m = (l + r) // 2
            if nums[m] == target:
                r = m
            else:
                l = m + 1

        return l

    def findLastIndex(self, nums: List[int], target: int, targetIndex: int) -> int:
        l, r = targetIndex, len(nums) - 1
        while l < r:
            m = (l + r + 1) // 2
            if nums[m] == target:
                l = m
            else:
                r = m - 1

        return l


print(Solution().findSpecialInteger(nums=[1, 2, 2, 6, 6, 6, 6, 7, 10]))
print(Solution().findSpecialInteger(nums=[1, 1]))
print(Solution().findSpecialInteger(nums=[1, 2, 3, 3]))


'''
# Naive O(n) time solution
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        numOfSameNumbers = 0
        target = n / 4
        for i, num in enumerate(arr):
            if i > 0 and num == arr[i - 1]:
                numOfSameNumbers += 1
            else:
                numOfSameNumbers = 1
            if numOfSameNumbers > target:
                return num

        return -1
'''