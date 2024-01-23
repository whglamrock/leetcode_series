from collections import defaultdict
from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        numCount = defaultdict(int)
        ans = 0
        for num in nums:
            if k - num in numCount:
                ans += 1
                numCount[k - num] -= 1
                if not numCount[k - num]:
                    del numCount[k - num]
            else:
                numCount[num] += 1

        return ans


print(Solution().maxOperations(nums=[1, 2, 3, 4], k=5))
print(Solution().maxOperations(nums=[3, 1, 3, 4, 3], k=6))
