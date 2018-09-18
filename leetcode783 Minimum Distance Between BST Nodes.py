
# Definition for a binary tree node.

class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def minDiffInBST(self, root):
        minDiff = 2147483647
        # make sure the prev the smallest and node is second smallest
        node, prev = root, None
        stack = []

        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if prev:
                minDiff = min(minDiff, node.val - prev.val)
            # re-assign prev and node
            prev = node
            node = node.right

        return minDiff