from typing import List

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        highestFromRight = 0
        indexes = []
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > highestFromRight:
                indexes.append(i)
                highestFromRight = heights[i]

        return indexes[::-1]


print(Solution().findBuildings([4, 3, 2, 1]))
print(Solution().findBuildings([4, 2, 3, 1]))
print(Solution().findBuildings([1, 3, 2, 4]))
