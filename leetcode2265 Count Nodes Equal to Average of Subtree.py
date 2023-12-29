from typing import Tuple

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.ans = 0

    def averageOfSubtree(self, root: TreeNode) -> int:
        self.ans = 0
        self.traverseTree(root)
        return self.ans

    def traverseTree(self, node: TreeNode) -> Tuple[int, int]:
        if not node.left and not node.right:
            # leaf node for sure equals to itself
            self.ans += 1
            return node.val, 1

        sumOfTree = node.val
        nodeCount = 1
        if node.left:
            returnTuple = self.traverseTree(node.left)
            sumOfTree += returnTuple[0]
            nodeCount += returnTuple[1]
        if node.right:
            returnTuple = self.traverseTree(node.right)
            sumOfTree += returnTuple[0]
            nodeCount += returnTuple[1]
        # the question asks for floor division
        if node.val == sumOfTree // nodeCount:
            self.ans += 1

        return sumOfTree, nodeCount



