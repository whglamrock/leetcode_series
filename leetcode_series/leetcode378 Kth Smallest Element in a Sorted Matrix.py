
# O(nlogn) time complexity
# the idea is to use binary search to cut the search range by half (logn search times);
#   within each search, count how many elements <= the mid with O(n) time

class Solution(object):
    def kthSmallest(self, matrix, k):

        n = len(matrix)
        l, r = matrix[0][0], matrix[n - 1][n - 1]

        while l < r:    # o(logn), when l == r, exit the while loop, l > r is impossible
            mid = l + (r - l) / 2
            cnt, j = 0, n - 1
            # o(n), because j at most goes from n-1 to 1 once. If matrix[i][j] always <= mid, j won't decrease.
            for i in xrange(n):
                while j >= 0 and matrix[i][j] > mid:
                    j -= 1
                cnt += j + 1
            # after the for loop, cnt counts the number of elements that are <= mid.
            if cnt < k:  # mid too small
                l = mid + 1
            else:  # mid too big or equals to the kth smallest
                r = mid
        # There is no need to worry if the final l is not a matrix element, because we always ensure that the
        # target, kth smallest, is within [l, r].

        # P.S.: it is possible for cnt > k while l == r. E.g., matrix = [[1,2], [1,3]], k = 1. When the target is
        # not distinct, we still need to keep it within [l, r]. So when cnt > k, it is also possible the current
        # mid is out potential target, we use 'r = mid' instead of 'r = mid-1'. However, when cnt < k, it is
        # definitely impossible for mid == kth smallest, so we use 'l = mid+1'.

        return l    # return r is same



Sol = Solution()
matrix = [
    [1, 5, 19],
    [10, 14, 18],
    [13, 21, 31]
]
print Sol.kthSmallest(matrix,8)



"""
# another O(nlogn) min-heap solution

from heapq import *

class Solution(object):
    def kthSmallest(self, matrix, k):

        if not matrix or not matrix[0]:
            return None

        n = len(matrix)
        q = []
        for j in xrange(n):
            heappush(q, [matrix[0][j], (0, j)])
        for i in xrange(k - 1):
            currsmallest, (x, y) = heappop(q)
            if x == n - 1:
                continue
            nexttoadd = matrix[x + 1][y]
            heappush(q, [nexttoadd, (x + 1, y)])

        thekth, (x, y) = heappop(q)
        return thekth
"""
