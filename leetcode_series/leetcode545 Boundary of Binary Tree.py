
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):

        self.val = x
        self.left = None
        self.right = None


# single pass solution needs to keep track the middle (leave) node
#   see: https://discuss.leetcode.com/topic/84258/java-preorder-single-pass-o-n-solution

class Solution(object):
    def boundaryOfBinaryTree(self, root):

        if not root: return []
        lb, rb = [root.val], []

        curr = root.left
        while curr and (curr.left or curr.right):
            lb.append(curr.val)
            if curr.left:
                curr = curr.left
            elif curr.right:
                curr = curr.right
            else:
                curr = None

        curr = root.right
        while curr and (curr.right or curr.left):
            rb.append(curr.val)
            if curr.right:
                curr = curr.right
            elif curr.left:
                curr = curr.left
            else:
                curr = None

        self.leaves = []
        # find all leaves from left to right
        def traversal(node):
            if node.left:
                traversal(node.left)
            if node.right:
                traversal(node.right)
            # the node != root condition is ver important:
            #   when the root has no children, we don't consider it as a leaf
            if node != root and not node.left and not node.right:
                self.leaves.append(node.val)
        traversal(root)

        rb.reverse()
        return lb + self.leaves + rb