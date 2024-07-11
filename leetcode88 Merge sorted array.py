from typing import List


# merge backwards to achieve O(1) space
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[i + j + 1] = nums1[i]
                i -= 1
            else:
                nums1[i + j + 1] = nums2[j]
                j -= 1

        while j >= 0:
            nums1[j] = nums2[j]
            j -= 1


nums1 = [0, 0, 0, 0, 0]
Solution().merge(nums1, 0, [1, 2, 3, 4, 5], 5)
print(nums1)

nums1 = [2, 3, 6, 0, 0, 0, 0, 0]
Solution().merge(nums1, 3, [1, 2, 3, 4, 5], 5)
print(nums1)
