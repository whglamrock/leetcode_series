from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodeValToLeftChildVal, nodeValToRightChildVal = {}, {}
        childVals = set()
        vals = set()
        for nodeVal, childVal, isLeft in descriptions:
            if isLeft:
                nodeValToLeftChildVal[nodeVal] = childVal
            else:
                nodeValToRightChildVal[nodeVal] = childVal

            childVals.add(childVal)
            vals.add(nodeVal)
            vals.add(childVal)

        root = None
        curr = []
        for nodeVal in vals:
            if nodeVal not in childVals:
                root = TreeNode(nodeVal)
                if nodeVal in nodeValToLeftChildVal:
                    leftChild = TreeNode(nodeValToLeftChildVal[nodeVal])
                    root.left = leftChild
                if nodeVal in nodeValToRightChildVal:
                    rightChild = TreeNode(nodeValToRightChildVal[nodeVal])
                    root.right = rightChild
                curr.append(root)
                break

        if not root:
            return None

        # level order traversal
        while curr:
            next = []
            for node in curr:
                if node.val in nodeValToLeftChildVal:
                    leftChild = TreeNode(nodeValToLeftChildVal[node.val])
                    node.left = leftChild
                    next.append(leftChild)
                if node.val in nodeValToRightChildVal:
                    rightChild = TreeNode(nodeValToRightChildVal[node.val])
                    node.right = rightChild
                    next.append(rightChild)

            curr = next

        return root
