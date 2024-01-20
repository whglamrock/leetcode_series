from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        if not root:
            return [None, None]
        if root.val == target:
            rootOfBigger = root.right
            root.right = None
            return [root, rootOfBigger]
        elif root.val < target:
            rootOfSmallerInRightSubtree, rootOfBiggerInRightSubtree = self.splitBST(root.right, target)
            root.right = rootOfSmallerInRightSubtree
            return [root, rootOfBiggerInRightSubtree]
        else:
            rootOfSmallerInLeftSubtree, rootOfBiggerInLeftSubtree = self.splitBST(root.left, target)
            root.left = rootOfBiggerInLeftSubtree
            return [rootOfSmallerInLeftSubtree, root]
