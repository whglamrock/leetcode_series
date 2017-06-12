
from heapq import *

# the idea is pretty much like the lc378. consider the nums1, nums2 are the rows and columns of
#   a 2-D array

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):

        if not nums1 or not nums2 or not k:
            return []

        n1, n2 = len(nums1), len(nums2)
        q = []
        for i2 in xrange(n2):
            heappush(q, [nums1[0] + nums2[i2], (0, i2)])

        ans = []
        while k:
            if not q:
                break
            currsum, (i1, i2) = heappop(q)
            ans.append([nums1[i1], nums2[i2]])
            k -= 1
            if i1 == n1 - 1:
                continue
            heappush(q, [nums1[i1 + 1] + nums2[i2], (i1 + 1, i2)])

        return ans