# see explanation from: https://discuss.leetcode.com/topic/7633/best-solution-i-have-found-with-explanations
# The key is to fill the dp table from bottom-right to top-left.
#   See reason from: https://discuss.leetcode.com/topic/6906/who-can-explain-why-from-the-bottom-right-corner-to-left-top/2
# P.S. when we find it's hard to do it from top-left, try it another way.

class Solution(object):
    def calculateMinimumHP(self, dungeon):

        if not dungeon or not dungeon[0]:
            return 1

        m, n = len(dungeon), len(dungeon[0])
        minInitHealth = [[1 for j in xrange(n)] for i in xrange(m)]

        for i in xrange(m - 1, -1, -1):
            for j in xrange(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    minInitHealth[i][j] = max(1, 1 - dungeon[-1][-1])
                elif i == m - 1:
                    minInitHealth[i][j] = max(1, minInitHealth[i][j + 1] - dungeon[i][j])
                elif j == n - 1:
                    minInitHealth[i][j] = max(1, minInitHealth[i + 1][j] - dungeon[i][j])
                else:
                    minInitHealth[i][j] = max(1, min(minInitHealth[i + 1][j], minInitHealth[i][j + 1]) - dungeon[i][j])

        return minInitHealth[0][0]

