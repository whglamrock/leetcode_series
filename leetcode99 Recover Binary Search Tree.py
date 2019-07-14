
# Definition for a binary tree node.

class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# idea: https://leetcode.com/problems/recover-binary-search-tree/discuss/32535/No-Fancy-Algorithm-just-Simple-and-Powerful-In-Order-Traversal

class Solution(object):

    def __init__(self):
        # we have to use global variable. directly passing local variables to the
            # traverse method will cause null pointer exception
        self.firstElement, self.secondElement, self.prevElement = None, None, None

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.traverse(root)
        tmp = self.firstElement.val
        self.firstElement.val = self.secondElement.val
        self.secondElement.val = tmp

    # the prevElement is record the last element in the in-order traverse
    def traverse(self, node):

        if not node:
            return

        self.traverse(node.left)

        # when find abnormal; there will be exactly 2 abnormal cases
        if self.prevElement and self.prevElement.val > node.val:
            if not self.firstElement:
                self.firstElement = self.prevElement
            self.secondElement = node

        self.prevElement = node
        self.traverse(node.right)