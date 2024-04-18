from collections import defaultdict
from typing import List, Dict

class Solution:
    def __init__(self):
        self.diameter = 0

    def treeDiameter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        for i, j in edges:
            graph[i].add(j)
            graph[j].add(i)

        self.diameter = 0
        self.dfs(0, graph, -1)
        return self.diameter - 1

    # returns the max depth from this node
    def dfs(self, node: int, graph: Dict[int, set], lastNode: int) -> int:
        if len(graph[node]) == 1 and list(graph[node])[0] == lastNode:
            return 1

        maxDepth, secondMaxDepth = 0, 0
        for connectedNode in graph[node]:
            if connectedNode == lastNode:
                continue
            depthFromChild = self.dfs(connectedNode, graph, node)
            if depthFromChild > maxDepth:
                secondMaxDepth = maxDepth
                maxDepth = depthFromChild
            elif depthFromChild > secondMaxDepth:
                secondMaxDepth = depthFromChild

        self.diameter = max(self.diameter, maxDepth + secondMaxDepth + 1)
        return maxDepth + 1


print(Solution().treeDiameter(edges=[[0, 1], [0, 2]]))
print(Solution().treeDiameter(edges=[[0, 1], [1, 2], [2, 3], [1, 4], [4, 5]]))
