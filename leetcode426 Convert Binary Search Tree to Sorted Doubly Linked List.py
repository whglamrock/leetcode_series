from typing import Tuple

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        head, tail = self.buildHeadAndTail(root)
        head.left, tail.right = tail, head

        return head

    def buildHeadAndTail(self, node: 'Optional[Node]') -> Tuple['Node', 'Node']:
        if not node:
            return None, None
        if not node.left and not node.right:
            return node, node
        if not node.left:
            headOfRight, tailOfRight = self.buildHeadAndTail(node.right)
            node.right, headOfRight.left = headOfRight, node
            return node, tailOfRight
        if not node.right:
            headOfLeft, tailOfLeft = self.buildHeadAndTail(node.left)
            tailOfLeft.right, node.left = node, tailOfLeft
            return headOfLeft, node

        headOfLeft, tailOfLeft = self.buildHeadAndTail(node.left)
        headOfRight, tailOfRight = self.buildHeadAndTail(node.right)
        tailOfLeft.right, node.left = node, tailOfLeft
        node.right, headOfRight.left = headOfRight, node
        return headOfLeft, tailOfRight
