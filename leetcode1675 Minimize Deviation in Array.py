from heapq import *
from math import inf
from typing import List

# the idea is:
# 1) divide every num until it's not dividable, add them to the priotity queue
# 2) also keep the original value of the num before division
# 3) try to shrink the range between the min, max value in the heap
# 4) pop out the smallest x, and see if we can add back 2 * x to pq.
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        pq = []
        for num in nums:
            heappush(pq, [self.divideNumUntilOdd(num), num])

        currMax = max(num for num, originalNum in pq)

        ans = inf
        while len(pq) == len(nums):
            num, originalNum = heappop(pq)
            ans = min(ans, currMax - num)
            if num % 2 == 1 or num < originalNum:
                currMax = max(currMax, num * 2)
                heappush(pq, [num * 2, originalNum])
        return ans

    def divideNumUntilOdd(self, num: int) -> int:
        while num % 2 == 0:
            num //= 2
        return num


print(Solution().minimumDeviation([8, 10, 2, 1]))
print(Solution().minimumDeviation([2, 10, 8]))
print(Solution().minimumDeviation([4, 1, 5, 20, 3]))
print(Solution().minimumDeviation([1, 2, 3, 4]))
