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
    def buildSubTree(self, count: int) -> List[Optional[TreeNode]]:
        if count == 1:
            return [TreeNode(0)]
        output = []
        for i in range((count - 1) // 2):
            leftOutput = self.buildSubTree(i * 2 + 1)
            # make sure to minus the extra one because we use it for the root
            rightOutput = self.buildSubTree(count - (i * 2 + 1) - 1)
            for j in range(len(leftOutput)):
                for k in range(len(rightOutput)):
                    output.append(TreeNode(val=0, left=leftOutput[j], right=rightOutput[k]))

        return output
