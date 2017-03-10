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
        def helper(node, curmin, curmax):
            if curmax != None and node.val >= curmax:
                self.flag = False
            if curmin != None and node.val <= curmin:
                self.flag = False
            if node.left:
                if curmax == None:
                    helper(node.left, curmin, node.val)
                else:
                    helper(node.left, curmin, min(curmax, node.val))
            if node.right:
                if curmin == None:
                    helper(node.right, node.val, curmax)
                else:
                    helper(node.right, max(curmin, node.val), curmax)

        helper(root, None, None)
        return self.flag

