from collections import Counter, defaultdict
from typing import List

# we could simply sort numCount.values() but below solution is guaranteed O(n) time.
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        numCount = Counter(arr)
        numCountFrequency = defaultdict(int)
        minCount, maxCount = 2147483647, 0
        for num, count in numCount.items():
            numCountFrequency[count] += 1
            minCount = min(minCount, count)
            maxCount = max(maxCount, count)

        counts = []
        for count in range(minCount, maxCount + 1):
            if count not in numCountFrequency:
                continue
            for i in range(numCountFrequency[count]):
                counts.append(count)

        i = 0
        while i < len(counts) and k >= counts[i]:
            k -= counts[i]
            i += 1

        return len(counts) - i


print(Solution().findLeastNumOfUniqueInts([4, 3, 1, 1, 3, 3, 2, 5, 5, 5, 5], 3))
print(Solution().findLeastNumOfUniqueInts([5, 5, 4], 1))
