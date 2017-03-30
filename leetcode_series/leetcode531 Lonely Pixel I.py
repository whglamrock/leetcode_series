
from collections import defaultdict

# this should've been an easy question

class Solution(object):
    def findLonelyPixel(self, picture):

        if not picture or not picture[0]:
            return 0

        rows, cols = defaultdict(int), defaultdict(int)
        m, n = len(picture), len(picture[0])

        for i in xrange(m):
            for j in xrange(n):
                if picture[i][j] == 'B':
                    rows[i] += 1
                    cols[j] += 1

        ans = 0
        for i in xrange(m):
            for j in xrange(n):
                if picture[i][j] == 'B' and rows[i] == 1 and cols[j] == 1:
                    ans += 1

        return ans