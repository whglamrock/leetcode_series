from collections import defaultdict
from typing import Optional, Dict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        levelToSum = defaultdict(int)
        self.traverseTree(root, levelToSum, 1)

        maxSum = max(levelToSum.values())
        minLevel = 2147483647
        for level in levelToSum:
            if levelToSum[level] != maxSum:
                continue
            minLevel = min(minLevel, level)

        return minLevel

    def traverseTree(self, node: Optional[TreeNode], levelToSum: Dict[int, int], level: int):
        levelToSum[level] += node.val
        if node.left:
            self.traverseTree(node.left, levelToSum, level + 1)
        if node.right:
            self.traverseTree(node.right, levelToSum, level + 1)
