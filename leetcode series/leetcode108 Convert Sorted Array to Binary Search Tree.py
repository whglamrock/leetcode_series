# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# O(n) recursive solution.
class Solution(object):
    def sortedArrayToBST(self, nums):

        if not nums:
            return None

        def helper(lst, root, direction):
            if not lst:
                return None
            l, r = 0, len(lst) - 1
            m = l + (r - l) / 2
            newnode = TreeNode(lst[m])
            if direction == 'L':
                root.left = newnode
            else:
                root.right = newnode
            helper(lst[:m], newnode, 'L')
            helper(lst[m + 1:], newnode, 'R')

        l, r = 0, len(nums) - 1
        m = l + (r - l) / 2
        root = TreeNode(nums[m])
        helper(nums[:m], root, 'L')
        helper(nums[m + 1:], root, 'R')

        return root