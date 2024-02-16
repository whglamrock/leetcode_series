from typing import List

# O(log(N)) + O(K) solution. Could be improved to O(log(N - K)) + O(K), but not really necessary in real
# interview (see: https://leetcode.com/problems/find-k-closest-elements/solutions/106426/java-c-python-binary-search-o-log-n-k-k/).
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        closestSmallerIndex = self.findClosestSmallerIndex(arr, x)
        # entire arr > x
        if closestSmallerIndex == -1:
            return arr[:k]

        if k == 1:
            if closestSmallerIndex + 1 >= len(arr) or abs(arr[closestSmallerIndex + 1] - x) >= abs(
                    arr[closestSmallerIndex] - x):
                return [arr[closestSmallerIndex]]
            else:
                return [arr[closestSmallerIndex + 1]]

        l, r = closestSmallerIndex, closestSmallerIndex
        while 1 <= l <= r < len(arr) - 1 and r - l + 1 < k:
            # this way, even the original closestSmallerIndex is not closest (i.e., the closestBiggerIndex is closer)
            # The closest element won't be missed, since the edge case of k == 1 is excluded already.
            if abs(arr[l - 1] - x) > abs(arr[r + 1] - x):
                r += 1
            else:
                l -= 1

        if r - l + 1 < k:
            if r == len(arr) - 1:
                return arr[len(arr) - k:]
            else:
                return arr[:k]

        return arr[l:r + 1]

    def findClosestSmallerIndex(self, nums: List[int], x: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r + 1) // 2
            if l == r:
                if nums[m] <= x:
                    return m
                else:
                    return -1
            if nums[m] <= x:
                l = m
            else:
                r = m - 1

        return -1


print(Solution().findClosestElements([1, 2, 3, 4, 5], 4, 3))
print(Solution().findClosestElements([1, 2, 2, 2, 3, 3], 3, 3))


'''
# original naive O(N) solution
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        distanceSum = 0
        for i in range(k):
            distanceSum += abs(x - arr[i])

        l, r = 0, k - 1
        ans = [l, r]
        while r < len(arr):
            if r + 1 < len(arr):
                newDistanceSum = distanceSum - abs(arr[l] - x) + abs(arr[r + 1] - x)
                if newDistanceSum < distanceSum:
                    ans = [l + 1, r + 1]
            r += 1
            l += 1

        return arr[ans[0]:ans[1] + 1]
'''