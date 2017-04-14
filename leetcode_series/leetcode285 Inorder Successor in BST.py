
# Definition for a binary tree node (P.S., the tree is a BST).

class TreeNode(object):
    def __init__(self, x):

        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderSuccessor(self, root, p):

        succ = None
        while root:
            # in this case, the p could be in root's left subtree
            #   or the current root is p's right child
            if p.val < root.val:    # then this root is potential successor
                succ = root
                root = root.left
            # the current root can't be p's left child
            else:   # contains the case when p.val == root.val, and the current root can't be candidate
                root = root.right

        # still applies when the while loop or the if statement didn't execute
        return succ



# consider the following test cases to execute the while loop:
#
#         1
#     4      6
#  2    3       7
# where p = 3
#
#         2
#            4
#         3     5
# where p = 2



'''
# recursive solution:

class Solution(object):
    def inorderSuccessor(self, root, p):

        if not root:
            return None

        # then this root is potential successor
        if p.val < root.val:
            suc = self.inorderSuccessor(root.left, p)
            return suc if suc else root
        # this current root can't be the candidate for successor
        else:   # even when p.val == root.val
            return self.inorderSuccessor(root.right, p)
'''

'''
# recursive solution for finding the inorderPredecessor:

class Solution(object):
    def inorderPredecessor(self, root, p):

        if not root:
            return None

        # in this case, the p could be in root's right subtree
        #   or the current root is p's left child
        if p.val > root.val:
            pred = self.inorderPredecessor(root.right, p)
            return pred if pred else root   # the root could be candidate
        else:
            # it applies even when the following value is None
            return self.inorderPredecessor(root.left, p)
'''



