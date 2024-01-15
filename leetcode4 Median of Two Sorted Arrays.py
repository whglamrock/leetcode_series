from typing import List

# remember every line of this solution because it's basically impossible to write a bug-free solution in real interview
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        # always make nums2 have more numbers to avoid any index out of range error for j
        if m > n:
            m, n = n, m
            nums1, nums2 = nums2, nums1

        # the first half is nums[:i] + nums[:j]
        l, r = 0, m
        while l <= r:
            # the setup of i & j makes sure the left half has one more number if (m + n) is an odd number
            i = (l + r) // 2
            j = (m + n + 1) // 2 - i

            # i is too small
            if j > 0 and i < m and nums2[j - 1] > nums1[i]:
                l = i + 1
            # j is too small / i is too big
            elif i > 0 and j < n and nums1[i - 1] > nums2[j]:
                r = i
            else:
                # entire nums2 is in the right, and len(nums1) == len(nums2)
                if j == 0:
                    maxOfLeft = nums1[i - 1]
                # entire nums1 is in the right
                elif i == 0:
                    maxOfLeft = nums2[j - 1]
                else:
                    maxOfLeft = max(nums1[i - 1], nums2[j - 1])

                # this also deals with edge cases like nums1 = [0], nums2 = [1]
                if (m + n) % 2 == 1:
                    return maxOfLeft

                # entire nums1 is in the left
                if i == m:
                    minOfRight = nums2[j]
                # entire nums2 is in the left
                elif j == n:
                    minOfRight = nums1[i]
                else:
                    minOfRight = min(nums1[i], nums2[j])

                return (maxOfLeft + minOfRight) / 2.0


print(Solution().findMedianSortedArrays([1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 13]))
print(Solution().findMedianSortedArrays([1, 2, 2, 2, 2], [3, 3, 3, 4, 4, 4]))
