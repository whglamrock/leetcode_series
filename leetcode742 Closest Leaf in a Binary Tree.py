from typing import Optional, Dict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.targetNode = None

    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        self.targetNode = None
        leafNodes = set()
        nodeToParent = {}
        self.dfs(root, nodeToParent, leafNodes, k)
        if self.targetNode is None:
            return -1

        todo = {self.targetNode}
        visited = set()
        while todo:
            nextTodo = set()
            for node in todo:
                if node in leafNodes:
                    return node.val
                if node in visited:
                    continue
                visited.add(node)
                if node.left and node.left not in visited:
                    nextTodo.add(node.left)
                if node.right and node.right not in visited:
                    nextTodo.add(node.right)
                if node in nodeToParent and nodeToParent[node] not in visited:
                    nextTodo.add(nodeToParent[node])
            todo = nextTodo

        return -1

    def dfs(self, node: Optional[TreeNode], nodeToParent: Dict[TreeNode, TreeNode], leafNodes: set, k: int):
        if node.val == k:
            self.targetNode = node

        # leaf node
        if not node.left and not node.right:
            leafNodes.add(node)
            return

        if node.left:
            nodeToParent[node.left] = node
            self.dfs(node.left, nodeToParent, leafNodes, k)
        if node.right:
            nodeToParent[node.right] = node
            self.dfs(node.right, nodeToParent, leafNodes, k)
