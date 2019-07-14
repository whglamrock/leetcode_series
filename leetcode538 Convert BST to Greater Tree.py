
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):

        self.val = x
        self.left = None
        self.right = None


# idea: inorder traverse

class Solution(object):
    def convertBST(self, root):

        if not root: return
        self.inordertraversal = []
        self.vals = []

        def inorder(node):
            if node.left:
                inorder(node.left)
            self.inordertraversal.append(node)
            self.vals.append(node.val)
            if node.right:
                inorder(node.right)

        inorder(root)
        dic = {}
        for i in xrange(len(self.vals) - 2, -1, -1):
            self.vals[i] += self.vals[i + 1]
        for i, node in enumerate(self.inordertraversal):
            dic[node] = self.vals[i]

        todo = [root]
        while todo:
            next = []
            while todo:
                node = todo.pop()
                newval = dic[node]
                node.val = newval
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            todo = next

        return root