
from collections import deque

# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):

        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findBottomLeftValue(self, root):

        firstleft = None
        todo = deque()
        todo.append(root)

        while todo:
            next = deque()
            firstleft = todo[0]
            while todo:
                node = todo.popleft()
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            todo = next

        return firstleft.val