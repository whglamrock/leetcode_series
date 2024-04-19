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

    # if it's leaf, return -1; if it's covered by its child return 0; if we put a camera on it, return 1
    def dfs(self, node: Optional[TreeNode], parent: Optional[TreeNode]) -> int:
        # leaf
        if not node.left and not node.right:
            return -1
        elif node.left and node.right:
            leftChild = self.dfs(node.left, node)
            rightChild = self.dfs(node.right, node)
            if leftChild == -1 or rightChild == -1:
                self.ans += 1
                return 1
            if leftChild == 1 or rightChild == 1:
                return 0
        elif node.left:
            leftChild = self.dfs(node.left, node)
            if leftChild == -1:
                self.ans += 1
                return 1
            if leftChild == 1:
                return 0
        else:
            rightChild = self.dfs(node.right, node)
            if rightChild == -1:
                self.ans += 1
                return 1
            if rightChild == 1:
                return 0

        # both children are covered by grandchildren, we need to rely on parent
        # to decide whether we put a camera on it
        if not parent:
            self.ans += 1
            return 1
        # leaf "like"
        return -1
