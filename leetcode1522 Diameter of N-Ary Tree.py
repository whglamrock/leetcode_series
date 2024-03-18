from collections import defaultdict
from typing import Dict, List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def diameter(self, root: 'Node') -> int:
        nodeToPathLengths = defaultdict(list)
        self.traverseTree(root, nodeToPathLengths)
        ans = 0
        for node in nodeToPathLengths:
            if len(nodeToPathLengths[node]) == 1:
                ans = max(ans, nodeToPathLengths[node][0] - 1)
            else:
                longestAnd2ndLongestPaths = self.findLongestAnd2ndLongestPaths(nodeToPathLengths[node])
                ans = max(ans, longestAnd2ndLongestPaths[0] + longestAnd2ndLongestPaths[1] - 2)

        return ans

    def traverseTree(self, node: 'Node', nodeToDepths: Dict['Node', List[int]]) -> int:
        if not node.children:
            nodeToDepths[node].append(1)
            return 1
        for child in node.children:
            nodeToDepths[node].append(1 + self.traverseTree(child, nodeToDepths))

        return max(nodeToDepths[node])

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
