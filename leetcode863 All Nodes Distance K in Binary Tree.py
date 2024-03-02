from typing import List, Dict

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        nodeToParent = {}
        self.dfs(root, nodeToParent)
        # bfs
        todo = {target}
        visited = set()
        for i in range(k):
            nextTodo = set()
            for node in todo:
                visited.add(node)
                if node in nodeToParent and nodeToParent[node] not in visited:
                    nextTodo.add(nodeToParent[node])
                if node.left and node.left not in visited:
                    nextTodo.add(node.left)
                if node.right and node.right not in visited:
                    nextTodo.add(node.right)
            todo = nextTodo

        ans = []
        for node in todo:
            ans.append(node.val)
        return ans

    def dfs(self, root: TreeNode, nodeToParent: Dict[TreeNode, TreeNode]):
        if root.left:
            nodeToParent[root.left] = root
            self.dfs(root.left, nodeToParent)
        if root.right:
            nodeToParent[root.right] = root
            self.dfs(root.right, nodeToParent)
