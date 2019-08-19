
# Definition for a Node.

class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children



from collections import deque

# serializing a binary tree is way easier because we know for sure each node has no more than 2 children

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        if not root:
            return ''

        traversal = []
        self.serializeHelper(root, traversal)
        return ','.join(traversal)

    # for tree defined in problem description, the pre-order traversal will look
        # like: 1,3,3,2,5,0,6,0,2,0,4,0
    def serializeHelper(self, root, traversal):
        if not root:
            return
        traversal.append(str(root.val))
        traversal.append(str(len(root.children)))
        for child in root.children:
            self.serializeHelper(child, traversal)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        if not data:
            return None

        traversal = deque(data.split(','))
        return self.deserializeHelper(traversal)

    # traversal is a deque
    def deserializeHelper(self, traversal):
        val = int(traversal.popleft())
        size = int(traversal.popleft())
        root = Node(val, [])
        for i in xrange(size):
            root.children.append(self.deserializeHelper(traversal))

        return root



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))