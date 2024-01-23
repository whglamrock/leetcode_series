from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.maxLen = 0

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.maxLen = 0
        self.dfs(root.left, 0, 'left')
        self.dfs(root.right, 0, 'right')
        return self.maxLen

    # the currLen is actually the length till the node one level above,
    # so we need to update the maxLen even if the node is None
    def dfs(self, node: Optional[TreeNode], currLen: int, prevDirection: str):
        self.maxLen = max(self.maxLen, currLen)
        if not node:
            return

        if prevDirection == 'right':
            self.dfs(node.left, currLen + 1, 'left')
            self.dfs(node.right, 0, 'right')
        else:
            self.dfs(node.left, 0, 'left')
            self.dfs(node.right, currLen + 1, 'right')