from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [0] * n

        for i in range(n):
            # has been painted
            if colors[i]:
                continue

            colors[i] = 1
            # one BFS will paint all connected nodes
            todo = {i}
            while todo:
                nextTodo = set()
                for node in todo:
                    for connectedNode in graph[node]:
                        if not colors[connectedNode]:
                            colors[connectedNode] = -colors[node]
                            nextTodo.add(connectedNode)
                        elif colors[connectedNode] != -colors[node]:
                            return False

                todo = nextTodo

        return True
