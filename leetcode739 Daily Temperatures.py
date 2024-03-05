from collections import deque
from typing import List

# intuition: keep a decreasing stack scanning from right to left
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        decreasingQueue = deque()
        n = len(temperatures)
        ans = [0] * n
        for i in range(n - 1, -1, -1):
            while decreasingQueue and temperatures[i] >= decreasingQueue[0][1]:
                decreasingQueue.popleft()
            if decreasingQueue:
                ans[i] = decreasingQueue[0][0] - i
            decreasingQueue.appendleft([i, temperatures[i]])

        return ans


print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
