# idea from: https://discuss.leetcode.com/topic/17971/my-python-solution-in-o-lgn-lgn-time/2
# divide and conquer. O((logN)^2) solution, n is the number of treeNodes.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def getdepth(self, node):

        if (not node):
            return 0
        else:
            return 1 + self.getdepth(node.left)

    def countNodes(self, root):

        if (not root):
            return 0

        leftdepth = self.getdepth(root.left)
        rightdepth = self.getdepth(root.right)

        if leftdepth == rightdepth:    # left subtree is a full binary
            return pow(2, leftdepth) + self.countNodes(root.right)
        else:    # right subtree is a full binary
            return pow(2, rightdepth) + self.countNodes(root.left)

