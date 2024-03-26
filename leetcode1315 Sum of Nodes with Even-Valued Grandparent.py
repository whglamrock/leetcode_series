from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.ans = 0

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.ans = 0
        self.dfs(root, None, None)
        return self.ans

    def dfs(self, node: TreeNode, parent: Optional[TreeNode], grandParent: Optional[TreeNode]):
        if grandParent and grandParent.val % 2 == 0:
            self.ans += node.val

        if node.left:
            self.dfs(node.left, node, parent)
        if node.right:
            self.dfs(node.right, node, parent)
