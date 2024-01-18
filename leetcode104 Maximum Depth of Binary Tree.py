from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.ans = None

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.traverse(root, 1)
        return self.ans

    def traverse(self, root: Optional[TreeNode], depth: int):
        if not root:
            return
        self.ans = max(self.ans, depth)
        self.traverse(root.left, depth + 1)
        self.traverse(root.right, depth + 1)
