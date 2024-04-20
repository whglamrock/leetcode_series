from collections import defaultdict
from typing import Optional, Dict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# there is no way to avoid copying the sumCount hashmap. This question is basically counting the combination sum
class Solution:
    def __init__(self):
        self.ans = 0

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0

        self.ans = 0
        self.dfs(root, defaultdict(int), targetSum)
        return self.ans

    def dfs(self, node: Optional[TreeNode], currSumCount: Dict[int, int], targetSum: int):
        nextSumCount = defaultdict(int)
        for currSum, count in currSumCount.items():
            newSum = currSum + node.val
            nextSumCount[newSum] = count
        # start from the current node
        nextSumCount[node.val] += 1

        self.ans += nextSumCount[targetSum]
        if node.left:
            self.dfs(node.left, nextSumCount, targetSum)
        if node.right:
            self.dfs(node.right, nextSumCount, targetSum)
