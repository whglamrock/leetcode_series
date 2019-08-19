
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if not root:
            return None

        if root.left:
            if root.val < L:
                root.left = None
            else:
                root.left = self.trimBST(root.left, L, R)

        if root.right:
            if root.val > R:
                root.right = None
            else:
                root.right = self.trimBST(root.right, L, R)

        if L <= root.val <= R:
            return root

        # at least one of them will be None
        leftChild, rightChild = root.left, root.right
        return leftChild if leftChild else rightChild







