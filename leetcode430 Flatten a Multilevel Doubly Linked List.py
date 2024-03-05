from typing import Tuple

class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        self.flattenList(head)
        return head

    def flattenList(self, node: 'Optional[Node]') -> Tuple['Node', 'Node']:
        if not node.child and not node.next:
            return node, node
        if not node.child:
            nextHead, nextTail = self.flattenList(node.next)
            return node, nextTail
        if not node.next:
            childHead, childTail = self.flattenList(node.child)
            node.next, node.child = childHead, None
            childHead.prev = node
            return node, childTail

        # both child and next are present
        nextNode, childNode = node.next, node.child
        childHead, childTail = self.flattenList(childNode)
        nextHead, nextTail = self.flattenList(nextNode)
        node.next, node.child, childHead.prev = childHead, None, node
        nextNode.prev, childTail.next = childTail, nextNode
        return node, nextTail
