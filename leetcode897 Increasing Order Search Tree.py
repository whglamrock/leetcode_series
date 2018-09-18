
# Definition for a binary tree node.

class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def increasingBST(self, root):

        # in order traversal
        def inOrder(root, traversal):
            if root.left:
                inOrder(root.left, traversal)
            traversal.append(root)
            if root.right:
                inOrder(root.right, traversal)
            return traversal

        traversal = inOrder(root, [])
        for i in xrange(len(traversal) - 1):
            traversal[i].left = None
            traversal[i].right = traversal[i + 1]
        traversal[-1].left, traversal[-1].right = None, None

        return traversal[0]



'''
# P.S., the problem description didn't tell it is a BST...lol
class Solution(object):

    def increasingBST(self, root):
        traversal = []
        node, prev = root, None
        stack = []

        # remember how to do in-order
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            traversal.append(node)
            node = node.right

        for i in xrange(len(traversal) - 1):
            traversal[i].left = None
            traversal[i].right = traversal[i + 1]
        traversal[-1].left, traversal[-1].right = None, None

        return traversal[0]
'''