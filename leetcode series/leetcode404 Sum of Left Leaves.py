# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# pay attention to the question requirement. The sum of "leaves" not all left nodes.
class Solution(object):
    def sumOfLeftLeaves(self, root):

        if not root:
            return 0

        ans = 0
        stack = [('r', root)]
        while stack:
            next = []
            for (direction, node) in stack:
                if (not node.left) and (not node.right):
                    if direction == 'l':
                        ans += node.val
                    continue
                if node.left:
                    next.append(('l', node.left))
                if node.right:
                    next.append(('r', node.right))
            stack = next

        return ans

