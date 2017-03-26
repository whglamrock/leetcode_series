
'''
The definition of binary search tree: https://zh.wikipedia.org/wiki/%E4%BA%8C%E5%85%83%E6%90%9C%E5%B0%8B%E6%A8%B9
The algorithm idea came from: https://leetcode.com/discuss/44959/3-lines-with-o-1-space-1-liners-alternatives
As for the trick of tuple: try: c = (2,3)[4>3] and c = (2,3)[2>3]
'''

class TreeNode(object):
    def __init__(self, x):

        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):

        while (root.val - p.val) * (root.val - q.val) > 0:
            root = (root.left, root.right)[p.val > root.val]

        return root



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
spot = Sol.lowestCommonAncestor(a, h, i)
print spot.val



'''
# my solution:
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        while (root.val - p.val) * (root.val - q.val) > 0:
            if p.val>root.val:
                root = root.right
            else:
                root = root.left

        return root
'''



'''
# my primitive solution:
class Solution(object):
    def find(self, head, node):
        if (not head):
            return False
        elif head == node or head.left == node or head.right == node:
            return True
        else:
            return (self.find(head.left, node) or self.find(head.right, node))

    def findboth(self, head, node1, node2):
        if self.find(head, node1) == self.find(head, node2) == True:
            return True
        else:
            return False

    def lowestCommonAncestor(self, root, p, q):

        if (not root) or self.findboth(root,p,q) == False:
            return None

        def LCA(gen, node1, node2):
            if self.findboth(gen.left,node1,node2) == self.findboth(gen.right,node1,node2) == False:
                return gen
            else:
                if self.findboth(gen.left,node1,node2) == True:
                    return LCA(gen.left,node1,node2)
                else:
                    return LCA(gen.right,node1,node2)

        return LCA(root, p, q)
'''


