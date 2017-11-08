
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):

        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def binaryTreePaths(self, root):

        if not root:
            return []

        self.ans = []
        def helper(node, path):
            if not node.left and not node.right:
                self.ans.append(path)
                return
            if node.left:
                # it is more efficient to put path increment here, instead of
                #   having to check if the path empty at the top of recursion
                helper(node.left, path + '->' + str(node.left.val))
            if node.right:
                helper(node.right, path + '->' + str(node.right.val))

        helper(root, str(root.val))
        return self.ans



a = TreeNode(6)
b = TreeNode(2)
c = TreeNode(8)
d = TreeNode(0)
e = TreeNode(4)
f = TreeNode(7)
g = TreeNode(9)
h = TreeNode(3)
i = TreeNode(5)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
e.left = h
e.right = i

Sol = Solution()
print Sol.binaryTreePaths(a)



'''
# iterative solution

class Solution(object):
    def binaryTreePaths(self, root):

        if not root:
            return []

        ans = []
        stack = [(root, str(root.val))]

        # this way is DFS;
        # if we change the stack into deque and popleft from it every time, plus switch the left/right order
        #   it will become BFS
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                ans.append(path)
            if node.right:
                stack.append((node.right, path + '->' + str(node.right.val)))
            if node.left:
                stack.append((node.left, path + '->' + str(node.left.val)))

        return ans
'''

