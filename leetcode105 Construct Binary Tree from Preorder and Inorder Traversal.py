
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# One of classic binary tree questions. The idea is:
    # 1) The preorder[0] is the root the recursion should return;
    # 2) the inorder[inL:inR + 1] are the subtree under the root of this recursion
    # 3) use recursion to build the subtree, then return the root of this recursion

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None

        valueToIndex = {}
        for i, value in enumerate(inorder):
            valueToIndex[value] = i

        return self.buildSubTree(preorder, 0, inorder, 0, len(inorder) - 1, valueToIndex)

    # preIndex points to the root this recursion should return
    # inorder[inL:inR + 1] separates the nodes in this subtree
    def buildSubTree(self, preorder, preIndex, inorder, inL, inR, valueToIndex):
        if inL > inR:
            return None
        if inL == inR:
            return TreeNode(inorder[inL])

        rootVal = preorder[preIndex]
        root = TreeNode(rootVal)

        rootIndexInorder = valueToIndex[rootVal]

        numOfNodesInLeft = rootIndexInorder - inL

        leftChild = self.buildSubTree(preorder, preIndex + 1, inorder, inL, rootIndexInorder - 1, valueToIndex)
        root.left = leftChild

        rightChild = self.buildSubTree(preorder, preIndex + 1 + numOfNodesInLeft, inorder, rootIndexInorder + 1, inR, valueToIndex)
        root.right = rightChild

        return root