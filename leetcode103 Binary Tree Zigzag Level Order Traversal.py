from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = []
        todo = [root]
        isReverse = True
        while todo:
            nextTodo = []
            level = []
            for node in todo:
                level.append(node.val)
                if node.left:
                    nextTodo.append(node.left)
                if node.right:
                    nextTodo.append(node.right)
            todo = nextTodo
            if isReverse:
                ans.append(level)
            else:
                ans.append(level[::-1])
            isReverse = not isReverse

        return ans
