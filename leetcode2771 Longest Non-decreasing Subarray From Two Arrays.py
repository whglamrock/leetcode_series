class Solution(object):
    def maxNonDecreasingLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
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