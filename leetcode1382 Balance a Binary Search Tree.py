# Definition for a binary tree node.
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        sortedNodes = self.traverseBST(root)
        m = len(sortedNodes) // 2
        newRoot = sortedNodes[m]
        self.buildBalancedBST(newRoot, 0, m - 1, sortedNodes)
        self.buildBalancedBST(newRoot, m + 1, len(sortedNodes) - 1, sortedNodes)
        return newRoot

    def buildBalancedBST(self, node: TreeNode, l: int, r: int, sortedNodes: List[TreeNode]):
        if l > r:
            return
        m = (l + r) // 2
        # sortedNodes[l:r + 1] is the left subtree
        if sortedNodes[r].val <= node.val:
            leftChild = sortedNodes[m]
            leftChild.left, leftChild.right = None, None
            node.left = leftChild
            self.buildBalancedBST(leftChild, l, m - 1, sortedNodes)
            self.buildBalancedBST(leftChild, m + 1, r, sortedNodes)
        else:
            rightChild = sortedNodes[m]
            rightChild.left, rightChild.right = None, None
            node.right = rightChild
            self.buildBalancedBST(rightChild, l, m - 1, sortedNodes)
            self.buildBalancedBST(rightChild, m + 1, r, sortedNodes)

    def traverseBST(self, root: TreeNode) -> List[TreeNode]:
        leftSubtree, rightSubtree = [], []
        if root.left:
            leftSubtree = self.traverseBST(root.left)
        if root.right:
            rightSubtree = self.traverseBST(root.right)
        return leftSubtree + [root] + rightSubtree
