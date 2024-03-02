from typing import Optional

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, root: Optional['Node']) -> Optional['Node']:
        if not root:
            return None

        oldToNew = {}
        # bfs
        todo = {root}
        while todo:
            nextTodo = set()
            for node in todo:
                if node in oldToNew:
                    continue
                newNode = Node(node.val)
                oldToNew[node] = newNode
                for connectedNode in node.neighbors:
                    if connectedNode not in oldToNew:
                        nextTodo.add(connectedNode)
            todo = nextTodo

        for oldNode in oldToNew:
            newNode = oldToNew[oldNode]
            for connectedOld in oldNode.neighbors:
                connectedNewNode = oldToNew[connectedOld]
                newNode.neighbors.append(connectedNewNode)

        return oldToNew[root]
