from collections import deque
from typing import List

# double the nums array + decreasing queue from right to left
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums = nums + nums
        n = len(nums)
        decreasingQueue = deque()
        for i in range(n - 1, n // 2 - 1, -1):
            while decreasingQueue and decreasingQueue[0][1] <= nums[i]:
                decreasingQueue.popleft()
            decreasingQueue.appendleft([i, nums[i]])

        ans = [-1] * (n // 2)
        for i in range(n // 2 - 1, -1, -1):
            while decreasingQueue and decreasingQueue[0][1] <= nums[i]:
                decreasingQueue.popleft()
            if decreasingQueue:
                ans[i] = decreasingQueue[0][1]
            decreasingQueue.appendleft([i, nums[i]])
            # i + n // 2 - 1 corresponds to the next for loop
            while decreasingQueue and decreasingQueue[-1][0] >= i + n // 2 - 1:
                decreasingQueue.pop()

        return ans
