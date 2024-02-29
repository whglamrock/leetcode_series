from heapq import *
from typing import List

# remember this set up of pre-adding the elements of the first row to the pq. we can't use the idea of merging
# k sorted list to solve this problem.
# Time complexity: O(log(K) * m * n * k)
class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        n = len(mat[0])
        pq = []
        for i in range(n):
            heappush(pq, -mat[0][i])

        for row in mat[1:]:
            nextPq = []
            for currSum in pq:
                currSum = -currSum
                for i in range(n):
                    heappush(nextPq, -(row[i] + currSum))
                    # the size of the pq doesn't need to be more than k
                    if len(nextPq) > k:
                        heappop(nextPq)
            pq = nextPq

        return -heappop(pq)
