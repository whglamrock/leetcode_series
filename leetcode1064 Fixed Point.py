from typing import List


class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1
        while l <= r:
            m = (l + r) // 2
            if l == r:
                if arr[m] == m:
                    return m
                return -1
            if arr[m] < m:
                l = m + 1
            elif arr[m] > m:
                r = m - 1
            else:
                r = m

        return -1
