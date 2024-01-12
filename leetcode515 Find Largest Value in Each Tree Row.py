from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ans = []
        todo = [root]
        while todo:
            nextTodo = []
            maxOfRow = -2147483648
            for node in todo:
                maxOfRow = max(maxOfRow, node.val)
                if node.left:
                    nextTodo.append(node.left)
                if node.right:
                    nextTodo.append(node.right)
            ans.append(maxOfRow)
            todo = nextTodo

        return ans
