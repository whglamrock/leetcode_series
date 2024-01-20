from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.ans = 0

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.ans = 0
        self.dfs(root)
        # minus one because it asks for the length of path not number of nodes
        return self.ans - 1

    def dfs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # the longestPath passing through the current root (root might be in the middle)
        longestPathPassingThrough = 1
        # the longestPath starting from root, which is what we return (to the parent)
        longestPathFromRoot = 1
        longestPathFromLeft = self.dfs(root.left)
        longestPathFromRight = self.dfs(root.right)
        if root.left and root.left.val == root.val:
            longestPathPassingThrough += longestPathFromLeft
            longestPathFromRoot += longestPathFromLeft
        if root.right and root.right.val == root.val:
            longestPathPassingThrough += longestPathFromRight
            longestPathFromRoot = max(longestPathFromRoot, 1 + longestPathFromRight)

        self.ans = max(self.ans, longestPathPassingThrough)
        return longestPathFromRoot
