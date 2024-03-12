from collections import defaultdict
from typing import List

# Most importantly we need to realize: for an island, optimally we can remove all stones until the last one. so this
# problem becomes a number of island problem
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        xToYs, yToXs = defaultdict(set), defaultdict(set)
        for x, y in stones:
            xToYs[x].add(y)
            yToXs[y].add(x)

        numOfIslands = 0
        for x, y in stones:
            # this stone has been removed
            if x not in xToYs or y not in xToYs[x]:
                continue
            numOfIslands += 1
            # bfs
            todo = {(x, y)}
            visited = set()
            while todo:
                nextTodo = set()
                for i, j in todo:
                    visited.add((i, j))
                    # search for the same ys
                    xToYs[i].discard(j)
                    if not xToYs[i]:
                        del xToYs[i]
                    for jj in xToYs[i]:
                        if (i, jj) in visited:
                            continue
                        nextTodo.add((i, jj))
                    # search for the same xs
                    yToXs[j].discard(i)
                    if not yToXs[j]:
                        del yToXs[j]
                    for ii in yToXs[j]:
                        if (ii, j) in visited:
                            continue
                        nextTodo.add((ii, j))
                todo = nextTodo

        return len(stones) - numOfIslands
