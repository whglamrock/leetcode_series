from collections import defaultdict
from typing import List

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        n = len(time)
        numCount = defaultdict(int)
        ans = 0
        for i in range(n):
            time[i] %= 60
            if time[i] == 0 and 0 in numCount:
                ans += numCount[0]
                numCount[0] += 1
                continue
            if 60 - time[i] in numCount:
                ans += numCount[60 - time[i]]
            numCount[time[i]] += 1

        return ans


print(Solution().numPairsDivisibleBy60(time=[30, 20, 150, 100, 40]))
print(Solution().numPairsDivisibleBy60(time=[60, 60, 60]))
