
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):

        self.val = x
        self.left = None
        self.right = None


# modify the order of preorder traversal to "root-right-left" and then reverse it
#   or just simply use deque and appendleft the newly visited node value

class Solution(object):
    def postorderTraversal(self, root):

        if not root:
            return []

        stack = [root]
        ans = []

        while stack:
            node = stack.pop()
            ans.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return ans[::-1]



'''
# recursive solution

class Solution(object):
    def postorderTraversal(self, root):

        self.ans = []

        def helper(node):
            if not node:
                return
            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)
            self.ans.append(node.val)

        helper(root)
        return self.ans
'''