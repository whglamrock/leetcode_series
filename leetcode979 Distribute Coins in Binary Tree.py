from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.ans = 0

    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.dfs(root)
        return self.ans

    # returns the number of coins given to its parent
    def dfs(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        numOfCoinsFromLeft = self.dfs(node.left)
        numOfCoinsFromRight = self.dfs(node.right)
        # only count the move when the coins are actually moved to the node's parent
        self.ans += abs(numOfCoinsFromLeft) + abs(numOfCoinsFromRight)
        # node.val - 1 is the number of coins given to its parent from this node itself
        return (node.val - 1) + numOfCoinsFromLeft + numOfCoinsFromRight
