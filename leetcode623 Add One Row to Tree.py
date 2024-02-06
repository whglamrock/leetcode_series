from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root)

        currLevel = [root]
        for i in range(depth - 2):
            nextLevel = []
            for node in currLevel:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            currLevel = nextLevel

        for node in currLevel:
            newLeft, newRight = TreeNode(val), TreeNode(val)
            newLeft.left, newRight.right = node.left, node.right
            node.left, node.right = newLeft, newRight

        return root
