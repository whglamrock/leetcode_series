# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def longestConsecutive(self, root):

        if not root: return 0
        self.longest = 0

        def helper(node, seq):
            if (not node.left) and (not node.right):
                self.longest = max(self.longest, seq)
            if node.left:
                if node.left.val == node.val + 1:
                    helper(node.left, seq + 1)
                else:
                    self.longest = max(self.longest, seq)
                    helper(node.left, 1)
            if node.right:
                if node.right.val == node.val + 1:
                    helper(node.right, seq + 1)
                else:
                    self.longest = max(self.longest, seq)
                    helper(node.right, 1)

        helper(root, 1)
        return self.longest

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)

a.right = c
c.left = b
c.right = d
d.right = e

Sol = Solution()
print Sol.longestConsecutive(a)
