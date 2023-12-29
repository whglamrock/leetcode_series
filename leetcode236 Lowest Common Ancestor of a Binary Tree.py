
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
        # we only need to look for one of them because p, q are guaranteed both in the tree
        if root == p or root == q:
            return root

        # if p, q both not in leftAns the most inner recursion will hit condition "root.left == None"
        leftAns = self.lowestCommonAncestor(root.left, p, q) if root.left else None
        rightAns = self.lowestCommonAncestor(root.right, p, q) if root.right else None

        if leftAns and rightAns:
            return root
        elif leftAns:
            return leftAns
        else:
            return rightAns
