from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.vals = []
        self.dfs(root)
        self.currIndex = 0

    def dfs(self, root: Optional[TreeNode]):
        if root.left:
            self.dfs(root.left)
        self.vals.append(root.val)
        if root.right:
            self.dfs(root.right)

    def next(self) -> int:
        val = self.vals[self.currIndex]
        self.currIndex += 1
        return val

    def hasNext(self) -> bool:
        return self.currIndex < len(self.vals)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
