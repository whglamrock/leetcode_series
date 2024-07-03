from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        traversal = self.dfs(root)

        minDiff = traversal[1] - traversal[0]
        for i in range(1, len(traversal) - 1):
            currVal, nextVal = traversal[i], traversal[i + 1]
            minDiff = min(minDiff, nextVal - currVal)

        return minDiff

    def dfs(self, node: Optional[TreeNode]) -> List[int]:
        if not node:
            return []

        if not node.left and not node.right:
            return [node.val]

        traversal = [node.val]
        if node.left:
            traversal = self.dfs(node.left) + [node.val]
        if node.right:
            traversal += self.dfs(node.right)

        return traversal
