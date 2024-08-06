from typing import Optional


# The answer for the followup question is at the bottom.
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


'''
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.pushAll(root)

    def next(self) -> int:
        node = self.stack.pop()
        self.pushAll(node.right)
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0
    
    def pushAll(self, node: Optional[TreeNode]):
        while node:
            self.stack.append(node)
            node = node.left
'''