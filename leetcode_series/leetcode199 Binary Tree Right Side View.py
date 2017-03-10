# Traversal of tree level by level and return the last node's value on each level
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if (not root):
            return []
        stack = [root]
        ans = []
        while stack:
            new = []
            ans.append(stack[-1].val)
            for item in stack:
                if item.left:
                    new.append(item.left)
                if item.right:
                    new.append(item.right)
            stack = new

        return ans
