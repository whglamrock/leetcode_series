
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):

        self.val = x
        self.left = None
        self.right = None



# writing a arbitary O(N) solution is easy, but we need to find optimization to avoid unnecessary traversal

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        height = self.get_height(root)
        return height != -1

    # dfs
    def get_height(self, root):
        if not root:
            return 0
        left = self.get_height(root.left)
        right = self.get_height(root.right)

        if left == -1 or right == -1:
            # this would prevent further dfs
            return -1
        if abs(left - right) > 1:
            return -1
        return max(left, right) + 1

