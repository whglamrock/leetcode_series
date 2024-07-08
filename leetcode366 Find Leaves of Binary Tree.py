from typing import Optional, List, Dict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodeToParent, leaves = {}, set()
        self.dfs(root, nodeToParent, leaves)

        ans = []
        todo = leaves
        while todo:
            currLayer = []
            nextTodo = set()
            for node in todo:
                currLayer.append(node.val)
                if node not in nodeToParent:
                    continue

                parent = nodeToParent[node]
                del nodeToParent[node]
                if parent.left == node:
                    parent.left = None
                else:
                    parent.right = None

                if not parent.left and not parent.right:
                    nextTodo.add(parent)

            todo = nextTodo
            ans.append(currLayer)

        return ans

    def dfs(self, node: Optional[TreeNode], nodeToParent: Dict[TreeNode, TreeNode], leaves: set):
        if not node:
            return

        if not node.left and not node.right:
            leaves.add(node)
            return

        if node.left:
            nodeToParent[node.left] = node
            self.dfs(node.left, nodeToParent, leaves)
        if node.right:
            nodeToParent[node.right] = node
            self.dfs(node.right, nodeToParent, leaves)
