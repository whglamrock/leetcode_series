from collections import deque

class Node(object):
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children

# Below is the most practical and bug-free solution you can come up with in real interview. Practice it to remember it.
# Use the level order traversal, with children separated by null:
# e.g., [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        queue = deque([root])
        serialized = []
        while queue:
            node = queue.popleft()
            if node is None:
                serialized.append('null')
                continue
            serialized.append(str(node.val))
            queue.append(None)
            if node.children:
                for child in node.children:
                    queue.append(child)

        return ','.join(serialized)

    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        if data == 'null':
            return None

        tokens = deque(data.split(','))
        root = Node(int(tokens.popleft()))
        queue = deque([root])
        parent = None
        while tokens:
            val = tokens.popleft()
            if val == 'null':
                parent = queue.popleft()
            else:
                node = Node(int(val))
                parent.children.append(node)
                queue.append(node)

        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
