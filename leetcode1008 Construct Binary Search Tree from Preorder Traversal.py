from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# O(n) stack solution
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        stack = [root]

        for val in preorder[1:]:
            newNode = TreeNode(val)
            if val < stack[-1].val:
                stack[-1].left = newNode
                stack.append(newNode)
            else:
                node = None
                while stack and val > stack[-1].val:
                    node = stack.pop()
                # no need to check if node is not None
                node.right = newNode
                stack.append(newNode)

        return root


'''
# original straightforward binary search O(N * log(N)) solution, should be acceptable in real interview
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        return self.buildBst(preorder, 0, len(preorder) - 1)

    def buildBst(self, preorder: List[int], l: int, r: int) -> Optional[TreeNode]:
        if l == r:
            return TreeNode(preorder[l])

        node = TreeNode(preorder[l])
        startIndexOfRightSubtree = self.findMinIndexBiggerThan(preorder, l + 1, r, preorder[l])
        if startIndexOfRightSubtree == -1:
            node.left = self.buildBst(preorder, l + 1, r)
        else:
            node.right = self.buildBst(preorder, startIndexOfRightSubtree, r)
            if startIndexOfRightSubtree > l + 1:
                node.left = self.buildBst(preorder, l + 1, startIndexOfRightSubtree - 1)

        return node

    def findMinIndexBiggerThan(self, nums: List[int], l: int, r: int, target: int) -> int:
        while l <= r:
            m = (l + r) // 2
            if l == r:
                if nums[m] > target:
                    return m
                else:
                    return -1
            if nums[m] > target:
                r = m
            else:
                l = m + 1

        return -1
'''