
# The idea of the __init__ function of class BSTIterator came from 230 Kth Smallest Element in a BST

class TreeNode(object):
    def __init__(self, x):

        self.val = x
        self.left = None
        self.right = None


class BSTIterator(object):
    def __init__(self, root):

        self.traversal = []
        stack = []

        # remember the classic way of iterative in-order traversal
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            self.traversal.append(root.val)
            root = root.right
        self.traversal.reverse()

    def hasNext(self):

        return len(self.traversal) != 0

    def next(self):

        return self.traversal.pop()  # no need to check if traversal empty, see how iterator is called



# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())



'''
# recursive way of traversal

class BSTIterator(object):
    def __init__(self, root):

        self.traversal = []
        def helper(root):
            if root and root.left:
                helper(root.left)
            if root: self.traversal.append(root.val)
            if root and root.right:
                helper(root.right)
        helper(root)
        self.traversal.reverse()

    def hasNext(self):

        return len(self.traversal) != 0

    def next(self):

        return self.traversal.pop()
'''