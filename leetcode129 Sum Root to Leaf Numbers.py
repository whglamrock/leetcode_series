from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.ans = 0

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.ans = 0
        self.dfs(root, 0)
        return self.ans

    def dfs(self, node: TreeNode, currVal: int):
        val = currVal * 10 + node.val
        if not node.left and not node.right:
            self.ans += val
            return
        if node.left:
            self.dfs(node.left, val)
        if node.right:
            self.dfs(node.right, val)
