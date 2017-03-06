# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if (not root):
            return root

        if root == p or root == q:
            return root

        leftans = self.lowestCommonAncestor(root.left, p, q)
        rightans = self.lowestCommonAncestor(root.right, p, q)
        if leftans and rightans:
            return root
        elif leftans:
            return leftans
        else:
            return rightans