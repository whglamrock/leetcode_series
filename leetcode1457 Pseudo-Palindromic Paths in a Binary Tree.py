from collections import defaultdict
from copy import deepcopy
from typing import Optional, Dict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.pathCount = 0

    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        self.pathCount = 0
        self.dfs(root, defaultdict(int))
        return self.pathCount

    def dfs(self, node: Optional[TreeNode], currNumCount: Dict[int, int]):
        currNumCount[node.val] += 1
        if not node.left and not node.right:
            oddNumCount = 0
            for count in currNumCount.values():
                if count % 2:
                    oddNumCount += 1
            if oddNumCount <= 1:
                self.pathCount += 1
            return

        if node.left:
            self.dfs(node.left, deepcopy(currNumCount))
        if node.right:
            self.dfs(node.right, deepcopy(currNumCount))
