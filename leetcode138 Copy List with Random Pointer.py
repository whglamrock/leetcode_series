class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# There is an O(1) space solution which modifies the original list
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node = head
        newHead = None
        prev = None
        oldToNew = {}

        while node:
            newNode = Node(node.val)
            if newHead is None:
                newHead = newNode
            if prev:
                prev.next = newNode
            oldToNew[node] = newNode
            prev = newNode
            node = node.next

        node = head
        curr = newHead
        while node:
            if node.random:
                randomNewNode = oldToNew[node.random]
                curr.random = randomNewNode
            node = node.next
            curr = curr.next

        return newHead
