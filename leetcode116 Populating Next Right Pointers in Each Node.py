class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

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
level order traversal approach
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        todo = [root]
        while todo:
            nextTodo = []
            if todo[0].left:
                nextTodo.append(todo[0].left)
                nextTodo.append(todo[0].right)
            for i in range(len(todo) - 1):
                leftNode, rightNode = todo[i], todo[i + 1]
                leftNode.next = rightNode
                if rightNode.left:
                    nextTodo.append(rightNode.left)
                    nextTodo.append(rightNode.right)
            todo = nextTodo
        return root
'''