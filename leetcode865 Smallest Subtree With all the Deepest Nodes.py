from collections import defaultdict
from typing import Set, Dict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        nodeToParent = {}
        depthToNodes = defaultdict(set)
        self.dfs(root, depthToNodes, nodeToParent, 0)
        maxDepth = max(depthToNodes.keys())
        return self.findLowestCommonAncestor(depthToNodes[maxDepth], nodeToParent)

    def dfs(self, node: TreeNode, depthToNodes: Dict[int, Set[TreeNode]], nodeToParent: Dict[TreeNode, TreeNode], depth: int):
        depthToNodes[depth].add(node)
        if node.left:
            nodeToParent[node.left] = node
            self.dfs(node.left, depthToNodes, nodeToParent, depth + 1)
        if node.right:
            nodeToParent[node.right] = node
            self.dfs(node.right, depthToNodes, nodeToParent, depth + 1)

    def findLowestCommonAncestor(self, nodes: Set[TreeNode], nodeToParent: Dict[TreeNode, TreeNode]) -> TreeNode:
        todo = nodes
        while len(todo) > 1:
            nextTodo = set()
            for node in todo:
                nextTodo.add(nodeToParent[node])
            todo = nextTodo

        return list(todo)[0]
