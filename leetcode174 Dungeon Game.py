from typing import List

# See explanation from: https://discuss.leetcode.com/topic/7633/best-solution-i-have-found-with-explanations
# We cannot solve this problem by starting from top left. Starting from bottom right, you won't have to care about
# the accumulated health value: you only need to care about the minHealth from right/down
class Solution(object):
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        minHealth = [[1 for j in range(n)] for i in range(m)]
        if dungeon[-1][-1] <= 0:
            minHealth[-1][-1] = -dungeon[-1][-1] + 1

        for i in range(m - 2, -1, -1):
            minHealth[i][-1] = max(1, minHealth[i + 1][-1] - dungeon[i][-1])
        for j in range(n - 2, -1, -1):
            minHealth[-1][j] = max(1, minHealth[-1][j + 1] - dungeon[-1][j])

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                # minHealth[i][j] + dungeon[i][j] -> minHealth[i + 1][j] or minHealth[i][j + 1]
                # don't forget to compare with 1 to get max, because the needed min health has to be at least 1
                minHealth[i][j] = max(1, min(minHealth[i + 1][j], minHealth[i][j + 1]) - dungeon[i][j])

        return minHealth[0][0]


dungeon = [
    [-2, -3, 3],
    [-5, -10, 1],
    [10, 30, -5]
]
print(Solution().calculateMinimumHP(dungeon))


'''
from heapq import *

# priority queue solution that got TLE
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        pq = [[-dungeon[0][0], 0, 0, -dungeon[0][0] + 1 if dungeon[0][0] <= 0 else 1]]
        
        while pq:
            currVal, i, j, minInitialHp = heappop(pq)
            currVal = -currVal
            if i == m - 1 and j == n - 1:
                return minInitialHp
            
            if i + 1 < m:
                newVal = currVal + dungeon[i + 1][j]
                newHp = -newVal + 1 if newVal <= 0 else 0
                newMinInitialHp = max(minInitialHp, newHp)
                heappush(pq, [-newVal, i + 1, j, newMinInitialHp])
            if j + 1 < n:
                newVal = currVal + dungeon[i][j + 1]
                newHp = -newVal + 1 if newVal <= 0 else 0
                newMinInitialHp = max(minInitialHp, newHp)
                heappush(pq, [-newVal, i, j + 1, newMinInitialHp])
        
        return 1
'''