from typing import Optional, Dict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.targetLeaves = set()

    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        self.targetLeaves = set()
        nodeToParent = {}
        self.dfs(root, target, nodeToParent)

        todo = self.targetLeaves
        while todo:
            nextTodo = set()
            for node in todo:
                if node not in nodeToParent:
                    continue

                # cut the leaf from its parent
                parent = nodeToParent[node]
                if parent.left == node:
                    parent.left = None
                else:
                    parent.right = None
                del nodeToParent[node]

                # if the parent node becomes leaf and its value equals to target we need to cut it in next loop
                if not parent.left and not parent.right and parent.val == target:
                    nextTodo.add(parent)

            todo = nextTodo

        return root if root.val != target or (root.left or root.right) else None

    def dfs(self, node: Optional[TreeNode], target: int, nodeToParent: Dict[TreeNode, TreeNode]):
        # leaf node
        if not node.left and not node.right:
            if node.val == target:
                self.targetLeaves.add(node)
            return

        if node.left:
            nodeToParent[node.left] = node
            self.dfs(node.left, target, nodeToParent)
        if node.right:
            nodeToParent[node.right] = node
            self.dfs(node.right, target, nodeToParent)
