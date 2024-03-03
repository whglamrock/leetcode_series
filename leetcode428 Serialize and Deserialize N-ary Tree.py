from collections import deque

class Node(object):
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children

# each level is separated by a '|', after a set of node values we add a '/' so all values in between
# belong to the corresponding parent in the above level
class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        levels = []
        todo = [root]
        while todo:
            level = []
            nextTodo = []
            for node in todo:
                if not node:
                    level.append('None')
                    continue
                elif node == '/':
                    level.append('/')
                    continue

                level.append(str(node.val))
                if not node.children:
                    nextTodo.append(None)
                else:
                    nextTodo.extend(node.children)
                nextTodo.append('/')
            # don't rstrip '/' because we need it in deserialization,
            # especially when we add the second level as root's children
            levels.append(','.join(level).strip(','))
            todo = nextTodo

        return '|'.join(levels)

    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        levelStrs = deque(data.split('|'))
        firstValue = levelStrs.popleft()
        if firstValue == 'None':
            return None
        root = Node(int(firstValue))

        prev = [root]
        while levelStrs:
            levelStr = levelStrs.popleft()
            valueStrs = levelStr.split(',')
            # store the nodes created in this level so in next level they can be referenced as parents
            curr = []
            # store the nodes created in this level belonging to a certain parent in previous level
            currChildren = []
            prevLevelIndex = 0
            i = 0

            while i < len(valueStrs):
                if valueStrs[i] == '/':
                    if currChildren:
                        prev[prevLevelIndex].children = currChildren
                    currChildren = []
                    prevLevelIndex += 1
                elif valueStrs[i] == 'None':
                    i += 1
                    continue
                else:
                    node = Node(int(valueStrs[i]))
                    curr.append(node)
                    currChildren.append(node)
                i += 1
            prev = curr

        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
