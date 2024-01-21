from collections import deque
from typing import List

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        decreasingQueue = deque()
        ans = deque()
        for i in range(len(heights) - 1, -1, -1):
            numOfPeopleShorter = 0
            while decreasingQueue and decreasingQueue[0] < heights[i]:
                decreasingQueue.popleft()
                numOfPeopleShorter += 1
            if decreasingQueue:
                ans.appendleft(numOfPeopleShorter + 1)
            else:
                ans.appendleft(numOfPeopleShorter)
            decreasingQueue.appendleft(heights[i])

        return list(ans)


print(Solution().canSeePersonsCount([10, 6, 8, 5, 11, 9]))
print(Solution().canSeePersonsCount([5, 1, 2, 3, 10]))
print(Solution().canSeePersonsCount([4, 3, 2, 1]))
