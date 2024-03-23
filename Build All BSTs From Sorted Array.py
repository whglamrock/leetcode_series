from typing import List, Optional

class TreeNode:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildBST(self, nums: List[int]) -> List[Optional[TreeNode]]:
        if not nums:
            return [None]
        if len(nums) == 1:
            return [TreeNode(nums[0])]

        ans = []
        for i in range(len(nums)):
            leftChildren = self.buildBST(nums[:i])
            rightChildren = self.buildBST(nums[i + 1:])
            for leftChild in leftChildren:
                for rightChild in rightChildren:
                    root = TreeNode(nums[i])
                    root.left = leftChild
                    root.right = rightChild
                    ans.append(root)

        return ans


def printTree(root: Optional[TreeNode]):
    if not root:
        return

    currLevel = [root]
    vals = []
    while currLevel:
        nextLevel = []
        level = []
        for node in currLevel:
            if not node:
                level.append(None)
                continue
            level.append(node.val)
            if node.left:
                nextLevel.append(node.left)
            if node.right:
                nextLevel.append(node.right)
        currLevel = nextLevel
        vals.append(level)

    print(vals)


bsts = Solution().buildBST([1, 2, 3, 4, 5])
for bst in bsts:
    printTree(bst)
