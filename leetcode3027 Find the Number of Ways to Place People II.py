from typing import List


# The problem description is extremely vague about "Alice and Bob" can be in a line. Does it mean the line is
# horizontal or vertical?
# If there's no requirement of Alice and Bob can stand in a line, we can simply do points.sort().
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        # sort by y coordinates in descending order to deal with edge case where Alice & Bob stand in a vertical line
        points.sort(key=lambda x: (x[0], -x[1]))

        count = 0
        n = len(points)
        for i in range(n - 1):
            currMaxY = None
            # find the maxY that's in the bottom right corner of points[i]
            for j in range(i + 1, n):
                if points[j][1] > points[i][1]:
                    continue

                if currMaxY is None or currMaxY < points[j][1]:
                    count += 1

                if currMaxY is None:
                    currMaxY = points[j][1]
                else:
                    currMaxY = max(currMaxY, points[j][1])

        return count
