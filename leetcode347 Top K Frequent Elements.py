from collections import Counter, defaultdict
from typing import List


# O(N) solution because the maxCount <= len(nums)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = Counter(nums)
        countToNums = defaultdict(list)
        minCount, maxCount = 2147483647, 0
        for num, count in numCount.items():
            countToNums[count].append(num)
            minCount = min(minCount, count)
            maxCount = max(maxCount, count)

        ans = []
        for i in range(maxCount, minCount - 1, -1):
            if i not in countToNums:
                continue
            numsWithIcount = countToNums[i]
            # the answer is guaranteed to be unique so
            # there won't be cases like [1, 2, 2, 3, 3, 4, 4] and k = 2
            if len(numsWithIcount) <= k:
                ans += numsWithIcount
                k -= len(numsWithIcount)
            if k <= 0:
                break

        return ans


print(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(Solution().topKFrequent([1, 1, 1, 2, 2, 3, 3, 4], 3))
