from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.ans = -2147483648

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.ans

    def dfs(self, root: Optional[TreeNode]):
        if not root.left and not root.right:
            self.ans = max(self.ans, root.val)
            return root.val

        maxLeftSum = self.dfs(root.left) if root.left else 0
        maxRightSum = self.dfs(root.right) if root.right else 0
        # the path goes through the current root but doesn't go to root's parent
        self.ans = max(self.ans, maxLeftSum + root.val + maxRightSum)

        # the path goes up to current root's parent
        maxSumFromRoot = root.val + max(maxLeftSum, maxRightSum, 0)
        self.ans = max(self.ans, maxSumFromRoot)

        return maxSumFromRoot
