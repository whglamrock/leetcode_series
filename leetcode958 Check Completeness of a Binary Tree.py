from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        vals = self.traverseTree(root)
        return None not in vals

    def traverseTree(self, node: Optional[TreeNode]):
        todo = [node]
        vals = []
        while todo:
            nextTodo = []
            for node in todo:
                if node is None:
                    vals.append(None)
                    continue
                else:
                    vals.append(node.val)
                    nextTodo.append(node.left)
                    nextTodo.append(node.right)
            todo = nextTodo

        while vals and vals[-1] is None:
            vals.pop()

        return vals

