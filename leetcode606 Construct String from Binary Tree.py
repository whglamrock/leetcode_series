
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# elegant pre-order recursion
class Solution(object):
    def tree2str(self, t):

        if not t:
            return ''
        if not t.left and not t.right:
            return str(t.val)
        if t.left and not t.right:
            return str(t.val) + '(' + self.tree2str(t.left) + ')'
        return str(t.val) + '(' + self.tree2str(t.left) + ')' + '(' + self.tree2str(t.right) + ')'



'''
# original inefficient solution:

class Solution(object):
    def tree2str(self, t):

        if not t:
            return ''
        string = self.traverse(t)

        ans = []
        i = 0
        curr = []
        while i < len(string):
            if string[i].isdigit():
                curr.append(string[i])
            else:
                if curr:
                    currNum = ''.join(curr)
                    ans.append(currNum)
                    curr = []
                # when we have the leaf node
                if string[i] == '(' and i + 3 < len(string) and string[i + 1] == ')' and string[i + 2] == '(' and string[i + 3] == ')':
                    i += 4
                    continue
                # when left node is not null and right node is null
                if string[i] == '(' and i + 2 < len(string) and string[i + 1] == ')' and string[i + 2] == ')':
                    i += 2
                    continue
                ans.append(string[i])
            i += 1

        if curr:
            ans.append(''.join(curr))
        if len(ans) >= 2 and ans[-1] == ')' and ans[-2] == '(':
            ans.pop()
            ans.pop()
        return ''.join(ans)

    # s is the current string
    def traverse(self, node):
        leftStr = ''
        rightStr = ''
        if node.left:
            leftStr = self.traverse(node.left)
        if node.right:
            rightStr = self.traverse(node.right)
        return str(node.val) + '(' + leftStr + ')' + '(' + rightStr + ')'
'''