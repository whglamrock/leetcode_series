class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

# level order traversal approach that's easier to remember
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        curr = [root]
        while curr:
            next = []
            for node in curr:
                if node.left:
                    node.left.next = node.right
                    next.append(node.left)
                if node.right:
                    if node.next:
                        node.right.next = node.next.left
                    next.append(node.right)
            curr = next

        return root


'''
# move the root solution
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        ans = root
        while root:
            curr = root
            while curr:
                if curr.left:
                    curr.left.next = curr.right
                if curr.next and curr.right:
                    curr.right.next = curr.next.left
                curr = curr.next
            root = root.left
        return ans
'''