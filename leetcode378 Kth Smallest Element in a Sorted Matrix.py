from heapq import *
from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        pq = []
        for i in range(n):
            heappush(pq, [matrix[i][0], i, 0])

        ans = 0
        while pq and k:
            ans, i, j = heappop(pq)
            k -= 1
            if j + 1 < n:
                heappush(pq, [matrix[i][j + 1], i, j + 1])

        return ans


print(Solution().kthSmallest(
    [[1, 5, 19],
     [10, 14, 18],
     [13, 21, 31]],
    8))
