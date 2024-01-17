from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''

        # level order traversal
        todo = [root]
        levelOrderTraversals = []
        while todo:
            nextTodo = []
            for node in todo:
                if node is None:
                    levelOrderTraversals.append(None)
                    continue
                levelOrderTraversals.append(node.val)
                if node.left:
                    nextTodo.append(node.left)
                else:
                    nextTodo.append(None)
                if node.right:
                    nextTodo.append(node.right)
                else:
                    nextTodo.append(None)
            todo = nextTodo
        while levelOrderTraversals and levelOrderTraversals[-1] is None:
            levelOrderTraversals.pop()
        ans = []
        for val in levelOrderTraversals:
            if val is None:
                ans.append('null')
            else:
                ans.append(str(val))
        return ','.join(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        data = deque(data.split(','))
        root = TreeNode(int(data.popleft()))
        todo = [root]
        while todo:
            nextTodo = []
            for node in todo:
                # to deal with leaf node
                if not data:
                    break
                nextVal = data.popleft()
                if nextVal != 'null':
                    leftNode = TreeNode(int(nextVal))
                    node.left = leftNode
                    nextTodo.append(leftNode)
                # to deal with leaf node
                if not data:
                    break
                nextVal = data.popleft()
                if nextVal != 'null':
                    rightNode = TreeNode(int(nextVal))
                    node.right = rightNode
                    nextTodo.append(rightNode)
            todo = nextTodo

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
