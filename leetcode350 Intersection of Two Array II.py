from collections import Counter
from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Count = Counter(nums1)
        nums2Count = Counter(nums2)
        ans = []
        for num in nums1Count:
            if num not in nums2Count:
                continue
            for i in range(min(nums1Count[num], nums2Count[num])):
                ans.append(num)
        return ans


print(Solution().intersect([1, 2, 2, 1], [2, 3, 2]))
