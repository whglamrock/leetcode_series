from collections import defaultdict
from typing import List

class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        indexToClosestLeftCandle = {}
        candleIndex = None
        for i, char in enumerate(s):
            if s[i] == '|':
                candleIndex = i
            if candleIndex is not None:
                indexToClosestLeftCandle[i] = candleIndex

        indexToClosestRightCandle = {}
        candleIndex = None
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '|':
                candleIndex = i
            if candleIndex is not None:
                indexToClosestRightCandle[i] = candleIndex

        # P.S. the index to numOfPlates in left is inclusive, V.S. exclusive in right.
        # This is to avoid double deduction when removing the plates in right of J, we accidentally remove j (if j is *)
        platesInLeft = 0
        indexToNumOfPlatesInLeft = defaultdict(int)
        for i, char in enumerate(s):
            if char == '*':
                if i in indexToClosestLeftCandle and i in indexToClosestRightCandle:
                    platesInLeft += 1
            indexToNumOfPlatesInLeft[i] = platesInLeft

        platesInRight = 0
        indexToNumOfPlatesInRight = defaultdict(int)
        for i in range(len(s) - 1, -1, -1):
            char = s[i]
            if char == '*':
                if i in indexToClosestLeftCandle and i in indexToClosestRightCandle:
                    indexToNumOfPlatesInRight[i] = platesInRight
                    platesInRight += 1
            else:
                indexToNumOfPlatesInRight[i] = platesInRight

        ans = []
        for i, j in queries:
            platesInLeftOfJ = indexToNumOfPlatesInLeft[j]
            platesInRightOfJ = indexToNumOfPlatesInRight[j]

            if i not in indexToClosestRightCandle:
                ans.append(0)
                continue
            closestCandleIndexInRightOfI = indexToClosestRightCandle[i]
            if j not in indexToClosestLeftCandle:
                ans.append(0)
                continue
            closestCandleIndexInLeftOfJ = indexToClosestLeftCandle[j]

            numOfPlatesToRemoveInRight = indexToNumOfPlatesInRight[closestCandleIndexInLeftOfJ] - platesInRightOfJ
            numOfPlatesToRemoveInLeft = indexToNumOfPlatesInLeft[closestCandleIndexInRightOfI]
            # P.S. there are edge cases where only 1 candle or no candle exists in range
            ans.append(max(platesInLeftOfJ - numOfPlatesToRemoveInLeft - numOfPlatesToRemoveInRight, 0))

        return ans
