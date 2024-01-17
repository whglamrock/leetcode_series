from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        minOfTree, maxOfTree, isValid = self.traverseBST(root)
        return isValid

    def traverseBST(self, root: Optional[TreeNode]) -> list:
        if not root.left and not root.right:
            return [root.val, root.val, True]

        isValid = True
        minOfTree, maxOfTree = root.val, root.val
        if root.left:
            minOfLeft, maxOfLeft, isLeftTreeValid = self.traverseBST(root.left)
            if not isLeftTreeValid or maxOfLeft >= root.val:
                isValid = False
            minOfTree = min(minOfTree, minOfLeft)
            maxOfTree = max(maxOfTree, maxOfLeft)
        if root.right:
            minOfRight, maxOfRight, isRightTreeValid = self.traverseBST(root.right)
            if not isRightTreeValid or minOfRight <= root.val:
                isValid = False
            minOfTree = min(minOfTree, minOfRight)
            maxOfTree = max(maxOfTree, maxOfRight)

        return [minOfTree, maxOfTree, isValid]
