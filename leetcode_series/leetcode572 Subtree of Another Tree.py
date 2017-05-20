
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):

        self.val = x
        self.left = None
        self.right = None


# the O(n) solution is to transfer the tree into strings and using KMP

class Solution(object):
    def isSubtree(self, s, t):

        def compare(root1, root2):

            if not root1 or not root2:
                return root1 == root2
            if root1.val != root2.val:
                return False

            leftans = compare(root1.left, root2.left)
            rightans = compare(root1.right, root2.right)
            return leftans and rightans

        self.flag = False
        def traverse(root, roottobecompared):

            if not root:
                return
            if compare(root, roottobecompared):
                self.flag = True
                return

            traverse(root.left, roottobecompared)
            traverse(root.right, roottobecompared)

        traverse(s, t)
        return self.flag



'''
# O(N) KMP solution that borrows the code from lc28

class Solution(object):

    def isSubtree(self, s, t):

        strs = self.serialize(s)
        strt = self.serialize(t)

        #print strs
        #print strt
        return self.strStr(strs, strt) != -1

    def ComputePrefixFunction(self, needle):

        pat = [0] * len(needle)
        # j is the prefix pointer, i is the suffix pointer
        j, i = 0, 1
        while i < len(needle):
            #print j, i
            if needle[i] == needle[j]:
                pat[i] = j + 1
                i += 1
                j += 1
            elif j == 0:
                pat[i] = 0
                i += 1
            else:
                j = pat[j - 1]

        return pat

    def strStr(self, haystack, needle):

        if (not needle) or len(needle) == 0:
            return 0
        if (not haystack) or len(haystack) < len(needle):
            return -1

        n = len(haystack)
        m = len(needle)
        # at this time, i is the haystack pointer, j is the needle pointer
        i, j = 0, 0
        pat = self.ComputePrefixFunction(needle)
        while i < len(haystack) and j < len(needle):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == len(needle):
                    return i - j
            elif j == 0:
                i += 1
            else:
                j = pat[j - 1]

        return -1

    # the serialization code from lc297 needs to be changed into preorder
    def serialize(self, root):

        if not root:
            return ''
        todo = [root]
        ans = []
        while todo:
            node = todo.pop()
            if not node:
                ans.append('N')
            else:
                ans.append(str(node.val))
                todo.append(node.right)
                todo.append(node.left)

        return ',' + ','.join(ans)
'''