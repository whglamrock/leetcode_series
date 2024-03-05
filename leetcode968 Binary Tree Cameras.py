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
        if not root.left and not root.right:
            return 1

        self.ans = 0
        self.dfs(root, None)
        return self.ans

    # 0 means we put camera on this node; -1 means it's leaf or "similar to leaf"; 1 means it's covered by its children
    def dfs(self, root: Optional[TreeNode], parent: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            if not parent:
                self.ans += 1
                return 0
            return -1

        if root.left and root.right:
            leftValue, rightValue = self.dfs(root.left, root), self.dfs(root.right, root)
            if leftValue == -1 or rightValue == -1:
                self.ans += 1
                return 0
            if leftValue == 0 or rightValue == 0:
                return 1
            # both children are covered, the node needs to be covered by its parent or itself
            if not parent:
                self.ans += 1
                return 0
            return -1
        elif root.left:
            leftValue = self.dfs(root.left, root)
            if leftValue == -1:
                self.ans += 1
                return 0
            if leftValue == 0:
                return 1
            if not parent:
                self.ans += 1
                return 0
            return -1
        else:
            rightValue = self.dfs(root.right, root)
            if rightValue == -1:
                self.ans += 1
                return 0
            if rightValue == 0:
                return 1
            if not parent:
                self.ans += 1
                return 0
            return -1
