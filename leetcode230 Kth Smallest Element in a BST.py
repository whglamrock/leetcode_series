from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans = -1
        self.count = 0

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.ans = -1
        self.dfs(root, k)
        return self.ans

    def dfs(self, node: Optional[TreeNode], k: int):
        if not node:
            return

        self.dfs(node.left, k)
        self.count += 1
        if self.count == k:
            self.ans = node.val

        self.dfs(node.right, k)


'''
# Non optimal O(n) space solution.
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
'''