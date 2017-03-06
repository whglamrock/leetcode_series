# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root):
        if not root:
            return []
        res = []
        self.dfs(root, "", res)
        return res

    def dfs(self, root, ls, res):
        if not root.left and not root.right:
            res.append(ls+str(root.val))
        if root.left:
            self.dfs(root.left, ls+str(root.val)+"->", res)
        if root.right:
            self.dfs(root.right, ls+str(root.val)+"->", res)

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
print Sol.binaryTreePaths(a)


''' #iterative solution
class Solution:
#dfs + stack
    def binaryTreePaths1(self, root):
        if not root:
            return []
        res, stack = [], [(root, "")]
        while stack:
            node, ls = stack.pop()
            if not node.left and not node.right:
                res.append(ls+str(node.val))
            if node.right:
                stack.append((node.right, ls+str(node.val)+"->"))
            if node.left:
                stack.append((node.left, ls+str(node.val)+"->"))
        return res
'''

