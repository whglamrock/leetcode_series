from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# remember the order * 2 & order * 2 + 1 trick.
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        ans = 0
        curr = [[0, root]]
        while curr:
            ans = max(ans, curr[-1][0] - curr[0][0] + 1)
            next = []
            for order, node in curr:
                if node.left:
                    next.append([order * 2, node.left])
                if node.right:
                    next.append([order * 2 + 1, node.right])
            curr = next

        return ans
