class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        curr = [root]
        while curr:
            next = []
            for i in range(len(curr)):
                currNode = curr[i]
                if i < len(curr) - 1:
                    nextNode = curr[i + 1]
                    currNode.next = nextNode

                if currNode.left:
                    next.append(currNode.left)
                if currNode.right:
                    next.append(currNode.right)
            curr = next

        return root
