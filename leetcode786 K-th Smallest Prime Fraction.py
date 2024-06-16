from heapq import *
from typing import List


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        pq = []
        n = len(arr)
        for i in range(n - 1):
            heappush(pq, [arr[i] / arr[-1], i, n - 1])

        ans = None
        while k:
            currMinFrac, i, j = heappop(pq)
            ans = [arr[i], arr[j]]
            if j - 1 > i:
                heappush(pq, [arr[i] / arr[j - 1], i, j - 1])
            k -= 1

        return ans
