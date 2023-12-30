from typing import List

class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numSet1 = set(nums1)
        numSet2 = set(nums2)
        numOfIndexesIn1AppearIn2 = 0
        numOfIndexesIn2AppearIn1 = 0
        for num in nums1:
            if num in numSet2:
                numOfIndexesIn1AppearIn2 += 1
        for num in nums2:
            if num in numSet1:
                numOfIndexesIn2AppearIn1 += 1

        return [numOfIndexesIn1AppearIn2, numOfIndexesIn2AppearIn1]


print(Solution().findIntersectionValues(nums1=[4, 3, 2, 3, 1], nums2=[2, 2, 5, 2, 3, 6]))
