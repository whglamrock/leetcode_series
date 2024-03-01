from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ans = []
        # level order traversal
        todo = [root]
        while todo:
            nextTodo = []
            ans.append(todo[-1].val)
            for node in todo:
                if node.left:
                    nextTodo.append(node.left)
                if node.right:
                    nextTodo.append(node.right)
            todo = nextTodo

        return ans
