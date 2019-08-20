
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



# idea from: https://leetcode.com/problems/distribute-coins-in-binary-tree/solution/, notice the intuition part

# we count the number of moves needed for each NODE, and we use DFS from bottom to top to return the state after
# each subtree has completed moves.

class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0

        def dfs(node):

            if not node:
                return 0

            L, R = dfs(node.left), dfs(node.right)
            self.ans += abs(L) + abs(R)

            # the L & R can offset each other, so we we count the number of moves
            return (node.val - 1) + L + R

        dfs(root)
        return self.ans