from collections import defaultdict
from typing import List


class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        modToNums = defaultdict(list)
        for num in nums:
            modToNums[num % space].append(num)

        maxCount = max(len(numsWithSameMod) for numsWithSameMod in modToNums.values())
        ans = None
        for modValue, numsWithSameMod in modToNums.items():
            if len(numsWithSameMod) == maxCount:
                if ans is None:
                    ans = min(numsWithSameMod)
                else:
                    ans = min(ans, min(numsWithSameMod))

        return ans
