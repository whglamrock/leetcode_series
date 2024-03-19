from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        leftChild, rightChild = root.left, root.right
        self.invertTree(leftChild)
        self.invertTree(rightChild)
        root.left, root.right = rightChild, leftChild
        return root
