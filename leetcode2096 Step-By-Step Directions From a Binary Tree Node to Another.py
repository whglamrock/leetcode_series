from typing import Optional, Dict, List

# The optimal solution is find the lowest common ancestor and do dfs upward to get the path for from start & dest
# The time complexity is O(log(N) ^ 2)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.destNode = None
        self.startNode = None

    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        self.startNode, self.destNode = None, None
        nodeToDepth, nodeToParent = {}, {}
        self.dfs(root, startValue, destValue, nodeToDepth, nodeToParent, 0)
        lowestCommonAncestor = self.findLca(self.startNode, self.destNode, nodeToDepth, nodeToParent)
        return self.findPathsToAncestor(self.startNode, lowestCommonAncestor, nodeToParent)[0] + self.findPathsToAncestor(self.destNode, lowestCommonAncestor, nodeToParent)[1]

    def findPathsToAncestor(self, node: Optional[TreeNode], ancestor: Optional[TreeNode], nodeToParent: Dict[TreeNode, TreeNode]) -> List[str]:
        if node == ancestor:
            return ['', '']

        path = []
        reversePaths = []
        while node != ancestor:
            parent = nodeToParent[node]
            path.append('U')
            if parent.left == node:
                reversePaths.append('L')
            else:
                reversePaths.append('R')
            node = parent

        return [''.join(path), ''.join(reversePaths)[::-1]]

    def dfs(self, node: Optional[TreeNode], startValue: int, destValue: int, nodeToDepth: Dict[TreeNode, int],
            nodeToParent: Dict[TreeNode, TreeNode], depth: int):
        nodeToDepth[node] = depth
        if node.val == startValue:
            self.startNode = node
        if node.val == destValue:
            self.destNode = node

        if node.left:
            nodeToParent[node.left] = node
            self.dfs(node.left, startValue, destValue, nodeToDepth, nodeToParent, depth + 1)
        if node.right:
            nodeToParent[node.right] = node
            self.dfs(node.right, startValue, destValue, nodeToDepth, nodeToParent, depth + 1)

    def findLca(self, node1: Optional[TreeNode], node2: Optional[TreeNode], nodeToDepth: Dict[TreeNode, int], nodeToParent: Dict[TreeNode, TreeNode]) -> TreeNode:
        depth1, depth2 = nodeToDepth[node1], nodeToDepth[node2]
        if depth1 < depth2:
            node1, node2 = node2, node1
            depth1, depth2 = depth2, depth1

        while depth1 > depth2:
            node1 = nodeToParent[node1]
            depth1 -= 1

        todo = {node1, node2}
        while len(todo) > 1:
            nextTodo = set()
            for node in todo:
                nextTodo.add(nodeToParent[node])
            todo = nextTodo

        return list(todo)[0]
