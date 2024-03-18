from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.minimumDepth = 0

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.minimumDepth = 0
        self.dfs(root, 1)
        return self.minimumDepth

    def dfs(self, node: Optional[TreeNode], depth: int):
        # leaf
        if not node.left and not node.right:
            if not self.minimumDepth:
                self.minimumDepth = depth
            else:
                self.minimumDepth = min(self.minimumDepth, depth)
            return

        if node.left:
            self.dfs(node.left, depth + 1)
        if node.right:
            self.dfs(node.right, depth + 1)
