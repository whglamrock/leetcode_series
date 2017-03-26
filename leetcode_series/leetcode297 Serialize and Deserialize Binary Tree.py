
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):

        self.val = x
        self.left = None
        self.right = None


# the idea is level order traversal

from collections import deque
class Codec:

    def serialize(self, root):

        if not root:
            return ''

        ans = []
        todo = deque([root])
        while todo:
            next = deque()
            while todo:
                node = todo.popleft()
                if not node:
                    ans.append('N')
                    continue
                ans.append(str(node.val))
                next.append(node.left)
                next.append(node.right)
            todo = next
        return ','.join(ans)

    # the key is to remember to check if the queue is empty
    def deserialize(self, data):

        if not data:
            return None

        data = deque(data.split(','))
        root = TreeNode(int(data.popleft()))
        todo = deque([root])

        while todo:
            next = deque()
            while todo:
                node = todo.popleft()
                if data:
                    val = data.popleft()
                    if val != 'N':
                        leftchild = TreeNode(int(val))
                        node.left = leftchild
                        next.append(leftchild)
                if data:
                    val = data.popleft()
                    if val != 'N':
                        rightchild = TreeNode(int(val))
                        node.right = rightchild
                        next.append(rightchild)
            todo = next

        return root



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
