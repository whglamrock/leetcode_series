from typing import Optional, Dict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 0

        nodeToParent = {}
        valToNode = {}
        self.traverseTree(root, nodeToParent, valToNode)

        startNode = valToNode[start]
        todo = {startNode}
        visited = set()
        minutes = 0
        while todo:
            nextTodo = set()
            for node in todo:
                visited.add(node)
                if node.left and node.left not in visited:
                    nextTodo.add(node.left)
                if node.right and node.right not in visited:
                    nextTodo.add(node.right)
                if node in nodeToParent and nodeToParent[node] not in visited:
                    nextTodo.add(nodeToParent[node])
            todo = nextTodo
            if todo:
                minutes += 1

        return minutes

    def traverseTree(self, root: Optional[TreeNode], nodeToParent: Dict[TreeNode, TreeNode], valToNode: Dict[int, TreeNode]):
        if not root:
            return
        valToNode[root.val] = root
        if not root.left and not root.right:
            return

        if root.left:
            nodeToParent[root.left] = root
            self.traverseTree(root.left, nodeToParent, valToNode)
        if root.right:
            nodeToParent[root.right] = root
            self.traverseTree(root.right, nodeToParent, valToNode)
