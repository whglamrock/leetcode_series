from collections import defaultdict
from typing import Set, Dict, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        nodeToParent = {}
        self.buildNodeToParent(root, nodeToParent)
        depthToNodes = defaultdict(set)
        self.buildDepthToNodes(root, depthToNodes, 0)
        maxDepth = max(depthToNodes.keys())
        return self.findLowestCommonAncestor(depthToNodes[maxDepth], nodeToParent)

    def buildDepthToNodes(self, node: TreeNode, depthToNodes: Dict[int, Set[TreeNode]], depth: int):
        depthToNodes[depth].add(node)
        if node.left:
            self.buildDepthToNodes(node.left, depthToNodes, depth + 1)
        if node.right:
            self.buildDepthToNodes(node.right, depthToNodes, depth + 1)

    def buildNodeToParent(self, node: TreeNode, nodeToParent: Dict[TreeNode, TreeNode]):
        if not node or (not node.left and not node.right):
            return
        if node.left:
            nodeToParent[node.left] = node
            self.buildNodeToParent(node.left, nodeToParent)
        if node.right:
            nodeToParent[node.right] = node
            self.buildNodeToParent(node.right, nodeToParent)

    def findLowestCommonAncestor(self, nodes: Set[TreeNode], nodeToParent: Dict[TreeNode, TreeNode]) -> TreeNode:
        todo = nodes
        while todo:
            if len(todo) == 1:
                return list(todo)[0]
            nextTodo = set()
            for node in todo:
                nextTodo.add(nodeToParent[node])
            todo = nextTodo
