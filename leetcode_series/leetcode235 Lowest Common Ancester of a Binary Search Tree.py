
'''
The algorithm idea came from: https://leetcode.com/discuss/44959/3-lines-with-o-1-space-1-liners-alternatives
As for the trick of tuple: try: c = (2,3)[4>3] and c = (2,3)[2>3]
'''

class TreeNode(object):
    def __init__(self, x):

        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):

        # we always assume the root won't be empty and p & q are in the BST, so no need to
        #   check if the root is None
        while (root.val - p.val) * (root.val - q.val) > 0:
            root = (root.left, root.right)[p.val > root.val]

        return root



a = TreeNode(6)
b = TreeNode(2)
c = TreeNode(8)
d = TreeNode(0)
e = TreeNode(4)
f = TreeNode(7)
g = TreeNode(9)
h = TreeNode(3)
i = TreeNode(5)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
e.left = h
e.right = i

Sol = Solution()
spot = Sol.lowestCommonAncestor(a, h, i)
print spot.val



'''
# my solution

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        while (root.val - p.val) * (root.val - q.val) > 0:
            if p.val>root.val:
                root = root.right
            else:
                root = root.left

        return root
'''



