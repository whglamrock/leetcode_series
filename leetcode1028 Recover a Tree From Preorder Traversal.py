from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        i, n = 0, len(traversal)
        stack = []
        depth = 0
        nodeToDepth = {}
        while i < n:
            if traversal[i].isdigit():
                currVal = int(traversal[i])
                while i + 1 < n and traversal[i + 1].isdigit():
                    currVal = currVal * 10 + int(traversal[i + 1])
                    i += 1
                node = TreeNode(currVal)
                nodeToDepth[node] = depth
                while stack and nodeToDepth[stack[-1]] >= depth:
                    stack.pop()
                if stack:
                    parentNode = stack[-1]
                    if not parentNode.left:
                        parentNode.left = node
                    else:
                        parentNode.right = node
                stack.append(node)
            else:
                depth = 1
                while i + 1 < n and traversal[i + 1] == '-':
                    i += 1
                    depth += 1
            i += 1

        return stack[0]
