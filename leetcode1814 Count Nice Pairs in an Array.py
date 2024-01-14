from collections import defaultdict
from functools import lru_cache
from typing import List

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        revDiffCount = defaultdict(int)
        ans = 0
        for num in nums:
            revDiff = self.getRevDiff(num)
            ans += revDiffCount[revDiff]
            ans %= mod
            revDiffCount[revDiff] += 1

        return ans % mod

    @lru_cache(None)
    def getRevDiff(self, num: int) -> int:
        if num == 0:
            return 0
        reverseIntStr = str(num).rstrip('0')[::-1]
        return int(reverseIntStr) - num


print(Solution().countNicePairs([9, 4, 0, 5, 2, 1, 8, 7, 6, 9, 9]))
print(Solution().countNicePairs([13, 10, 35, 24, 76]))
print(Solution().countNicePairs([1, 1, 1, 1, 1]))
