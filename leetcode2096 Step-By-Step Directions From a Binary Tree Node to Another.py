from typing import Optional, Dict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.startNode = None

    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        self.startNode = None
        nodeToParent = {}
        self.dfs(root, startValue, nodeToParent)

        todo = [[self.startNode, '']]
        visited = set()
        while todo:
            nextTodo = []
            for node, path in todo:
                visited.add(node)
                if node.val == destValue:
                    return path
                if node.left and node.left not in visited:
                    nextTodo.append([node.left, path + 'L'])
                if node.right and node.right not in visited:
                    nextTodo.append([node.right, path + 'R'])
                if node in nodeToParent and nodeToParent[node] not in visited:
                    nextTodo.append([nodeToParent[node], path + 'U'])
            todo = nextTodo

        return ''

    def dfs(self, node: Optional[TreeNode], startValue: int, nodeToParent: Dict[TreeNode, TreeNode]):
        if node.val == startValue:
            self.startNode = node

        if node.left:
            nodeToParent[node.left] = node
            self.dfs(node.left, startValue, nodeToParent)
        if node.right:
            nodeToParent[node.right] = node
            self.dfs(node.right, startValue, nodeToParent)
