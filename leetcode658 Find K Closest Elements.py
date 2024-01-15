from typing import List

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


print(Solution().findClosestElements([1, 2, 3, 4, 5], 4, 3))
print(Solution().findClosestElements([1, 2, 2, 2, 3, 3], 3, 3))


'''
# O(K + log(N - K)) solution, see: https://leetcode.com/problems/find-k-closest-elements/solutions/106426/java-c-python-binary-search-o-log-n-k-k/
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        l, r = 0, len(arr) - k
        while l < r:
            m = (l + r) / 2
            if x - arr[m] > arr[m + k] - x:
                l = m + 1
            else:
                r = m

        return arr[l:l + k]
'''