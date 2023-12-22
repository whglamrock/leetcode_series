class SparseVector:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.nonZeroIndexes = set()
        for i in range(len(nums)):
            if nums[i] != 0:
                self.nonZeroIndexes.add(i)

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        """
        :type vec: 'SparseVector'
        :rtype: int
        """
        nonZeroIndexesOfVec = vec.nonZeroIndexes
        nonZeroIndexesOfBoth = nonZeroIndexesOfVec.intersection(self.nonZeroIndexes)

        ans = 0
        for i in nonZeroIndexesOfBoth:
            ans += vec.nums[i] * self.nums[i]

        return ans

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
