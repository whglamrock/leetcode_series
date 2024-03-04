from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.leaves = []

    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        leftBoundary = []
        curr = root.left
        while curr:
            # non leaf node
            if curr.left or curr.right:
                leftBoundary.append(curr.val)
            # leaf node
            else:
                break
            if curr.left:
                curr = curr.left
            else:
                curr = curr.right

        rightBoundary = []
        curr = root.right
        while curr:
            # non leaf node
            if curr.left or curr.right:
                rightBoundary.append(curr.val)
            # leaf node
            else:
                break
            if curr.right:
                curr = curr.right
            else:
                curr = curr.left

        # get all leaf nodes
        self.leaves = []
        self.dfs(root, root)

        return [root.val] + leftBoundary + self.leaves + rightBoundary[::-1]

    def dfs(self, node: Optional[TreeNode], root: Optional[TreeNode]):
        if not node.left and not node.right and node != root:
            self.leaves.append(node.val)
            return

        if node.left:
            self.dfs(node.left, root)
        if node.right:
            self.dfs(node.right, root)
