from copy import deepcopy
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.ans = []

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        self.ans = []
        self.dfs(root, targetSum, 0, [])
        return self.ans

    def dfs(self, node: Optional[TreeNode], targetSum: int, currSum: int, currVals: List[int]):
        currVals.append(node.val)
        currSum += node.val
        if currSum == targetSum and (not node.left and not node.right):
            self.ans.append(deepcopy(currVals))

        if node.left:
            self.dfs(node.left, targetSum, currSum, deepcopy(currVals))
        if node.right:
            self.dfs(node.right, targetSum, currSum, deepcopy(currVals))
