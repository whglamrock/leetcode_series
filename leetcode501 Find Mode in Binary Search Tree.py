
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):

        self.val = x
        self.left = None
        self.right = None


# standard Morris Inorder Traversal solution
# Abour Morris Inorder: https://www.youtube.com/watch?v=wGXB9OWhPTg

class Solution(object):

    def findMode(self, root):

        if not root: return []
        self.prev, self.count, self.maximum, self.res = None, 0, 0, []

        def updatecount(val):

            if val == self.prev:
                self.count += 1
            # val != prev
            else:
                self.count = 1
                self.prev = val
            if self.count > self.maximum:
                self.res = [self.prev]
                self.maximum = self.count
            elif self.count == self.maximum:
                self.res.append(self.prev)

        # go through the test case [10,5,30,-2,6,null,40,null,2,null,8,null,null,-1]
        #   to understand the workflow
        while root:
            if not root.left:
                updatecount(root.val)
                root = root.right
            else:
                pred = root.left
                # find the predecessor of root in inorder traverse
                while pred.right and pred.right is not root:
                    pred = pred.right
                # means the pred doesn't have a manually created "virtual" link
                if not pred.right:
                    # create a "virtual" link so we can reference this next descendent later
                    pred.right = root
                    root = root.left
                # means we have already visited the left subtree of current root
                #   so we need to visit the right subtree and delete the "virtual" link
                else:
                    pred.right = None
                    updatecount(root.val)
                    root = root.right

        return self.res



'''
# "So called" O(1) solution using recursion
# idea is inorderly flatten the BST

class Solution(object):
    def findMode(self, root):

        if not root: return []

        self.prev = None
        self.count = 0
        self.maximum = 0
        self.res = []

        def updatecount(val):

            if val == self.prev:
                self.count += 1
            # val != prev
            else:
                self.count = 1
                self.prev = val
            if self.count > self.maximum:
                self.res = [self.prev]
                self.maximum = self.count
            elif self.count == self.maximum:
                self.res.append(self.prev)

        # flatten the BST, strictly not O(1) because of the recursion stack,
        #   but can be considered O(1) due to the problem description
        def flatten(root):

            if not root:
                return

            leftroot = flatten(root.left) if root.left else None
            rightroot = flatten(root.right) if root.right else None
            root.right = rightroot

            if not leftroot:
                return root
            pred = leftroot
            while pred and pred.right:
                pred = pred.right
            pred.right = root

            return leftroot

        root = flatten(root)
        while root:
            updatecount(root.val)
            root = root.right

        return self.res
'''