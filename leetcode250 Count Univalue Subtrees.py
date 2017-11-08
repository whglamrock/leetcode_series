
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):

        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def countUnivalSubtrees(self, root):

        def check(head):
            if (not head):
                return False
            stack = [head]
            lst = []
            while stack:
                node = stack.pop()
                if lst:
                    if node.val != lst[-1]:
                        return False
                lst.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            return True

        counter = []
        def count(head):
            if (not head):
                return None
            if check(head) == True:
                counter.append(0)
            if head.left:
                count(head.left)
            if head.right:
                count(head.right)

        count(root)

        return len(counter)



a = TreeNode(5)
b = TreeNode(1)
c = TreeNode(5)
d = TreeNode(5)
e = TreeNode(5)
f = TreeNode(5)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

Sol = Solution()
print Sol.countUnivalSubtrees(a)

