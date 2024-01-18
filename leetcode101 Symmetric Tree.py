from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.left:
            return not root.right
        return self.areSymmetric(root.left, root.right)

    def areSymmetric(self, leftNode: Optional[TreeNode], rightNode: Optional[TreeNode]) -> bool:
        if not leftNode or not rightNode:
            return leftNode == rightNode
        if leftNode.val != rightNode.val:
            return False

        return self.areSymmetric(leftNode.left, rightNode.right) and self.areSymmetric(leftNode.right, rightNode.left)
