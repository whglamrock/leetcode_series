from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# if there is a lot of insertion to the BST, the optimization is to keep a
# node to number of children map. So we can directly use BST structure to do binary search
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.inOrderTraversal(root)[k - 1]

    def inOrderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        if root.left:
            ans = self.inOrderTraversal(root.left) + ans
        ans.append(root.val)
        if root.right:
            ans += self.inOrderTraversal(root.right)
        return ans
