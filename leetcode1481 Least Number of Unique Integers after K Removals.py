from collections import Counter
from typing import List

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        numCount = Counter(arr)
        counts = sorted(numCount.values())

        i = 0
        while i < len(counts) and k >= counts[i]:
            k -= counts[i]
            i += 1

        return len(counts) - i


print(Solution().findLeastNumOfUniqueInts([4, 3, 1, 1, 3, 3, 2, 5, 5, 5, 5], 3))
print(Solution().findLeastNumOfUniqueInts([5, 5, 4], 1))
