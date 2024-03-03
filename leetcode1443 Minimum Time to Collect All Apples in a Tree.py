from collections import defaultdict
from typing import List

# Idea: trim the non-apple left nodes but not trim 0 (most important pitfall)!
# Then each edge corresponds to 2 seconds of time.
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(set)
        for node, nextNode in edges:
            graph[node].add(nextNode)
            graph[nextNode].add(node)

        # get the leaf nodes
        leafNodes = set()
        for i in range(1, n):
            if i not in graph:
                continue
            if len(graph[i]) == 1 and not hasApple[i]:
                leafNodes.add(i)

        # bfs to trim the leaf nodes
        todo = leafNodes
        while todo:
            nextTodo = set()
            for node in todo:
                # no need to check if node not in graph
                for nextNode in graph[node]:
                    # also no need to check if nextNode is in graph
                    graph[nextNode].discard(node)
                    # be really careful about not trimming 0 here
                    if nextNode != 0 and len(graph[nextNode]) == 1 and not hasApple[nextNode]:
                        nextTodo.add(nextNode)
                del graph[node]
            todo = nextTodo

        return sum([len(edgesOfEachNode) for edgesOfEachNode in graph.values()])


print(Solution().minTime(n=7, edges=[[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
                         hasApple=[False, False, True, False, True, True, False]))
print(Solution().minTime(n=7, edges=[[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
                         hasApple=[False, False, True, False, False, True, False]))
print(Solution().minTime(n=5, edges=[[0, 1], [0, 2], [1, 3], [0, 4]], hasApple=[False, False, False, True, False]))
