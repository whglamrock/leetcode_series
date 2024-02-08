from typing import Optional, Tuple

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.maxDiff = 0

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.maxDiff = 0
        self.dfs(root)
        return self.maxDiff

    def dfs(self, node: Optional[TreeNode]) -> Tuple[int, int]:
        if not node.left and not node.right:
            return node.val, node.val

        minVal, maxVal = node.val, node.val
        if node.left:
            minOfLeftChild, maxOfLeftChild = self.dfs(node.left)
            minVal, maxVal = min(minVal, minOfLeftChild), max(maxVal, maxOfLeftChild)
            self.maxDiff = max(self.maxDiff, abs(node.val - minOfLeftChild), abs(node.val - maxOfLeftChild))
        if node.right:
            minOfRightChild, maxOfRightChild = self.dfs(node.right)
            minVal, maxVal = min(minVal, minOfRightChild), max(maxVal, maxOfRightChild)
            self.maxDiff = max(self.maxDiff, abs(node.val - minOfRightChild), abs(node.val - maxOfRightChild))

        return minVal, maxVal
