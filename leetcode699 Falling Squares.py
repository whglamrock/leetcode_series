
class Interval:
    def __init__(self, l, r, h):
        self.l = l
        self.r = r
        self.h = h



# O(N^2) naive solution but it should work in real interviews (but we also need to explain the segment tree idea).

class Solution(object):
    def fallingSquares(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        if not positions:
            return []

        intervals = []
        ans = []
        currMaxHeight = 0
        
        for left, width in positions:
            height = width
            for interval in intervals:
                if self.isOverlapping(left, left + width, interval.l, interval.r):
                    height = max(height, interval.h + width)
            intervals.append(Interval(left, left + width, height))
            currMaxHeight = max(currMaxHeight, height)
            ans.append(currMaxHeight)

        return ans

    def isOverlapping(self, l1, r1, l2, r2):
        if l1 >= r2 or l2 >= r1:
            return False
        return True



print Solution().fallingSquares([[1, 2], [2, 3], [6, 1]])