from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# There are so many stupid test cases, so you have to remember the below approach.
# Idea coming from: https://leetcode.com/problems/binary-tree-cameras/solutions/211180/java-c-python-greedy-dfs/
class Solution:
    def __init__(self):
        self.ans = 0

    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.ans = 0
        # in this case root is considered a "leaf" or all its children are covered
        if self.dfs(root) == 0:
            return self.ans + 1
        else:
            return self.ans

    def dfs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 2

        left, right = self.dfs(root.left), self.dfs(root.right)
        # at least one of the children is leaf
        if left == 0 or right == 0:
            self.ans += 1
            return 1
        # at least one of the children has a camera
        if left == 1 or right == 1:
            return 2

        # both children are returning 2 so it's a leaf
        return 0
