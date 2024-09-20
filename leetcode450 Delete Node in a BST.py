from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        node, parent = self.dfs(root, key)
        # didn't find the node or the root is what we wanna delete
        if not node:
            if not root or root.val != key:
                return root
            leftChild, rightChild = root.left, root.right
            if not leftChild:
                return rightChild
            if not rightChild:
                return leftChild
            curr = leftChild
            while curr.right:
                curr = curr.right
            curr.right = rightChild
            return leftChild

        leftChild, rightChild = node.left, node.right
        if not leftChild and not rightChild:
            if parent.left == node:
                parent.left = None
            else:
                parent.right = None
        elif leftChild and rightChild:
            if parent.left == node:
                parent.left = leftChild
            else:
                parent.right = leftChild
            curr = leftChild
            while curr.right:
                curr = curr.right
            curr.right = rightChild
        elif leftChild:
            if parent.left == node:
                parent.left = leftChild
            else:
                parent.right = leftChild
        else:
            if parent.left == node:
                parent.left = rightChild
            else:
                parent.right = rightChild

        return root

    def dfs(self, root: Optional[TreeNode], key: int) -> Tuple[Optional[TreeNode], Optional[TreeNode]]:
        if not root:
            return None, None
        if not root.left and not root.right:
            return None, None

        if root.left and root.left.val == key:
            return root.left, root
        if root.right and root.right.val == key:
            return root.right, root

        if root.val < key:
            return self.dfs(root.right, key)
        else:
            return self.dfs(root.left, key)
