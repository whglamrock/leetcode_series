
'''
idea came from: https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2481/Share-my-O(log(min(mn))-solution-with-explanation
'''

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        # make sure nums1 is always the shorter one
        if m > n:
            m, n, nums1, nums2 = n, m, nums2, nums1

        # search range is based on nums1
        l, r = 0, m

        # we concatenate nums1[:i] & nums2[:j] to be left half and nums1[i:] & nums2[j:] to be right half
        while l <= r:  # the "=" condition considers when m == 0
            i = (l + r) / 2
            # remember this index trick that makes sure when the total length is odd number,
              # we always make the  left half has 1 more number
            j = (m + n + 1) / 2 - i

            # i is to small
            if j > 0 and i < m and nums2[j - 1] > nums1[i]:
                l = i + 1
            # j is to small / i is too big
            elif i > 0 and j < n and nums1[i - 1] > nums2[j]:
                r = i
            # when i is correct + corner cases
            else:
                if i == 0:  # no number in nums1 exist in the left half
                    max_of_left = nums2[j - 1]
                elif j == 0:
                    max_of_left = nums1[i - 1]
                else:
                    max_of_left = max(nums2[j - 1], nums1[i - 1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m:  # no number in nums1 exist in the right half
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])

                return (max_of_left + min_of_right) / 2.0



Sol = Solution()
print Sol.findMedianSortedArrays([1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 13])




