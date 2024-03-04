from collections import defaultdict
from typing import List

# The idea is cut the leaves. But we have to know when to stop (there should be only 1 or 2 nodes left).
# When we trim the connection of leaves from the graph, don't delete the graph[connectedNode] as the "connectedNode"
# may be the last node we need to keep.
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        if n == 2:
            return [0, 1]

        graph = defaultdict(set)
        for i, j in edges:
            graph[i].add(j)
            graph[j].add(i)

        todo = set()
        for i in range(n):
            if len(graph[i]) == 1:
                todo.add(i)

        while todo:
            nextTodo = set()
            for node in todo:
                if node not in graph:
                    continue
                for connectedNode in graph[node]:
                    if connectedNode not in graph:
                        continue
                    graph[connectedNode].discard(node)
                    if len(graph[connectedNode]) == 1:
                        nextTodo.add(connectedNode)
                del graph[node]

            if len(graph) <= 2:
                break
            todo = nextTodo

        return list(graph.keys())
