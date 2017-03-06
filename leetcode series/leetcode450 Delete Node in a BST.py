# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# the leetcode test cases are stupid.
class Solution(object):
    def deleteNode(self, root, key):

        if not root or key == None:
            return root

        def finder(parent, node, key):
            if not node:
                return parent, None
            elif node.val == key:
                return parent, node
            elif node.val < key:
                return finder(node, node.right, key)
            else:
                return finder(node, node.left, key)

        parent, node = finder(None, root, key)
        if not node:
            return root

        def helper(node):
            if not node:
                return None
            elif (not node.left) and (not node.right):
                return None
            elif (not node.left) and node.right:
                return node.right
            elif node.left and (not node.right):
                return node.left
            else:
                org = node
                prev, node = node, node.right
                while node and node.left:
                    prev = node
                    node = node.left
                if prev != org:
                    prev.left = node.right
                    node.right = None
                    node.left = org.left
                    node.right = org.right
                    org.left, org.right = None, None
                else:
                    node.left = org.left
                    org.left, org.right = None, None
                return node

        if not parent:
            newnode = helper(root)
            return newnode
        else:
            if parent.left is node:
                newnode = helper(node)
                parent.left = newnode
            else:
                newnode = helper(node)
                parent.right = newnode
            return root
