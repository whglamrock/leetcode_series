from collections import defaultdict
from typing import List

# below is essentially ranked union find with path compression. so time complexity is actually O(k * log(m * n)).
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        indexToIslandId = {}
        islandIdToIndexes = defaultdict(set)
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        islandId = 0
        ans = []
        for i, j in positions:
            if (i, j) in indexToIslandId:
                ans.append(len(islandIdToIndexes))
                continue

            connectedIslands = set()
            for deltaI, deltaJ in directions:
                ii, jj = i + deltaI, j + deltaJ
                if 0 <= ii < m and 0 <= jj < n and (ii, jj) in indexToIslandId:
                    connectedIslands.add(indexToIslandId[(ii, jj)])
            if connectedIslands:
                connectedIslands = sorted(connectedIslands, key=lambda x: -len(islandIdToIndexes[x]))
                biggestIslandId = connectedIslands[0]
                islandIdToIndexes[biggestIslandId].add((i, j))
                indexToIslandId[(i, j)] = biggestIslandId
                # union other islandIds' indexes
                for k in range(1, len(connectedIslands)):
                    connectedIndexes = islandIdToIndexes[connectedIslands[k]]
                    del islandIdToIndexes[connectedIslands[k]]
                    for index in connectedIndexes:
                        indexToIslandId[index] = biggestIslandId
                        islandIdToIndexes[biggestIslandId].add(index)
            else:
                indexToIslandId[(i, j)] = islandId
                islandIdToIndexes[islandId].add((i, j))
                islandId += 1
            ans.append(len(islandIdToIndexes))

        return ans


print(Solution().numIslands2(4, 4, [[0, 1], [0, 2], [1, 1], [1, 3], [2, 2], [3, 2], [1, 2]]))
print(Solution().numIslands2(3, 3, [[0, 0], [0, 1], [1, 2], [2, 1]]))
