from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.ans = []

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.ans = 0
        self.dfs(root, low, high)
        return self.ans

    def dfs(self, node: Optional[TreeNode], low: int, high: int):
        if not node:
            return
        if node.val < low:
            self.dfs(node.right, low, high)
            return
        if node.val > high:
            self.dfs(node.left, low, high)
            return

        self.ans += node.val
        self.dfs(node.left, low, high)
        self.dfs(node.right, low, high)
