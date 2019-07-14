
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):

        self.val = x
        self.left = None
        self.right = None


# idea: inorder traverse, find the min Diff of two consecutive nodes

class Solution(object):
    def getMinimumDifference(self, root):

        stack = []
        minDiff = 2147483647
        node = root
        prev = None

        # the condition for while loop is very important
        #   cuz it's possible that node is None but stack is not
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if prev:
                minDiff = min(minDiff, node.val - prev.val)
            prev = node
            node = node.right

        return minDiff