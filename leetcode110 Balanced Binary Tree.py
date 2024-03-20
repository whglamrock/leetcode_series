from typing import Optional, Tuple

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.heightBalanced = False

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        self.heightBalanced = True
        self.compareSubtrees(root)
        return self.heightBalanced

    def compareSubtrees(self, node: Optional[TreeNode]) -> Tuple[int, int]:
        if not node.left and not node.right:
            return 1, 1

        leftDepth, rightDepth = 1, 1
        if node.left:
            maxDepthOfLeftInLeft, maxDepthOfRightInLeft = self.compareSubtrees(node.left)
            leftDepth += max(maxDepthOfLeftInLeft, maxDepthOfRightInLeft)
        if node.right:
            maxDepthOfLeftInRight, maxDepthOfRightInRight = self.compareSubtrees(node.right)
            rightDepth += max(maxDepthOfLeftInRight, maxDepthOfRightInRight)

        if abs(rightDepth - leftDepth) > 1:
            self.heightBalanced = False

        return leftDepth, rightDepth
