from collections import defaultdict, deque
from typing import List

# Basically equals to number of islands (Strictly O(n) solution): if 2 stones in a same row/column they belong to
# the same island. For an island, optimally we can remove all stones until the last one.
class Solution(object):
    def removeStones(self, stones: List[List[int]]) -> int:
        rows = defaultdict(set)
        cols = defaultdict(set)

        for i, j in stones:
            rows[i].add(j)
            cols[j].add(i)

        queue = deque()
        numOfIslands = 0
        for i, j in stones:
            # means the node has been removed by previous dfs
            if j not in rows[i]:
                continue
            queue.append((i, j))
            numOfIslands += 1
            while queue:
                x, y = queue.popleft()
                if x in rows:
                    rows[x].discard(y)
                    for y1 in rows[x]:
                        queue.append((x, y1))
                    del rows[x]
                if y in cols:
                    cols[y].discard(x)
                    for x1 in cols[y]:
                        queue.append((x1, y))
                    del cols[y]

        return len(stones) - numOfIslands
