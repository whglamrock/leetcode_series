
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):

        self.val = x
        self.left = None
        self.right = None



from collections import deque

# it's natural to think of level order traversal idea

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''

        todo = [root]
        ans = []
        while todo:
            nextTodo = []
            for node in todo:
                if node.val != None:
                    ans.append(str(node.val))
                    if node.left:
                        nextTodo.append(node.left)
                    else:
                        nextTodo.append(TreeNode(None))
                    if node.right:
                        nextTodo.append(node.right)
                    else:
                        nextTodo.append(TreeNode(None))
                else:
                    ans.append("null")
            todo = nextTodo

        return ','.join(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        data = deque(data.split(','))
        rootVal = data.popleft()
        root = TreeNode(int(rootVal))
        todo = [root]

        while todo:
            nextTodo = []
            for node in todo:
                leftVal = data.popleft()
                if leftVal != 'null':
                    leftChild = TreeNode(int(leftVal))
                    node.left = leftChild
                    nextTodo.append(leftChild)
                rightVal = data.popleft()
                if rightVal != 'null':
                    rightChild = TreeNode(int(rightVal))
                    node.right = rightChild
                    nextTodo.append(rightChild)
            todo = nextTodo

        return root



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))



'''
# practice:

from collections import deque

class Codec:

    def serialize(self, root):

        if not root:
            return ''
        todo = deque([root])
        ans = []
        while todo:
            next = deque()
            while todo:
                node = todo.popleft()
                if not node:
                    ans.append('N')
                else:
                    ans.append(str(node.val))
                    next.append(node.left)
                    next.append(node.right)
            todo = next

        return ','.join(ans)

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
                    value = data.popleft()
                    if value != 'N':
                        leftchild = TreeNode(int(value))
                        node.left = leftchild
                        next.append(leftchild)
                if data:
                    value = data.popleft()
                    if value != 'N':
                        rightchild = TreeNode(int(value))
                        node.right = rightchild
                        next.append(rightchild)
            todo = next

        return root
'''
