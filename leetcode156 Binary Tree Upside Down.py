from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or not root.left:
            return root

        leftChild, rightChild = root.left, root.right
        root.left, root.right = None, None
        newRoot = self.upsideDownBinaryTree(leftChild)
        leftChild.right = root
        leftChild.left = rightChild
        return newRoot
