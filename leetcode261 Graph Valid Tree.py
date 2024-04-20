from collections import defaultdict
from typing import List

# Below is a solution without trimming the tree.
# Trimming the tree will also work, but the implementation is a bit different
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        graph = defaultdict(set)
        for i, j in edges:
            graph[i].add(j)
            graph[j].add(i)

        todo = {0}
        visited = set()
        while todo:
            nextTodo = set()
            for node in todo:
                if node in visited:
                    return False
                visited.add(node)
                for connectedNode in graph[node]:
                    if connectedNode in nextTodo:
                        return False
                    if connectedNode in visited:
                        continue
                    nextTodo.add(connectedNode)

            todo = nextTodo

        return len(visited) == n
