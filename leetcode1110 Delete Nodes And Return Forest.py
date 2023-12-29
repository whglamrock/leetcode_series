from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(self, root: Optional[TreeNode], toDelete: List[int]) -> List[TreeNode]:
        valsToDelete = set(toDelete)
        forest = {root}
        self.dfs(root, valsToDelete, forest, None)
        return list(forest)

    def dfs(self, node: Optional[TreeNode], valsToDelete: set, forest: set, parent: Optional[TreeNode]):
        leftNode = node.left
        rightNode = node.right
        if node.val in valsToDelete:
            # cut it from its parent
            if parent:
                if parent.left == node:
                    parent.left = None
                else:
                    parent.right = None
            # delete the node from forest
            forest.discard(node)
            # cut it from its children
            node.left, node.right = None, None
            # its children can be potentially root of a new tree
            if leftNode:
                forest.add(leftNode)
            if rightNode:
                forest.add(rightNode)
        if leftNode:
            self.dfs(leftNode, valsToDelete, forest, node)
        if rightNode:
            self.dfs(rightNode, valsToDelete, forest, node)
