from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# serialize it the same way in leetcode. e.g., [1,2,3,null,null,4,5,null,6,null,7]
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''

        serialized = []
        curr = [root]
        while curr:
            next = []
            for node in curr:
                if node is None:
                    serialized.append('null')
                    continue

                serialized.append(str(node.val))
                next.append(node.left)
                next.append(node.right)

            curr = next

        while serialized and serialized[-1] == 'null':
            serialized.pop()

        return ','.join(serialized)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        tokens = deque(data.split(','))
        root = TreeNode(int(tokens.popleft()))

        q = deque([root])
        parent = None
        leftChildConnected = False
        while tokens:
            if not parent:
                parent = q.popleft()

            val = tokens.popleft()
            if val == 'null':
                childNode = None
            else:
                childNode = TreeNode(int(val))
                q.append(childNode)

            if not leftChildConnected:
                parent.left = childNode
                leftChildConnected = True
            else:
                parent.right = childNode
                parent = None
                leftChildConnected = False

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
