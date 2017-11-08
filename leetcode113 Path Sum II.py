
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):

        self.val = x
        self.left = None
        self.right = None


# basic idea is depth-first search, look at the tree level by level and record every path

class Solution(object):
    def pathSum(self, root, summary):

        if (not root):
            return []

        stack = [[root.val, root]]
        res = []
        while stack:
            next = []
            for item in stack:
                last = item.pop()
                if (not last.left) and (not last.right):
                    if sum(item) == summary:
                        res.append(item)
                if last.left:
                    next.append(item+[last.left.val, last.left])
                if last.right:
                    next.append(item+[last.right.val, last.right])
            stack = next

        return res