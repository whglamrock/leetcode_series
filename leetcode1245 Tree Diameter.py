from collections import defaultdict
from typing import List, Dict, Tuple

class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        if not edges:
            return 0

        graph = defaultdict(set)
        for i, j in edges:
            graph[i].add(j)
            graph[j].add(i)

        nodeToDepths = defaultdict(list)
        anyNode = edges[0][0]
        self.dfs(graph, nodeToDepths, anyNode, -1)

        ans = 0
        for node, depths in nodeToDepths.items():
            if len(depths) == 1:
                ans = max(ans, depths[0] - 1)
                continue
            longest, secondLongest = self.findLongestAndSecondLongestDepths(depths)
            ans = max(ans, longest + secondLongest - 2)

        return ans

    def dfs(self, graph: Dict[int, set], nodeToDepths: Dict[int, list], node: int, lastNode: int) -> int:
        if len(graph[node]) == 1 and lastNode in graph[node]:
            nodeToDepths[node] = [1]
            return 1

        depths = []
        for nextNode in graph[node]:
            if nextNode == lastNode:
                continue
            depths.append(1 + self.dfs(graph, nodeToDepths, nextNode, node))
        nodeToDepths[node] = depths
        return max(depths)

    def findLongestAndSecondLongestDepths(self, depths: List[int]) -> Tuple[int, int]:
        longest, secondLongest = -10001, -10002
        for depth in depths:
            if depth > longest:
                secondLongest = longest
                longest = depth
            elif depth > secondLongest:
                secondLongest = depth

        return longest, secondLongest


print(Solution().treeDiameter(edges=[[0, 1], [0, 2]]))
print(Solution().treeDiameter(edges=[[0, 1], [1, 2], [2, 3], [1, 4], [4, 5]]))
