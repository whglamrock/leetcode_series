from typing import Optional, Tuple

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.longest = 0

    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None

        self.longest = 0
        self.dfs(root)
        return self.longest

    def dfs(self, node: Optional[TreeNode]) -> Tuple[int, int]:
        if not node:
            return 0, 0
        if not node.left and not node.right:
            self.longest = max(self.longest, 1)
            return 1, 1

        longestIncreasing, longestDecreasing = 1, 1
        longestIncreasingFromLeft, longestDecreasingFromLeft = self.dfs(node.left)
        longestIncreasingFromRight, longestDecreasingFromRight = self.dfs(node.right)
        if node.left and node.left.val == node.val + 1:
            longestIncreasing = max(longestIncreasing, 1 + longestIncreasingFromLeft)
        if node.right and node.right.val == node.val + 1:
            longestIncreasing = max(longestIncreasing, 1 + longestIncreasingFromRight)
        if node.left and node.left.val == node.val - 1:
            longestDecreasing = max(longestDecreasing, 1 + longestDecreasingFromLeft)
        if node.right and node.right.val == node.val - 1:
            longestDecreasing = max(longestDecreasing, 1 + longestDecreasingFromRight)

        self.longest = max(self.longest, longestIncreasing)
        self.longest = max(self.longest, longestDecreasing)
        if longestIncreasing > 1 and longestDecreasing > 1:
            self.longest = max(self.longest, longestIncreasing + longestDecreasing - 1)

        return longestIncreasing, longestDecreasing
