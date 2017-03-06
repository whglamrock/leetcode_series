# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        self.dick = []
        def helper(node):
            new = [str(node.val)]
            if node.left:
                new.append(str(node.left.val))
            else:
                new.append('N')
            if node.right:
                new.append(str(node.right.val))
            else:
                new.append('N')
            self.dick.append(','.join(new))
            if node.left: helper(node.left)
            if node.right: helper(node.right)

        helper(root)
        return '/'.join(self.dick)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None
        elif data.isdigit():
            return TreeNode(int(data))
        elif data.startswith('-') and data[1:].isdigit():
            return TreeNode(int(data))

        self.dick = data.split('/')
        self.dic = {}
        rootval = None
        for i in xrange(len(self.dick)):
            parent, lchild, rchild = self.dick[i].split(',')
            if i == 0:
                rootval = int(parent)
            self.dic[int(parent)] = [lchild, rchild]

        root = TreeNode(rootval)
        def helper(node):
            if node.val not in self.dic:
                return
            l, r = self.dic[node.val]
            if l.isdigit():
                newleft = TreeNode(int(l))
                node.left = newleft
                helper(newleft)
            if r.isdigit():
                newright = TreeNode(int(r))
                node.right = newright
                helper(newright)

        helper(root)
        return root



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))