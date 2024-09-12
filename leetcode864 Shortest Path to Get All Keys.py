from collections import deque
from typing import List


# It's more realistic to remember this solution (especially the dedupe handling)
# as there is way too many annoying edge test cases.
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        numOfKeys = 0
        startI, startJ = 0, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    startI = i
                    startJ = j
                elif grid[i][j] in "abcdef":
                    numOfKeys += 1

        queue = deque([[startI, startJ, 0, ".@abcdef", 0]])
        visited = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while queue:
            i, j, steps, walkableChars, collectedKeys = queue.popleft()

            # we have found a new key we didn't collect before
            if grid[i][j] in "abcdef" and grid[i][j].upper() not in walkableChars:
                # adding the upper case letters for easier check for neighbor cells.
                walkableChars += grid[i][j].upper()
                collectedKeys += 1

            if collectedKeys == numOfKeys:
                return steps

            for deltaI, deltaJ in directions:
                ii = i + deltaI
                jj = j + deltaJ
                if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] in walkableChars:
                    # notice the dedupe logic here, we allow same set of keys to be added in different order
                    # e.g., ".@abcdef" + AB != ".@abcdef" + BA
                    if (ii, jj, walkableChars) not in visited:
                        visited.add((ii, jj, walkableChars))
                        queue.append([ii, jj, steps + 1, walkableChars, collectedKeys])

        return -1


print(Solution().shortestPathAllKeys(
    ["Dd#b@",
     ".fE.e",
     "##.B.",
     "#.cA.",
     "aF.#C"]))
