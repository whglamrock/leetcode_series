from typing import Optional

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# the idea is search for BST based on p.val, but only assign the successor if we find any node bigger than the p.
# Then if p.val is bigger than the current node, we keep going right (especially if the successor is set previously)
class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        successor = None
        while root:
            if p.val < root.val:
                successor = root
                root = root.left
            else:
                root = root.right

        return successor
