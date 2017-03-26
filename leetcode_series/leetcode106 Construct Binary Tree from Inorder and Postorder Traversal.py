
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):

        self.val = x
        self.left = None
        self.right = None


# breakthrough point from postorder. Find the position of parent node in inorder list,
# then we can divide and conquer and write recursion.

class Solution(object):
    def buildTree(self, inorder, postorder):

        if not inorder: return

        self.inorder = inorder
        self.postorder = postorder
        self.position = {}
        for i, num in enumerate(inorder):
            self.position[num] = i

        def helper(inlo, inhi, polo, pohi):  # define the work range in list inorder and postorder

            if inlo > inhi:
                return None
            if inlo == inhi:
                newnode = TreeNode(self.inorder[inlo])
                return newnode

            parent = TreeNode(self.postorder[pohi])
            mid = self.position[self.postorder[pohi]]
            # pay attention to the boundary indices!!
            # if any of them got messed up, it could exceed "maximum number of recursion"
            lchild = helper(inlo, mid - 1, polo, polo + mid - inlo - 1)
            rchild = helper(mid + 1, inhi, pohi + mid - inhi, pohi - 1)

            parent.left = lchild
            parent.right = rchild
            return parent

        root = helper(0, len(self.inorder) - 1, 0, len(self.postorder) - 1)
        return root