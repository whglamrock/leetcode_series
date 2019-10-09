
# Greedy Solution: from left to right, try to shoot as many balloons as possible with one arrow
# Note that we cannot sort by points[i][0];
    # e.g., try test case: [[9, 12], [1, 10], [4, 11], [8, 12], [3, 9], [6, 9], [6, 7]]

class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0

        points.sort(key = lambda x:x[1])
        currEnd = points[0][1]
        ans = 1

        for s, e in points:
            if s > currEnd:
                currEnd = e
                ans += 1

        return ans



print Solution().findMinArrowShots([[9, 12], [1, 10], [4, 11], [8, 12], [3, 9], [6, 9], [6, 7]])
print Solution().findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]])