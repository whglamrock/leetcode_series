# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# pay attention to iterative solution
class Solution(object):
    def preorderTraversal(self, root):

        self.ans = []
        def helper(node):
            if not node:
                return
            else:
                self.ans.append(node.val)
                helper(node.left)
                helper(node.right)

        helper(root)
        return self.ans


'''
# iterative solution:
class Solution(object):
    def preorderTraversal(self, root):

        ans = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                ans.append(node.val)
            else:
                continue
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return ans
'''