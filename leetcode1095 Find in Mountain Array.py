from typing import List

"""
This is MountainArray's API interface.
You should not implement it, or speculate about its implementation
"""
class MountainArray:
    def __init__(self, array: List[int]):
        self.nums = array

    def get(self, index: int) -> int:
        return self.nums[index]

    def length(self) -> int:
        return len(self.nums)

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        peak = self.findPeakIndex(mountainArr, n)
        indexInLeft = self.findTargetInSorted(target, mountainArr, 0, peak)
        indexInRight = self.findTargetInReverseSorted(target, mountainArr, peak, n - 1)
        if indexInLeft == -1:
            return indexInRight
        elif indexInRight == -1:
            return indexInLeft
        else:
            return min(indexInLeft, indexInRight)

    def findTargetInSorted(self, target: int, mountainArr: 'MountainArray', l: int, r: int) -> int:
        while l <= r:
            m = (l + r) // 2
            midVal = mountainArr.get(m)
            if midVal == target:
                return m
            elif midVal < target:
                l = m + 1
            else:
                r = m - 1
        # exit condition is l == r
        return -1

    def findTargetInReverseSorted(self, target: int, mountainArr: 'MountainArray', l: int, r: int) -> int:
        while l <= r:
            m = (l + r) // 2
            midVal = mountainArr.get(m)
            if midVal == target:
                return m
            elif midVal < target:
                r = m - 1
            else:
                l = m + 1

        # exit condition is l == r
        return -1

    def findPeakIndex(self, mountainArr: 'MountainArray', n: int) -> int:
        l, r = 0, n - 1
        while l < r:
            m = (l + r) // 2
            midVal = mountainArr.get(m)
            if midVal < mountainArr.get(m + 1):
                l = m + 1
            else:
                r = m

        # exit condition is l == r
        return l


mountainArr1 = MountainArray([1, 2, 3, 4, 5, 3, 1])
mountainArr2 = MountainArray([0, 1, 2, 4, 2, 1])
print(Solution().findInMountainArray(3, mountainArr1))
print(Solution().findInMountainArray(3, mountainArr2))
print(Solution().findInMountainArray(1, mountainArr1))
print(Solution().findInMountainArray(4, mountainArr2))