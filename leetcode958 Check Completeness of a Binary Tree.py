from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        curr = [root]
        traversal = []
        while curr:
            next = []
            for node in curr:
                if node is None:
                    traversal.append(None)
                    continue
                traversal.append(node.val)
                next.append(node.left)
                next.append(node.right)

            curr = next

        while traversal and traversal[-1] is None:
            traversal.pop()
        return None not in traversal

