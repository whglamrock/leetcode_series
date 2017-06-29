
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):

        self.val = x
        self.left = None
        self.right = None


# the O(n) solution is to transfer the tree into strings and using KMP

class Solution(object):
    def isSubtree(self, s, t):

        def issame(root1, root2):

            if not root1 or not root2:
                return root1 == root2

            if root1.val != root2.val:
                return False

            return issame(root1.left, root2.left) and issame(root1.right, root2.right)

        todo = [s]
        while todo:
            node = todo.pop()
            if not node: continue
            if node.val == t.val and issame(node, t):
                    return True
            todo.append(node.left)
            todo.append(node.right)

        return False



'''
# O(N) KMP solution that borrows the code from lc28

class Solution(object):

    def isSubtree(self, s, t):

        # transfer the tree into string in preorder
        def preorderTraversal(root):

            if not root: return ''

            ans = []
            stack = [root]

            while stack:
                node = stack.pop()
                if not node:
                    ans.append('N')
                else:
                    ans.append(str(node.val))
                    stack.append(node.right)
                    stack.append(node.left)

            # it's necessary to add ',' to the head
            #   otherwise e.g.: s = [12], t = [2], then strings = 12,N,N
            #   stringt = 2,N,N (in this case we should return False
            #   but the "','.join(ans)" gives true eventually)
            return ',' + ','.join(ans)

        strings = preorderTraversal(s)
        stringt = preorderTraversal(t)
        return self.strStr(strings, stringt) != -1

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
'''