from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans = deque()

    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        self.ans = deque()
        self.findSmallerValues(root, target, k)
        self.findBiggerValues(root, target, k)
        return list(self.ans)

    def findSmallerValues(self, root: Optional[TreeNode], target: float, k: int):
        if not root:
            return
        if root.val <= target:
            # only in right subtree there could be smaller than target but closer than root values
            self.findSmallerValues(root.right, target, k)
            if len(self.ans) == k:
                # we directly return here because findSmallerValues gets called first and we know the
                # ans deque only contains values <= target
                return
            self.ans.appendleft(root.val)
            
        self.findSmallerValues(root.left, target, k)

    def findBiggerValues(self, root: Optional[TreeNode], target: float, k: int):
        if not root:
            return
        if root.val > target:
            self.findBiggerValues(root.left, target, k)
            if len(self.ans) == k:
                if target - self.ans[0] > root.val - target:
                    self.ans.popleft()
                else:
                    return
            self.ans.append(root.val)

        self.findBiggerValues(root.right, target, k)
