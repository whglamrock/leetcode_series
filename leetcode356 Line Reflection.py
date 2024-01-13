from typing import List

# the description is pretty vague, see: https://leetcode.com/problems/line-reflection/solutions/202760/bad-problem-description-come-and-read-what-it-really-means/
class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        pointsSet = set()
        for x, y in points:
            pointsSet.add((x, y))

        sumX = 0
        for x, y in pointsSet:
            sumX += x

        middleX = sumX / len(pointsSet)
        for x, y in pointsSet:
            reflectedX = int(2 * middleX - x)
            if (reflectedX, y) not in pointsSet:
                return False

        return True


print(Solution().isReflected([[-16, 1], [16, 1], [16, 1]]))
