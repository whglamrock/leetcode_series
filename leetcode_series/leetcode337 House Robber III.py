
'''
idea comes from: https://leetcode.com/discuss/91652/c-java-python-%26-explanation
'''

class TreeNode:
    def __init__(self, val):

        self.val = val
        self.left, self.right = None, None


class Solution(object):
    def rob(self, root):

        def dfs(node):
            # return (subtree max money if not rob this node, subtree max money (this node "might be robbed"))
            if not node: return 0, 0
            max_l_ignore, max_l = dfs(node.left) # max_l means we "might" rob the left node
                # max_l_ignore means we already decided not to rob this left node
            max_r_ignore, max_r = dfs(node.right) # same as above
            return max_l + max_r, max(max_l + max_r, node.val + max_l_ignore + max_r_ignore) #for the
                # 'node.val + max_l_ignore + max_r_ignore', it means we rob this node for sure.

        return dfs(root)[1]

# the key point is return two parameters with dfs: although what we need is
# max(max_l + max_r, node.val + max_l_ignore + max_r_ignore), but both the not robbed one and "might" robbed ones:
# in other words, if we only return one value (lets say "max(max_l + max_r, node.val + max_l_ignore + max_r_ignore)"),
# in the next round of recursion the "max_l/r = dfs(node.left/right)" can only acquire one parameter, there is no
# max_l/r_ignore values for the return anymore.



a = TreeNode(3)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(3)
e = TreeNode(1)
a.left = b
a.right = c
b.right = d
c.right = e

Sol = Solution()
print Sol.rob(a)