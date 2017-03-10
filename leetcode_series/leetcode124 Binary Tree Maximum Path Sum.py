# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):

        self.val = x
        self.left = None
        self.right = None


# the idea for maxPathDown function is the input node is highest node in path

class Solution(object):
    def maxPathSum(self, root):

        self.maxSum = -2147483648

        def maxPathDown(node):

            if not node: return 0
            leftmax = max(0, maxPathDown(node.left))
            rightmax = max(0, maxPathDown(node.right))
            self.maxSum = max(self.maxSum, node.val + leftmax + rightmax)

            return max(leftmax, rightmax) + node.val

        maxPathDown(root)
        return self.maxSum


