class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        def fku(root1,level):
            if root1.left == None and root1.right == None:
                return level
            elif root1.right == None:
                level += 1
                return fku(root1.left,level)
            elif root1.left == None:
                level += 1
                return fku(root1.right,level)
            else:
                level += 1
                return min(fku(root1.left,level),fku(root1.right,level))

        return fku(root,1)

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
a.left = b
b.right = c
Sol = Solution()
e = Sol.minDepth(a)
print e
