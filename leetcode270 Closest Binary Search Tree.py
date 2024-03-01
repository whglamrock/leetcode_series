from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.minDiff = 0
        self.closestVal = 0

    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.closestVal = None
        self.minDiff = 10 ** 10 + 1
        self.dfs(root, target)
        return self.closestVal

    def dfs(self, node: TreeNode, target: float):
        if abs(node.val - target) < self.minDiff:
            self.minDiff = abs(node.val - target)
            self.closestVal = node.val
        elif abs(node.val - target) == self.minDiff:
            if self.closestVal is None or self.closestVal > node.val:
                self.closestVal = node.val

        if node.left:
            self.dfs(node.left, target)
        if node.right:
            self.dfs(node.right, target)
