from typing import Optional, Tuple

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.flattenTree(root)

    def flattenTree(self, root: Optional[TreeNode]) -> Tuple[TreeNode, TreeNode]:
        if not root.left and not root.right:
            return root, root
        elif root.left and root.right:
            headOfLeftSubtree, tailOfLeftSubtree = self.flattenTree(root.left)
            headOfRightSubtree, tailOfRightSubtree = self.flattenTree(root.right)
            root.left, root.right = None, headOfLeftSubtree
            tailOfLeftSubtree.right = headOfRightSubtree
            return root, tailOfRightSubtree
        elif root.left:
            headOfLeftSubtree, tailOfLeftSubtree = self.flattenTree(root.left)
            root.left, root.right = None, headOfLeftSubtree
            return root, tailOfLeftSubtree
        else:
            headOfRightSubtree, tailOfRightSubtree = self.flattenTree(root.right)
            root.left, root.right = None, headOfRightSubtree
            return root, tailOfRightSubtree
