
from collections import defaultdict, deque

# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):

        self.val = x
        self.left = None
        self.right = None



class Solution(object):
    def verticalOrder(self, root):

        if not root: return []

        dic = defaultdict(list)
        mincol, maxcol = 0, 0
        ans = []

        todo = deque()
        todo.append((0, 0, root))

        # remember that we can't use a simple to do list and pop from right
            # because the level order traverse has to be from left to right
        while todo:
            next = deque()
            while todo:
                row, col, node = todo.popleft()
                mincol = min(mincol, col)
                maxcol = max(maxcol, col)
                dic[col].append(node.val)
                if node.left:
                    next.append(((row + 1, col - 1, node.left)))
                if node.right:
                    next.append(((row + 1, col + 1, node.right)))
            todo = next

        for col in xrange(mincol, maxcol + 1):
            ans.append(dic[col])

        return ans