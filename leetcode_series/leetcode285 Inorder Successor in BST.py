
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):

        self.val = x
        self.left = None
        self.right = None


# conception about inorder successor:
# https://discuss.leetcode.com/topic/29428/for-those-who-is-not-so-clear-about-inorder-successors

class Solution(object):
    def inorderSuccessor(self, root, p):

        if root == None:
            return None

        if p.val < root.val:    # it could be either when looking for p looking for the
            # potential successor (first left value or root itself)
            suc = self.inorderSuccessor(root.left, p)
            # when we go left, the suc could be None. in this case we return suc's root
            if suc != None:
                return suc
            else:   # when there is no valid left value
                return root
        else:   # even when p.val == root.val. because we need to find successor,
            # which can't be p itself.
            return self.inorderSuccessor(root.right, p)



# consider the following test cases to execute the while loop
#         1
#     4      6
#  2    3       7
# where p = 3
#         2
#            4
#         3     5
# where p = 2



