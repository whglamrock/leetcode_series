
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):

        self.val = x
        self.left = None
        self.right = None


# idea from: https://discuss.leetcode.com/topic/36966/short-python-solution
class Solution(object):
    def largestBSTSubtree(self, root):

        def dfs(root):
            if (not root):
                return 0, 0, float('inf'), float('-inf')
            N1, n1, min1, max1 = dfs(root.left)
            N2, n2, min2, max2 = dfs(root.right)
            n = n1 + 1 + n2 if max1 < root.val < min2 else float('-inf')
            return max(N1, N2, n), n, min(min1, min2, root.val), max(max1, max2, root.val)

        return dfs(root)[0]