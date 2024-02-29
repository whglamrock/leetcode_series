from heapq import *
from typing import List

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pq = []
        m, n = len(nums1), len(nums2)
        for i in range(min(m, k)):
            heappush(pq, [nums1[i] + nums2[0], i, 0])

        ans = []
        while k:
            currMinSum, i, j = heappop(pq)
            ans.append([nums1[i], nums2[j]])
            k -= 1
            if j == n - 1:
                continue
            heappush(pq, [nums1[i] + nums2[j + 1], i, j + 1])

        return ans
