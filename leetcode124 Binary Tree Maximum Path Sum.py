
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# the key is to use dfs to get the max path sum that ends with node i

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxSum = -2147483648
        # each node stores the biggest sum that ends with it
        self.dfs(root)
        return self.maxSum

    def dfs(self, node):
        maxToNode = node.val
        maxLeft = 0
        maxRight = 0

        if node.left:
            maxLeft = self.dfs(node.left)
        if node.right:
            maxRight = self.dfs(node.right)

        maxToNode = max(maxToNode,
                        node.val + maxLeft,
                        node.val + maxRight)

        self.maxSum = max(self.maxSum,
                          node.val,
                          maxLeft + node.val,
                          maxRight + node.val,
                          maxLeft + maxRight + node.val)

        return maxToNode


