from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.nodeQ = None
        self.nodeP = None
        self.nodeToParent = {}

    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        self.nodeToParent = {}
        self.nodeP, self.nodeQ = None, None
        self.dfs(root, p, q)

        # bfs from p to q
        todo = {self.nodeP}
        distance = 0
        visited = set()
        while todo:
            nextTodo = set()
            for node in todo:
                if node == self.nodeQ:
                    return distance
                visited.add(node)
                if node.left and node.left not in visited:
                    nextTodo.add(node.left)
                if node.right and node.right not in visited:
                    nextTodo.add(node.right)
                if node in self.nodeToParent and self.nodeToParent[node] not in visited:
                    nextTodo.add(self.nodeToParent[node])
            todo = nextTodo
            distance += 1

        return -1

    def dfs(self, node: Optional[TreeNode], p: int, q: int):
        if node.val == p:
            self.nodeP = node
        if node.val == q:
            self.nodeQ = node
        if node.left:
            self.nodeToParent[node.left] = node
            self.dfs(node.left, p, q)
        if node.right:
            self.nodeToParent[node.right] = node
            self.dfs(node.right, p, q)
