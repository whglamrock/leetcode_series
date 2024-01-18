from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        todo = [root]
        while todo:
            nextTodo = []
            level = []
            for node in todo:
                level.append(node.val)
                if node.left:
                    nextTodo.append(node.left)
                if node.right:
                    nextTodo.append(node.right)
            ans.append(level)
            todo = nextTodo
        return ans
