
from collections import deque

# no need to use union find. DFS solution can achieve O(N^2) time complexity

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M:
            return 0

        ans = 0
        for i in xrange(len(M)):
            for j in xrange(len(M)):
                if M[i][j] == 1:
                    ans += 1
                    M[i][j] = 0
                    self.dfs(i, j, M)

        return ans

    def dfs(self, i, j, M):
        queue = deque()
        queue.append((i, j))
        visitedRows = set()
        visitedCols = set()
        while queue:
            x, y = queue.popleft()
            if x not in visitedRows:
                for y1 in xrange(len(M)):
                    if M[x][y1] == 1:
                        queue.append((x, y1))
                        M[x][y1] = 0
            if y not in visitedCols:
                for x1 in xrange(len(M)):
                    if M[x1][y] == 1:
                        queue.append((x1, y))
                        M[x1][y] = 0
            visitedRows.add(x)
            visitedCols.add(y)



print Solution().findCircleNum([
    [1,1,0],
    [1,1,0],
    [0,0,1]
])


