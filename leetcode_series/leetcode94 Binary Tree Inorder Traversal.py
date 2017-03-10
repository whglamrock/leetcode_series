
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):

        self.val = x
        self.left = None
        self.right = None


# pay attention to iterative solution

class Solution(object):
    def inorderTraversal(self, root):
        
        self.ans = []
        def helper(node):
            if node and node.left:
                helper(node.left)
            if node:
                self.ans.append(node.val)
            if node and node.right:
                helper(node.right)

        helper(root)
        return self.ans



'''
# iterative solution

class Solution(object):
    def inorderTraversal(self, root):

        ans, cur, stack = [], root, []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            ans.append(cur.val)
            cur = cur.right

        return ans
'''
