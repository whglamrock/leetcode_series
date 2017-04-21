
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):

        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root):

        if not root:
            return True

        self.flag = True
        def helper(node, lo, hi):
            if not lo < node.val < hi:
                self.flag = False
                return False    # return immediately to prune useless recursions
            if node.left:
                if helper(node.left, lo, min(node.val, hi)) == False:
                    self.flag = False
                    return False    # return immediately to prune useless recursions
            if node.right:
                if helper(node.right, max(node.val, lo), hi) == False:
                    self.flag = False
                    return False    # return immediately to prune useless recursions
            return True    # this return is for the above two sub if statement

        helper(root, -2147483649, 2147483648)   # the initial bounds are set to the min/max int -/+1
        return self.flag

