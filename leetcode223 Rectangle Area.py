class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area1, area2 = (ax2 - ax1) * (ay2 - ay1), (bx2 - bx1) * (by2 - by1)
        # completely no overlapping
        if ax2 < bx1 or ay2 < by1 or bx2 < ax1 or by2 < ay1:
            return area1 + area2

        sortedXs, sortedYs = sorted([ax1, ax2, bx1, bx2]), sorted([ay1, ay2, by1, by2])
        overlappingArea = (sortedXs[2] - sortedXs[1]) * (sortedYs[2] - sortedYs[1])
        return area1 + area2 - overlappingArea
