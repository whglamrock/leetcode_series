from typing import List

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        totalTime = 0
        i = 0
        while i < len(colors):
            if i == len(colors) - 1 or colors[i + 1] != colors[i]:
                i += 1
                continue

            maxTimeToRemove = neededTime[i]
            totalTimeToRemoveInCurr = neededTime[i]
            while i + 1 < len(colors) and colors[i + 1] == colors[i]:
                maxTimeToRemove = max(maxTimeToRemove, neededTime[i + 1])
                totalTimeToRemoveInCurr += neededTime[i + 1]
                i += 1
            totalTime += totalTimeToRemoveInCurr - maxTimeToRemove
            i += 1

        return totalTime
