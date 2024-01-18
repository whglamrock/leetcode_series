from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# need to recognize the idea is to find the index (i.e., i) of preorder[0] (the root) in the inorder array.
# then the inorder[:i] is the left subtree, and inorder[i + 1:] is the right subtree
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        i = 0
        while i < len(inorder) and inorder[i] != preorder[0]:
            i += 1

        root.left = self.buildTree(preorder[1:i + 1], inorder[:i])
        root.right = self.buildTree(preorder[i + 1:], inorder[i + 1:])
        return root
