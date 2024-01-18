from heapq import *
from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        pq = []
        for i in range(n):
            heappush(pq, [matrix[i][0], i, 0])

        ans = []
        while pq:
            smallest, i, j = heappop(pq)
            ans.append(smallest)
            if len(ans) == k:
                return ans[-1]
            if j + 1 < n:
                heappush(pq, [matrix[i][j + 1], i, j + 1])


print(Solution().kthSmallest(
    [[1, 5, 19],
     [10, 14, 18],
     [13, 21, 31]],
    8))


'''
# O(N * log(N)) time, count how many elements less that mid
class Solution(object):
    def kthSmallest(self, matrix, k):

        n = len(matrix)
        l, r = matrix[0][0], matrix[n - 1][n - 1]

        while l < r:  # o(logN), when l == r, exit the while loop, l > r is impossible
            mid = l + (r - l) / 2
            cnt, j = 0, n - 1
            # o(n), because j at most goes from n-1 to 1 once. If matrix[i][j] always <= mid, j won't decrease.
            for i in range(n):
                while j >= 0 and matrix[i][j] > mid:
                    j -= 1
                cnt += j + 1
            # after the for loop, cnt counts the number of elements that are <= mid.
            if cnt < k:  # mid too small
                l = mid + 1  # no "l = mid"! because when l == r - 1 it will go into infinite loop
            else:  # mid too big or equals to the kth smallest
                r = mid
        # There is no need to worry if the final l is not a matrix element, because we always ensure that the
        # target, kth smallest, is within [l, r].

        # P.S.: it is possible for cnt > k while l == r. E.g., matrix = [[1,2], [1,3]], k = 1. When the target is
        # not distinct, we still need to keep it within [l, r]. So when cnt > k, it is also possible the current
        # mid is out potential target, we use 'r = mid' instead of 'r = mid-1'. However, when cnt < k, it is
        # definitely impossible for mid == kth smallest, so we use 'l = mid+1'.

        return l  # return r is same
'''
