from typing import List

class SparseVector:
    def __init__(self, nums: List[int]):
        self.indexToNum = {}
        for i, num in enumerate(nums):
            if num:
                self.indexToNum[i] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        indexToNumOfVec = vec.indexToNum
        non0Indexes = set(self.indexToNum.keys()).intersection(indexToNumOfVec.keys())
        ans = 0
        for i in non0Indexes:
            ans += self.indexToNum[i] * indexToNumOfVec[i]

        return ans


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
