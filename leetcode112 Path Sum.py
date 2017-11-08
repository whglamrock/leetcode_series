
class TreeNode(object):
    def __init__(self, x):

        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def hasPathSum(self, root, sum):

        if root == None:
            return False

        def summup(root1, last, num):
            if root1.left == None and root1.right == None:
                last += root1.val
                if last == num:
                    return True
            else:
                last += root1.val
                if root1.left == None:
                    return summup(root1.right, last, num)
                elif root1.right == None:
                    return summup(root1.left, last, num)
                else:
                    return (summup(root1.left, last, num) or summup(root1.right, last, num))

        return summup(root,0,sum) == True



a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
a.right = b
b.right = c
Sol = Solution()
e = Sol.hasPathSum(a,6)
print e
