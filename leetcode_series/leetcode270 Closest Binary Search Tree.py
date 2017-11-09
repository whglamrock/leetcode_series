
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):

        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def closestValue(self, root, target):

        self.ans = root.val

        if (not root):
            return

        def fku(node, target):
            if (not node):
                return
            if abs(node.val - target) < abs(self.ans - target):
                self.ans = node.val
            fku(node.left, target)
            fku(node.right, target)

        fku(root, target)

        return self.ans



a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)
h = TreeNode(10)
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
d.left = h

Sol = Solution()
print Sol.closestValue(a, 8)


