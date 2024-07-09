from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.dfs(root)
        return self.ans - 1

    def dfs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        maxLenFromRoot = 1
        diameter = 1
        if root.left:
            maxLenFromLeftChild = self.dfs(root.left)
            maxLenFromRoot += maxLenFromLeftChild
            diameter += maxLenFromLeftChild
        if root.right:
            maxLenFromRightChild = self.dfs(root.right)
            maxLenFromRoot = max(maxLenFromRoot, 1 + maxLenFromRightChild)
            diameter += maxLenFromRightChild

        self.ans = max(self.ans, diameter)
        return maxLenFromRoot
