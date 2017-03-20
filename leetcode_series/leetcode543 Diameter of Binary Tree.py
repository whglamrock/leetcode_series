# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# idea: the length of the path is the leftdepth + rightdepth + 1,
#   so set a global variable and traverse the tree

class Solution(object):
    def diameterOfBinaryTree(self, root):

        if not root:
            return 0

        self.ans = 0

        def maxDepth(node):
            if not node:
                return 0
            leftdepth = maxDepth(node.left)
            rightdepth = maxDepth(node.right)
            self.ans = max(self.ans, leftdepth + 1 + rightdepth)
            return max(leftdepth, rightdepth) + 1

        maxDepth(root)
        return self.ans - 1