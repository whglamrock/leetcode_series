from typing import Optional, Tuple

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.nodeToSubtreeSum = {}
        self.bsts = set()

    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.bsts = set()
        self.findBst(root)
        self.nodeToSubtreeSum = {}
        self.getSubtreeSum(root)

        ans = 0
        for node in self.bsts:
            if node not in self.nodeToSubtreeSum:
                continue
            ans = max(ans, self.nodeToSubtreeSum[node])

        return ans

    # return the min & max values of the tree
    def findBst(self, node: Optional[TreeNode]) -> Tuple[int, int]:
        if not node.left and not node.right:
            self.bsts.add(node)
            return node.val, node.val

        if node.left and node.right:
            leftMin, leftMax = self.findBst(node.left)
            rightMin, rightMax = self.findBst(node.right)
            if leftMax < node.val < rightMin and (node.left in self.bsts and node.right in self.bsts):
                self.bsts.add(node)
            return leftMin, rightMax
        elif node.left:
            leftMin, leftMax = self.findBst(node.left)
            if node.val > leftMax and node.left in self.bsts:
                self.bsts.add(node)
            return leftMin, node.val
        else:
            rightMin, rightMax = self.findBst(node.right)
            if node.val < rightMin and node.right in self.bsts:
                self.bsts.add(node)
            return node.val, rightMax

    def getSubtreeSum(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0

        subtreeSum = node.val
        if node.left:
            subtreeSum += self.getSubtreeSum(node.left)
        if node.right:
            subtreeSum += self.getSubtreeSum(node.right)

        self.nodeToSubtreeSum[node] = subtreeSum
        return subtreeSum
