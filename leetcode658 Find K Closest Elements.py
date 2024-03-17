from collections import deque
from typing import List

# For all these find closest element in an array type of question, write 2 binary search functions
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        closestBiggerIndex = self.findClosestBiggerIndex(arr, x)
        closestSmallerIndex = self.findClosestSmallerIndex(arr, x)
        if closestBiggerIndex == -1:
            closestIndex = closestSmallerIndex
        elif closestSmallerIndex == -1:
            closestIndex = closestBiggerIndex
        # both are not -1
        else:
            if abs(arr[closestSmallerIndex] - x) <= abs(arr[closestBiggerIndex] - x):
                closestIndex = closestSmallerIndex
            else:
                closestIndex = closestBiggerIndex

        ans = deque([arr[closestIndex]])
        l, r = closestIndex - 1, closestIndex + 1
        k -= 1

        while k and l >= 0 and r < len(arr):
            if abs(arr[l] - x) <= abs(arr[r] - x):
                ans.appendleft(arr[l])
                l -= 1
            else:
                ans.append(arr[r])
                r += 1
            k -= 1
        while k and l >= 0:
            ans.appendleft(arr[l])
            l -= 1
            k -= 1
        while k and r < len(arr):
            ans.append(arr[r])
            r += 1
            k -= 1

        return ans

    def findClosestBiggerIndex(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        # find the min index that >= target
        while l <= r:
            m = (l + r) // 2
            if l == r:
                if nums[m] >= target:
                    return m
                return -1
            if nums[m] < target:
                l = m + 1
            else:
                r = m

        return -1

    def findClosestSmallerIndex(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        # find the max index that < target
        while l <= r:
            m = (l + r + 1) // 2
            if l == r:
                if nums[m] < target:
                    return m
                return -1
            if nums[m] < target:
                l = m
            else:
                r = m - 1

        return -1


print(Solution().findClosestElements([1, 2, 3, 4, 5], 4, 3))
print(Solution().findClosestElements([1, 2, 2, 2, 3, 3], 3, 3))
