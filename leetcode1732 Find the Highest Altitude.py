from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxAltitude = 0
        curr = 0
        for i in range(len(gain)):
            curr += gain[i]
            maxAltitude = max(maxAltitude, curr)
        return maxAltitude
