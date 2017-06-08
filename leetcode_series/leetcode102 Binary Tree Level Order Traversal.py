
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):

        self.val = x
        self.left = None
        self.right = None


from collections import deque

class Solution(object):
    def levelOrder(self, root):

        if not root:
            return []

        todo = deque([root])
        ans = []
        while todo:
            next = deque()
            currlevel = []
            while todo:
                node = todo.popleft()
                currlevel.append(node.val)
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            todo = next
            ans.append(currlevel)

        return ans
