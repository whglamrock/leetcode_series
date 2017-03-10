
from collections import deque

# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):

        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def largestValues(self, root):

        if not root:
            return []

        ans = []
        todo = deque()
        todo.append(root)

        while todo:
            next = deque()
            maxval = todo[0].val
            while todo:
                node = todo.popleft()
                maxval = max(maxval, node.val)
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            todo = next
            ans.append(maxval)

        return ans