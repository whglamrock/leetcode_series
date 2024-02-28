from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.yDepth = 0
        self.xDepth = 0
        self.yParent = None
        self.xParent = None

    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.xParent, self.yParent = None, None
        self.xDepth, self.yDepth = 0, 0
        self.dfs(root, x, y, 0)
        return self.xDepth == self.yDepth and self.xParent != self.yParent

    def dfs(self, root: Optional[TreeNode], x: int, y: int, depth: int):
        if root and (root.left and root.left.val == x) or (root.right and root.right.val == x):
            self.xParent = root
        if root and (root.left and root.left.val == y) or (root.right and root.right.val == y):
            self.yParent = root
        if root.val == x:
            self.xDepth = depth
        if root.val == y:
            self.yDepth = depth
        if root.left:
            self.dfs(root.left, x, y, depth + 1)
        if root.right:
            self.dfs(root.right, x, y, depth + 1)
