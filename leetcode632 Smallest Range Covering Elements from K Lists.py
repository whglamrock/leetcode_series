from heapq import *
from typing import List

# the strategy is init the pq with all row[0]'s and keep popping out the smallest, and calculate the range
# the tricky part is to figure out that the strategy can guarantee the optimal range is reached:
# 1) we only need one element from each of the list, so starting from left we can make sure all possible
# left bounds are considered from the smallest to the biggest
# 2) for each k element group that formed a left bound, we don't have the option to "choose" right, the right
# is literally the max of the heapq
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        pq = []
        for i, row in enumerate(nums):
            heappush(pq, [row[0], i, 0])
        right = max(row[0] for row in nums)

        ans = [-2147483648, 2147483647]
        while len(pq) >= len(nums):
            left, i, j = heappop(pq)
            if right - left < ans[1] - ans[0]:
                ans = [left, right]
            if j + 1 < len(nums[i]):
                heappush(pq, [nums[i][j + 1], i, j + 1])
                right = max(right, nums[i][j + 1])

        return ans


print(Solution().smallestRange([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]))
