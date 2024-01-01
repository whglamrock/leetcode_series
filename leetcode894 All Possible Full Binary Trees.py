from functools import lru_cache
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []
        return self.buildSubTree(n)

    # the recursion has to take integer (not any node) as input in order to use cache
    @lru_cache(None)
    def buildSubTree(self, count: int) -> List[TreeNode]:
        if count == 1:
            return [TreeNode(0)]

        ans = []
        for i in range(count // 2):
            leftCount = i * 2 + 1
            # root node uses 1 count
            rightCount = count - 1 - leftCount
            leftSubtrees = self.buildSubTree(leftCount)
            rightSubtrees = self.buildSubTree(rightCount)
            for leftSubtree in leftSubtrees:
                for rightSubtree in rightSubtrees:
                    ans.append(TreeNode(0, leftSubtree, rightSubtree))

        return ans
