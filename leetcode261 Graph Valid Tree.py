from collections import defaultdict
from typing import List


# Below is a solution without trimming the tree.
# Trimming the tree will also work, but the implementation is a bit different
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return n == 1

        graph = defaultdict(set)
        for i, j in edges:
            graph[i].add(j)
            graph[j].add(i)

        todo = {edges[0][0]}
        visitedNodeCount = 0

        while todo:
            nextTodo = set()
            for node in todo:
                visitedNodeCount += 1
                if node not in graph:
                    continue

                for connectedNode in graph[node]:
                    if connectedNode in todo or connectedNode in nextTodo:
                        return False
                    if connectedNode not in graph:
                        continue

                    graph[connectedNode].discard(node)
                    if not graph[connectedNode]:
                        del graph[connectedNode]
                    nextTodo.add(connectedNode)

                del graph[node]

            todo = nextTodo

        return visitedNodeCount == n
