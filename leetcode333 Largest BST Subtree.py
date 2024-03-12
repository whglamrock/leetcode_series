from typing import Optional, Tuple

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.nodeToNumOfNodes = {}
        self.nodeToIsBst = {}

    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.nodeToIsBst = {}
        self.nodeToNumOfNodes = {}
        self.dfs(root)

        maxNumOfNode = 0
        for node in self.nodeToIsBst:
            if self.nodeToIsBst[node]:
                maxNumOfNode = max(maxNumOfNode, self.nodeToNumOfNodes[node])

        return maxNumOfNode

    def dfs(self, node: Optional[TreeNode]) -> Tuple[int, int, int]:
        if not node.left and not node.right:
            self.nodeToIsBst[node] = True
            self.nodeToNumOfNodes[node] = 1
            return node.val, node.val, 1

        minVal, maxVal, numOfNodes = node.val, node.val, 1
        isBst = True
        if node.left:
            minOfLeft, maxOfLeft, numOfNodesInLeft = self.dfs(node.left)
            if maxOfLeft >= node.val or not self.nodeToIsBst[node.left]:
                isBst = False
            numOfNodes += numOfNodesInLeft
            minVal = min(minVal, minOfLeft)
            maxVal = max(maxVal, maxOfLeft)
        if node.right:
            minOfRight, maxOfRight, numOfNodesInRight = self.dfs(node.right)
            if minOfRight <= node.val or not self.nodeToIsBst[node.right]:
                isBst = False
            numOfNodes += numOfNodesInRight
            minVal = min(minVal, minOfRight)
            maxVal = max(maxVal, maxOfRight)

        self.nodeToIsBst[node] = isBst
        self.nodeToNumOfNodes[node] = numOfNodes
        return minVal, maxVal, numOfNodes
