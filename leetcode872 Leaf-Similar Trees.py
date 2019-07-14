
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        leaves1, leaves2 = [], []
        self.traverse(leaves1, root1)
        self.traverse(leaves2, root2)
        return leaves1 == leaves2

    def traverse(self, current, node):

        if node.left:
            self.traverse(current, node.left)
        if node.right:
            self.traverse(current, node.right)
        if not node.left and not node.right:
            current.append(node.val)



'''
# iterative solution

class Solution(object):
    def leafSimilar(self, root1, root2):

        # traverse root1
        leaves1 = self.traverse(root1)
        leaves2 = self.traverse(root2)
        return leaves1 == leaves2
                    
    def traverse(self, root):
        stack = [root]
        leaves = []
        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                leaves.append(node.val)
            else:
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        return leaves
'''