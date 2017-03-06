# seems there is no O(1) space solution without changing the preorder.
# O(1) solution from here: https://discuss.leetcode.com/topic/21217/java-o-n-and-o-1-extra-space/2
# O(logn) space solution is keeping a stack, while not changing the preorder.

# the idea is using original list preorder as a stack, and the elements in stack need to
# be in descending order.
# P.S. Invalid BST could have same preorder traversal as valid BST's.

class Solution(object):
    def verifyPreorder(self, preorder):

        if not preorder: return True
        # no need to check duplicates

        curmin = -2147483648
        i = -1

        for p in preorder:
            if p < curmin:
                return False
            while i >= 0 and p > preorder[i]:
                curmin = preorder[i]
                i -= 1
            i += 1
            preorder[i] = p

        return True



'''
# Solution without changing preorder

class Solution(object):
    def verifyPreorder(self, preorder):

        if (not preorder): return True

        curmin = -2147483648
        stack = []

        for p in preorder:
            if p < curmin:
                return False
            while stack and p > stack[-1]:
                curmin = stack.pop()
            stack.append(p)

        return True
'''
