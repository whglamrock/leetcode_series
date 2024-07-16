from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacificTodo = set()
        atlanticTodo = set()
        for i in range(m):
            pacificTodo.add((i, 0))
            atlanticTodo.add((i, n - 1))
        for j in range(n):
            pacificTodo.add((0, j))
            atlanticTodo.add((m - 1, j))

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        # bfs for pacific
        visitedForPacific = set()
        while pacificTodo:
            nextPacificTodo = set()
            for i, j in pacificTodo:
                visitedForPacific.add((i, j))
                for deltaI, deltaJ in directions:
                    ii, jj = i + deltaI, j + deltaJ
                    if ii < 0 or ii >= m or jj < 0 or jj >= n or (ii, jj) in visitedForPacific or (
                    ii, jj) in pacificTodo:
                        continue
                    if heights[i][j] <= heights[ii][jj]:
                        nextPacificTodo.add((ii, jj))

            pacificTodo = nextPacificTodo

        # bfs for atlantic
        visitedForAtlantic = set()
        while atlanticTodo:
            nextAtlanticTodo = set()
            for i, j in atlanticTodo:
                visitedForAtlantic.add((i, j))
                for deltaI, deltaJ in directions:
                    ii, jj = i + deltaI, j + deltaJ
                    if ii < 0 or ii >= m or jj < 0 or jj >= n or (ii, jj) in visitedForAtlantic or (
                    ii, jj) in atlanticTodo:
                        continue
                    if heights[i][j] <= heights[ii][jj]:
                        nextAtlanticTodo.add((ii, jj))

            atlanticTodo = nextAtlanticTodo

        commonIndexes = visitedForPacific.intersection(visitedForAtlantic)
        ans = []
        for item in commonIndexes:
            ans.append(list(item))
        return ans


print(Solution().pacificAtlantic(heights=[[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]))
