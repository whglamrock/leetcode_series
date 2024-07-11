from collections import defaultdict
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []

        sequenceToCount = defaultdict(int)
        for i in range(len(s) - 9):
            sequence = s[i:i + 10]
            sequenceToCount[sequence] += 1

        ans = []
        for sequence, count in sequenceToCount.items():
            if count >= 2:
                ans.append(sequence)

        return ans
