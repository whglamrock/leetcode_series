# Definition for a binary tree node. (P.S. in the leetcode, do not include the TreeNode class)
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):

        if (not root) or (not root.left):
            return root

        l = None
        head = []
        r = []
        mark = root

        while mark:
            head.append(mark.val)
            if (not mark.left):
                l = TreeNode(head.pop())
                break
            if mark.right:
                r.append(mark.right.val)
            else:
                r.append(None)

            mark = mark.left

        temp = l
        while head and r:
            rp = r.pop()
            hp = head.pop()
            if rp:
                lNode = TreeNode(rp)
                l.left = lNode
            else:
                l.left = None
            rNode = TreeNode(hp)
            l.right = rNode
            l = l.right

        return temp


