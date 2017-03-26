
# The idea of the __init__ function of class BSTIterator came from 230 Kth Smallest Element in a BST

class TreeNode(object):
    def __init__(self, x):

        self.val = x
        self.left = None
        self.right = None


class BSTIterator(object):
    def __init__(self, root):

        self.stack = []
        self.res = []
        while root or self.stack:
            while root:
                self.stack.append(root)
                root = root.left
            root = self.stack.pop()
            self.res.append(root.val)
            root = root.right
        self.res.reverse()

    def hasNext(self):

        return len(self.res) != 0

    def next(self):

        if len(self.res) != 0:
            ans = self.res.pop()
            return ans
        else:
            return None



# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())