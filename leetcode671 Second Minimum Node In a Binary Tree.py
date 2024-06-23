from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.secondMinVal = None
        self.minVal = None

    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.minVal = root.val
        # Node.val <= 2^31 - 1
        self.secondMinVal = 2147483648
        self.traverseTree(root)
        return self.secondMinVal if self.secondMinVal != 2147483648 else -1

    def traverseTree(self, node: Optional[TreeNode]):
        if not node:
            return
        if self.minVal < node.val < self.secondMinVal:
            self.secondMinVal = node.val

        self.traverseTree(node.left)
        self.traverseTree(node.right)
