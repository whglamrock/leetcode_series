
# See explanation from: https://discuss.leetcode.com/topic/7633/best-solution-i-have-found-with-explanations
# This question should be viewed as a very special/typical case where we need top-down (starting from final state) solution

class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if not dungeon or not dungeon[0]:
            return 0

        m, n = len(dungeon), len(dungeon[0])
        minHealth = [[1 for j in xrange(n)] for i in xrange(m)]
        if dungeon[-1][-1] <= 0:
            minHealth[-1][-1] = -dungeon[-1][-1] + 1

        for i in xrange(m - 2, -1, -1):
            # minHealth[i][-1] + dungeon[i][-1] = minHealth[i + 1][-1]
            minHealth[i][-1] = max(1, minHealth[i + 1][-1] - dungeon[i][-1])
        for j in xrange(n - 2, -1, -1):
            # minHealth[-1][j] + dungeon[-1][j] = minHealth[-1][j + 1]
            minHealth[-1][j] = max(1, minHealth[-1][j + 1] - dungeon[-1][j])

        for i in xrange(m - 2, -1, -1):
            for j in xrange(n - 2, -1, -1):
                # minHealth[i][j] + dungeon[i][j] -> minHealth[i + 1][j] or minHealth[i][j + 1]
                # don't forget to compare with 1 to get max, because the needed min health has to be at least 1
                minHealth[i][j] = max(1, min(minHealth[i + 1][j], minHealth[i][j + 1]) - dungeon[i][j])

        return minHealth[0][0]



dungeon = [
    [-2,-3,3],
    [-5,-10,1],
    [10,30,-5]
]
print Solution().calculateMinimumHP(dungeon)