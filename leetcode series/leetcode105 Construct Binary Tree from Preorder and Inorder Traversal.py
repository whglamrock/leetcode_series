# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# reuse the solution for lc106.
class Solution(object):
    def buildTree(self, preorder, inorder):

        if not inorder: return

        self.inorder = inorder
        self.preorder = preorder
        self.position = {}
        for i, num in enumerate(inorder):
            self.position[num] = i

        def helper(inlo, inhi, prelo, prehi):  # define the work range in list inorder and preorder

            if inlo > inhi:
                return None
            if inlo == inhi:
                newnode = TreeNode(self.inorder[inlo])
                return newnode

            parent = TreeNode(self.preorder[prelo])
            mid = self.position[self.preorder[prelo]]
            # pay attention to the boundary indices!!
            # if any of them got messed up, it could exceed "maximum number of recursion"
            lchild = helper(inlo, mid - 1, prelo + 1, prelo + mid - inlo)
            rchild = helper(mid + 1, inhi, prehi + mid + 1 - inhi, prehi)

            parent.left = lchild
            parent.right = rchild
            return parent

        root = helper(0, len(self.inorder) - 1, 0, len(self.preorder) - 1)
        return root