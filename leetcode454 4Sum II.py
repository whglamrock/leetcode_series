from collections import defaultdict
from typing import List

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n = len(nums1)
        twoSumCount1stAnd2nd = defaultdict(int)
        for i in range(n):
            for j in range(n):
                twoSumCount1stAnd2nd[nums1[i] + nums2[j]] += 1
        twoSumCount3rdAnd4th = defaultdict(int)
        for i in range(n):
            for j in range(n):
                twoSumCount3rdAnd4th[nums3[i] + nums4[j]] += 1

        ans = 0
        for twoSum in twoSumCount1stAnd2nd:
            if -twoSum in twoSumCount3rdAnd4th:
                ans += twoSumCount1stAnd2nd[twoSum] * twoSumCount3rdAnd4th[-twoSum]
        return ans
