
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):

        self.val = x
        self.left = None
        self.right = None


# the question title should be modified to "height-balanced BST".

class Solution(object):
    def isBalanced(self, root):

        if not root:
            return True

        self.flag = True
        def helper(node, depth):
            if (not node.left) and (not node.right):
                return depth
            leftdepth, rightdepth = depth, depth
            if node.left:
                leftdepth = helper(node.left, depth + 1)
            if node.right:
                rightdepth = helper(node.right, depth + 1)
            #print node.val, leftdepth, rightdepth
            if abs(leftdepth - rightdepth) > 1:
                self.flag = False
            return max(leftdepth, rightdepth)
        helper(root, 1)

        return self.flag

