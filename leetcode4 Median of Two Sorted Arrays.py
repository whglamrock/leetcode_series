from typing import List

class Solution(object):
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        # make sure nums1 is always the shorter one
        if m > n:
            m, n = n, m
            nums1, nums2 = nums2, nums1

        l, r = 0, m
        while l <= r:
            i = (l + r) // 2
            # remember this index trick that makes sure when the total length is odd number,
            # we can make the left half have 1 more number
            j = (m + n + 1) // 2 - i

            # i too small
            if j > 0 and i < m and nums1[i] < nums2[j - 1]:
                l = i + 1
            # i too big
            elif i > 0 and j < n and nums1[i - 1] > nums2[j]:
                r = i
            # corner cases + we find the median
            else:
                # the whole nums1 is in right part
                if i == 0:
                    maxOfLeft = nums2[j - 1]
                # the whole nums2 is in right part
                elif j == 0:
                    maxOfLeft = nums1[i - 1]
                # remember to include the special case when i == m / j == n here
                else:
                    maxOfLeft = max(nums1[i - 1], nums2[j - 1])

                if (m + n) % 2 == 1:
                    return maxOfLeft

                # the whole nums1 is in left part
                if i == m:
                    minOfRight = nums2[j]
                # the whole nums2 is in left part
                elif j == n:
                    minOfRight = nums1[i]
                # remember to include the special case when i == 0 / j == 0 here
                else:
                    minOfRight = min(nums1[i], nums2[j])

                return (maxOfLeft + minOfRight) / 2.0


print(Solution().findMedianSortedArrays([1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 13]))
print(Solution().findMedianSortedArrays([1, 2, 2, 2, 2], [3, 3, 3, 4, 4, 4]))
