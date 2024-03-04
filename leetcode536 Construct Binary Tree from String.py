from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# remember to use stack for this question. Finding the balanced back parenthesis idea won't work since len(s) is too big
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        if not s:
            return None

        stack = []
        i = 0
        n = len(s)
        while i < n:
            if s[i].isdigit() or s[i] == '-':
                j = i
                while i + 1 < n and s[i + 1].isdigit():
                    i += 1
                val = int(s[j:i + 1])
                node = TreeNode(val)
                if stack:
                    parent = stack[-1]
                    if parent.left:
                        parent.right = node
                    else:
                        parent.left = node
                stack.append(node)
            else:
                if s[i] == ')':
                    stack.pop()
            i += 1

        return stack[0]
