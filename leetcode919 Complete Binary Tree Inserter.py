from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class CBTInserter:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        todo = {root}
        lastLevel, secondLastLevel = [], []
        while todo:
            nextTodo = []
            for node in todo:
                if node.left:
                    nextTodo.append(node.left)
                if node.right:
                    nextTodo.append(node.right)
            secondLastLevel = lastLevel
            lastLevel = todo
            todo = nextTodo

        self.queue = deque()
        for node in secondLastLevel:
            if node.left and node.right:
                continue
            self.queue.append(node)
        self.queue.extend(lastLevel)

    def insert(self, val: int) -> int:
        newNode = TreeNode(val)
        node = self.queue.popleft()
        if not node.left:
            node.left = newNode
            self.queue.appendleft(node)
        else:
            node.right = newNode
        self.queue.append(newNode)

        return node.val

    def get_root(self) -> Optional[TreeNode]:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()
