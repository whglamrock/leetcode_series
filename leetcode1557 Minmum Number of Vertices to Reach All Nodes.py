from collections import defaultdict
from typing import List

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        nodeToSrcNode = defaultdict(set)
        for srcNode, node in edges:
            nodeToSrcNode[node].add(srcNode)

        ans = []
        for i in range(n):
            if i not in nodeToSrcNode:
                ans.append(i)
        return ans
