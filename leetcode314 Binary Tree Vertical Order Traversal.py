from collections import defaultdict
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        colToNodes = defaultdict(list)
        # use bfs to do level order traversal
        todo = [(root, 0)]
        while todo:
            nextTodo = []
            for node, col in todo:
                colToNodes[col].append(node.val)
                if node.left:
                    nextTodo.append([node.left, col - 1])
                if node.right:
                    nextTodo.append([node.right, col + 1])
            todo = nextTodo

        minCol, maxCol = min(colToNodes.keys()), max(colToNodes.keys())
        ans = []
        for i in range(minCol, maxCol + 1):
            ans.append(colToNodes[i])
        return ans
