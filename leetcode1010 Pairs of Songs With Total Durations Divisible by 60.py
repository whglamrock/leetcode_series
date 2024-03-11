from collections import defaultdict
from typing import List

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        for i in range(len(time)):
            time[i] %= 60

        numOfPairs = 0
        durationCount = defaultdict(int)
        for duration in time:
            if 60 - duration in durationCount:
                numOfPairs += durationCount[60 - duration]
            elif duration == 0:
                if 0 in durationCount:
                    numOfPairs += durationCount[0]
            durationCount[duration] += 1

        return numOfPairs


print(Solution().numPairsDivisibleBy60(time=[30, 20, 150, 100, 40]))
print(Solution().numPairsDivisibleBy60(time=[60, 60, 60]))
