
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):

        self.val = x
        self.left = None
        self.right = None


# remember to 'node.left = None'!

class Solution(object):
    def flatten(self, root):

        if not root:
            return

        def helper(node):
            if (not node.left) and (not node.right):
                return node, node
            elif (not node.left) and node.right:
                rhead, rtail = helper(node.right)
                node.right = rhead
                node.left = None
                return node, rtail
            elif node.left and (not node.right):
                lhead, ltail = helper(node.left)
                node.right = lhead
                node.left = None
                return node, ltail
            else:
                lhead, ltail = helper(node.left)
                rhead, rtail = helper(node.right)
                node.right = lhead
                node.left = None
                ltail.right = rhead
                return node, rtail
                
        helper(root)
        #return root  # stupid leetcode asked to return nothing