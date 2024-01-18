from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        if root and root.left:
            ans += self.inorderTraversal(root.left)
        if root:
            ans.append(root.val)
        if root and root.right:
            ans += self.inorderTraversal(root.right)
        return ans
