
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):

        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def invertTree(self, root):
        
        if (not root):
            return
        else:
            temp1 = root.left
            temp2 = root.right
            root.left = temp2
            root.right = temp1
            self.invertTree(root.left)
            self.invertTree(root.right)

        return root



a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)
h = TreeNode(8)
i = TreeNode(9)
j = TreeNode(10)
k = TreeNode(11)
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
d.left = h
d.right = i
f.left = j
g.left = k

Sol = Solution()
root = Sol.invertTree(a)
print root.val
print root.left.val
print root.left.left.val
print root.left.left.right.val

