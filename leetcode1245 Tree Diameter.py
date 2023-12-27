from collections import defaultdict
from typing import List, Dict

class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        if not edges:
            return 0

        nodeToConnectedNodes = defaultdict(set)
        nodeToDepths = defaultdict(list)
        for node, nextNode in edges:
            nodeToConnectedNodes[node].add(nextNode)
            nodeToConnectedNodes[nextNode].add(node)

        anyNode = edges[0][0]
        self.traverseTree(anyNode, nodeToConnectedNodes, nodeToDepths, -1)
        # print(nodeToDepths)
        ans = 0
        for node in nodeToDepths:
            if len(nodeToDepths[node]) == 1:
                ans = max(ans, nodeToDepths[node][0] - 1)
                continue
            longestAnd2ndLongestPaths = self.findLongestAnd2ndLongestPaths(nodeToDepths[node])
            ans = max(ans, longestAnd2ndLongestPaths[0] + longestAnd2ndLongestPaths[1] - 2)

        return ans

    def traverseTree(self, node: int, nodeToConnectedNodes: Dict[int, set], nodeToDepths: Dict[int, List[int]],
                     lastNode: int) -> int:
        # reached the end
        if len(nodeToConnectedNodes[node]) == 1 and list(nodeToConnectedNodes[node])[0] == lastNode:
            nodeToDepths[node].append(1)
            return 1
        for nextNode in nodeToConnectedNodes[node]:
            if nextNode == lastNode:
                continue
            nodeToDepths[node].append(1 + self.traverseTree(nextNode, nodeToConnectedNodes, nodeToDepths, node))

        return max(nodeToDepths[node])

    # it's assumed that paths has at least 2 elements
    def findLongestAnd2ndLongestPaths(self, depths: List[int]) -> List[int]:
        longest = max(depths[0], depths[1])
        secondLongest = min(depths[0], depths[1])
        for i in range(2, len(depths)):
            depth = depths[i]
            # need to update both
            if depth > longest:
                secondLongest = longest
                longest = depth
            elif depth > secondLongest:
                secondLongest = depth

        return [longest, secondLongest]


print(Solution().treeDiameter(edges=[[0, 1], [0, 2]]))
print(Solution().treeDiameter(edges=[[0, 1], [1, 2], [2, 3], [1, 4], [4, 5]]))
