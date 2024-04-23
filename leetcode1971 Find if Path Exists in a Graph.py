from collections import defaultdict
from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(set)
        for i, j in edges:
            graph[i].add(j)
            graph[j].add(i)

        todo = {source}
        while todo:
            nextTodo = set()
            for node in todo:
                if node == destination:
                    return True
                if node not in graph:
                    continue
                for connectedNode in graph[node]:
                    nextTodo.add(connectedNode)
                    graph[connectedNode].discard(node)
                    if not graph[connectedNode]:
                        del graph[connectedNode]
                del graph[node]

            todo = nextTodo

        return False
