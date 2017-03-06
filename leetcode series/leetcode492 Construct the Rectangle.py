# sqrt solution, not necessarily O(1), but O(logn), where n == area

import math
class Solution(object):
    def constructRectangle(self, area):

        ans = []
        for j in xrange(int(math.sqrt(area)), 0, -1):
            if area % j == 0:
                ans = [area/j, j]
                break

        return ans

