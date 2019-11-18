
# simple hash map solution

from collections import defaultdict

class Solution(object):
    def leastBricks(self, wall):

        if not wall:
            return 0

        widthSumCount = defaultdict(int)
        totalWidth = sum(wall[0])

        for row in wall:
            widthSum = 0
            for width in row:
                widthSum += width
                if widthSum != totalWidth:
                    widthSumCount[widthSum] += 1

        ans = len(wall)
        if widthSumCount:
            ans = min(len(wall) - max(widthSumCount.values()), ans)

        return ans



wall = [
 [1,2,2,1],
 [3,1,2],
 [1,3,2],
 [2,4],
 [3,1,2],
 [1,3,1,1]]
print Solution().leastBricks(wall)
