class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.numOfGoodNodes = 0

    def goodNodes(self, root: TreeNode) -> int:
        self.numOfGoodNodes = 0
        self.dfs(root, -2147483648)
        return self.numOfGoodNodes

    def dfs(self, node: TreeNode, currMax: int):
        if node.val >= currMax:
            self.numOfGoodNodes += 1
        currMax = max(currMax, node.val)
        if node.left:
            self.dfs(node.left, currMax)
        if node.right:
            self.dfs(node.right, currMax)
