from typing import List

class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        maxLenNums1 = [1 for i in range(n)]
        maxLenNums2 = [1 for i in range(n)]

        ans = 1
        for i in range(1, n):
            if nums1[i] >= nums1[i - 1]:
                maxLenNums1[i] = maxLenNums1[i - 1] + 1
            if nums1[i] >= nums2[i - 1]:
                maxLenNums1[i] = max(maxLenNums1[i], maxLenNums2[i - 1] + 1)
            if nums2[i] >= nums2[i - 1]:
                maxLenNums2[i] = maxLenNums2[i - 1] + 1
            if nums2[i] >= nums1[i - 1]:
                maxLenNums2[i] = max(maxLenNums2[i], maxLenNums1[i - 1] + 1)
            ans = max(maxLenNums1[i], maxLenNums2[i], ans)

        return ans


print(Solution().maxNonDecreasingLength(nums1=[2, 3, 1], nums2=[1, 2, 1]))
print(Solution().maxNonDecreasingLength(nums1=[1, 3, 2, 1], nums2=[2, 2, 3, 4]))
print(Solution().maxNonDecreasingLength(nums1=[1, 1], nums2=[2, 2]))
