from typing import Optional

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        if not node:
            return None
        if not node.right and not node.parent:
            return None

        if node.right:
            curr = node.right
            while curr.left:
                curr = curr.left
            return curr
        else:
            curr = node
            while curr.parent and curr.parent.right == curr:
                curr = curr.parent
            return curr.parent if (curr and curr.parent) else None
