# O(m + n) time, O(1) space optimal solution
# this question is so fucking stupid, and it shouldn't be an easy level because you have to be able to think
# of filling the nums1 array backwards.

class Solution(object):
    def merge(self, nums1, m, nums2, n):

        # set each element from the biggest to smallest
        while m and n:
            if nums1[m - 1] <= nums2[n - 1]:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
            else:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1

        while n:
            nums1[n - 1] = nums2[n - 1]
            n -= 1


nums1 = [0, 0, 0, 0, 0]
Solution().merge(nums1, 0, [1, 2, 3, 4, 5], 5)
print(nums1)

nums1 = [2, 3, 6, 0, 0, 0, 0, 0]
Solution().merge(nums1, 3, [1, 2, 3, 4, 5], 5)
print(nums1)
