from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1
        while l <= r:
            if l == r:
                return l
            m = (l + r) // 2
            if arr[m] > arr[m - 1] and arr[m] > arr[m + 1]:
                return m
            elif arr[m - 1] < arr[m] < arr[m + 1]:
                l = m + 1
            # be careful here for edge case like [3,9,8,6,4]. r = m - 1 doesn't work
            else:
                r = m

        return l


print(Solution().peakIndexInMountainArray([3, 9, 8, 6, 4]))
print(Solution().peakIndexInMountainArray([3, 5, 6, 8, 9, 4]))
print(Solution().peakIndexInMountainArray([0, 1, 2, 3, 4, 3, 2, 1]))
print(Solution().peakIndexInMountainArray([0, 10, 5, 2]))
print(Solution().peakIndexInMountainArray([0, 2, 1, 0]))
print(Solution().peakIndexInMountainArray([0, 1, 0]))
