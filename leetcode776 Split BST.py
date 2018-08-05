
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# remember how the logic is formed
# WUNAO use recursion and goes down the bottom levl

class Solution(object):
    def splitBST(self, root, V):

        if not root:
            return [None, None]

        l_res = self.splitBST(root.left, V)
        r_res = self.splitBST(root.right, V)

        # in this case, the left subTree won't be split because we don't do "root.left = XXX"
        if root.val <= V:
            root.right = r_res[0]
            return [root, r_res[1]]
        # likewise, the right subTree won't be split
        else:
            root.left = l_res[1]
            return [l_res[0], root]
