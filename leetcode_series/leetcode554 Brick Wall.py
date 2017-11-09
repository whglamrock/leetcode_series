
# simple hash map solution

from collections import defaultdict

class Solution(object):
    def leastBricks(self, wall):

        if not wall:
            return 0

        dic = defaultdict(int)
        totallength = sum(wall[0])
        for row in wall:
            widthsum = 0
            for width in row:
                widthsum += width
                if widthsum != totallength:
                    dic[widthsum] += 1

        numofrows = len(wall)
        ans = len(wall)
        for value in dic.values():
            ans = min(ans, numofrows - value)

        return ans



Sol = Solution()
wall = [[1,2,2,1],
 [3,1,2],
 [1,3,2],
 [2,4],
 [3,1,2],
 [1,3,1,1]]
print Sol.leastBricks(wall)
