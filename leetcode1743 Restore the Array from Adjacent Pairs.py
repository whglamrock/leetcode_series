from collections import defaultdict
from typing import List

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        numToNeighbors = defaultdict(set)
        for i, j in adjacentPairs:
            numToNeighbors[i].add(j)
            numToNeighbors[j].add(i)

        startAndEnd = []
        for num in numToNeighbors:
            if len(numToNeighbors[num]) == 1:
                startAndEnd.append(num)

        ans = []
        curr = startAndEnd[0]
        while numToNeighbors:
            ans.append(curr)
            neighbors = numToNeighbors[curr]
            del numToNeighbors[curr]
            for neighbor in neighbors:
                numToNeighbors[neighbor].discard(curr)
                if len(numToNeighbors[neighbor]) == 1:
                    curr = neighbor
                if not numToNeighbors[neighbor]:
                    del numToNeighbors[neighbor]

        return ans + [startAndEnd[1]]


print(Solution().restoreArray([[100000, -100000]]))
print(Solution().restoreArray([[4, -2], [1, 4], [-3, 1]]))
print(Solution().restoreArray([[2, 1], [3, 4], [3, 2]]))
