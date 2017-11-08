
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):

        self.val = x
        self.left = None
        self.right = None


# every time we hit a new node, we calculate if there is a feasible path that ENDS with
# this node.

class Solution(object):
    def helper(self, lst, target):

        windowsum = 0
        ans = 0
        # the sum will start from the last element
        for i in xrange(len(lst) - 1, -1, -1):
            windowsum += lst[i]
            if windowsum == target:
                ans += 1
        return ans

    def pathSum(self, root, s):

        if not root:
            return 0

        self.res = 0

        def recursion(node, path):
            if node:
                self.res += self.helper(path + [node.val], s)
            if node and node.left:
                recursion(node.left, path + [node.val])
            if node and node.right:
                recursion(node.right, path + [node.val])

        recursion(root, [])
        return self.res