from collections import deque
from typing import List

# remember to use chunkSum to avoid using index to calculate the bottom value (there are some annoying edge cases)
class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        indexToMaxLeftHeightSum = {}
        leftHeightSum = 0
        stack = [[-1, 0, 0]]
        for i, h in enumerate(maxHeights):
            while stack and stack[-1][2] > h:
                prevIndex, prevChunkSum, prevH = stack.pop()
                leftHeightSum -= prevChunkSum
            chunkSum = h * (i - stack[-1][0])
            leftHeightSum += chunkSum
            stack.append([i, chunkSum, h])
            indexToMaxLeftHeightSum[i] = leftHeightSum

        indexToMaxRightHeightSum = {}
        rightHeightSum = 0
        stack = deque([[len(maxHeights), 0, 0]])
        for i in range(len(maxHeights) - 1, -1, -1):
            h = maxHeights[i]
            while stack and stack[0][2] > h:
                prevIndex, prevChunkSum, prevH = stack.popleft()
                rightHeightSum -= prevChunkSum
            chunkSum = h * (stack[0][0] - i)
            rightHeightSum += chunkSum
            stack.appendleft([i, chunkSum, h])
            indexToMaxRightHeightSum[i] = rightHeightSum

        ans = 0
        for i in range(len(maxHeights)):
            ans = max(ans, indexToMaxLeftHeightSum[i] + indexToMaxRightHeightSum[i] - maxHeights[i])

        return ans


print(Solution().maximumSumOfHeights([5, 3, 4, 1, 1]))
print(Solution().maximumSumOfHeights([6, 5, 3, 9, 2, 7]))
print(Solution().maximumSumOfHeights([3, 2, 5, 5, 2, 3]))
