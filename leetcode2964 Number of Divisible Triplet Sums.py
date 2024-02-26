from collections import defaultdict
from typing import List

class Solution:
    def divisibleTripletCount(self, nums: List[int], d: int) -> int:
        for i in range(len(nums)):
            nums[i] %= d

        prefixSingleNumCount = defaultdict(int)
        prefix2SumModCount = defaultdict(int)
        ans = 0
        for i, num in enumerate(nums):
            if d - num in prefix2SumModCount:
                ans += prefix2SumModCount[d - num]
            elif num == 0 and 0 in prefix2SumModCount:
                ans += prefix2SumModCount[0]

            for firstNum in prefixSingleNumCount:
                prefix2SumModCount[(firstNum + num) % d] += prefixSingleNumCount[firstNum]
            prefixSingleNumCount[num] += 1

        return ans
