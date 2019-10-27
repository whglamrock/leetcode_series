
# a DFS solution that's most realistic to be given in interview

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        self.ans = True
        self.dfs(root)
        return self.ans

    def dfs(self, root):
        lo, hi = root.val, root.val
        if root.left:
            leftLo, leftHi = self.dfs(root.left)
            lo, hi = min(lo, leftLo), max(hi, leftHi)
            if not leftHi < root.val:
                self.ans = False
        if root.right:
            rightLo, rightHi = self.dfs(root.right)
            lo, hi = min(lo, rightLo), max(hi, rightHi)
            if not rightLo > root.val:
                self.ans = False
        return lo, hi