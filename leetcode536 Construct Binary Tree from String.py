
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):

        self.val = x
        self.left = None
        self.right = None


# remember when to pop and unify the operation for the case when s[i] == '(' or ')'
# when encountering parenthesis, usually the ')' is the indication for popping, but
#   '(' is not necessarily the start of a new number. In most cases, we should use
#   a while loop to build the number

class Solution(object):
    def str2tree(self, s):

        if not s: return
        stack = []
        i = 0

        while i < len(s):
            j, char = i, s[i]
            if char.isdigit() or char == '-':
                while i + 1 < len(s) and s[i + 1].isdigit():
                    i += 1
                node = TreeNode(int(s[j:i + 1]))
                if stack:
                    parent = stack[-1]
                    if parent.left:
                        parent.right = node
                    else:
                        parent.left = node
                stack.append(node)
            else:
                if char == ')':
                    stack.pop()
            i += 1

        return stack[0]    # or stack[-1]