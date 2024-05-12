from heapq import *
from typing import List

# the strategy is init the pq with all row[0]'s and keep popping out the smallest, and calculate the range
# the tricky part is to figure out that the strategy can guarantee the optimal range is reached:
# 1) assuming len(nums) == k, we keep a min heap of k numbers (each from nums[i]);
# 2) within each row, we try to make the current nums[i][j] the left bound of the range
# 3) the min of such nums[i][j] is smaller than all other elements in the minHeap, so for all other nums[ii][j]
# where ii != i, all nums[ii][j + 1:] cannot form any smaller range with nums[i][j] being the left bound,
# so we have to move nums[i][j] to nums[i][j + 1]
# 4) we keep doing this, until we exhaust all nums[i][j] for certain row i, which means we exhausted all left bound
# <= nums[i][-1]
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
