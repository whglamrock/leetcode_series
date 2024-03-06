from collections import defaultdict
from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # not absolutely necessary but it can speed up the algorithm
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
                for nextNode in graph[node]:
                    graph[nextNode].discard(node)
                    if not graph[nextNode]:
                        del graph[nextNode]
                    # edge case: a ring of 4 nodes (or any even number of nodes)
                    if nextNode in nextTodo:
                        return False
                    nextTodo.add(nextNode)
                del graph[node]
            todo = nextTodo

        return len(visited) == n
