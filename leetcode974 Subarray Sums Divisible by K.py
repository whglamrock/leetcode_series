from collections import defaultdict
from typing import List

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixSumRemainderCount = defaultdict(int)
        prefixSumRemainderCount[0] = 1
        prefixSum = 0
        ans = 0
        for num in nums:
            prefixSum += num
            ans += prefixSumRemainderCount[prefixSum % k]
            prefixSumRemainderCount[prefixSum % k] += 1

        return ans


print(Solution().subarraysDivByK(nums=[4, 5, 0, -2, -3, 1], k=5))
