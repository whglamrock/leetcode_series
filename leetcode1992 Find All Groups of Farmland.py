from typing import Tuple, List

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        ans = []
        m, n = len(land), len(land[0])
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    bottomRightI, bottomRightJ = self.dfs(land, i, j)
                    ans.append([i, j, bottomRightI, bottomRightJ])

        return ans

    def dfs(self, land: List[List[int]], i: int, j: int) -> Tuple[int, int]:
        m, n = len(land), len(land[0])
        land[i][j] = 0
        bottomRightI, bottomRightJ = i, j
        if i + 1 < m and land[i + 1][j] == 1:
            downI, downJ = self.dfs(land, i + 1, j)
            bottomRightI, bottomRightJ = max(bottomRightI, downI), max(bottomRightJ, downJ)
        if j + 1 < n and land[i][j + 1] == 1:
            rightI, rightJ = self.dfs(land, i, j + 1)
            bottomRightI, bottomRightJ = max(bottomRightI, rightI), max(bottomRightJ, rightJ)

        return bottomRightI, bottomRightJ
