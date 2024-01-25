from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1Set, nums2Set = set(nums1), set(nums2)
        distinctNums1 = []
        visited1 = set()
        for num in nums1:
            if num not in visited1 and num not in nums2Set:
                distinctNums1.append(num)
            visited1.add(num)
        distinctNums2 = []
        visited2 = set()
        for num in nums2:
            if num not in visited2 and num not in nums1Set:
                distinctNums2.append(num)
            visited2.add(num)

        return [distinctNums1, distinctNums2]
