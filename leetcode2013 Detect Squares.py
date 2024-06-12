from collections import defaultdict, Counter
from typing import List


class DetectSquares:
    def __init__(self):
        self.xToYCounts = defaultdict(Counter)

    def add(self, point: List[int]) -> None:
        self.xToYCounts[point[0]][point[1]] += 1

    def count(self, point: List[int]) -> int:
        print(self.xToYCounts)
        x, y = point
        if x not in self.xToYCounts:
            return 0

        count = 0
        for yy in self.xToYCounts[x]:
            if yy == y:
                continue

            length = abs(yy - y)
            # the other edge is on the left side
            leftX = x - length
            if leftX in self.xToYCounts:
                if y in self.xToYCounts[leftX] and yy in self.xToYCounts[leftX]:
                    count += self.xToYCounts[leftX][y] * self.xToYCounts[leftX][yy] * self.xToYCounts[x][yy]

            # the other edge is on the right side
            rightX = x + length
            if rightX in self.xToYCounts:
                if y in self.xToYCounts[rightX] and yy in self.xToYCounts[rightX]:
                    count += self.xToYCounts[rightX][y] * self.xToYCounts[rightX][yy] * self.xToYCounts[x][yy]

        return count


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
