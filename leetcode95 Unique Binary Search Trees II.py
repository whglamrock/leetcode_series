
class TreeNode(object):
    def __init__(self, x):

        self.val = x
        self.left = None
        self.right = None


# the 'divide and conquer' idea came from:
# https://discuss.leetcode.com/topic/8398/dp-solution-in-6-lines-with-explanation-f-i-n-g-i-1-g-n-i

class Solution(object):
    def generateSubtrees(self, s, e):

        res = []
        if s > e:   # when the recursion hits the bottom
            res.append(None)
            return res

        for i in xrange(s, e+1):
            leftSubtrees = self.generateSubtrees(s, i - 1)
            rightSubtrees = self.generateSubtrees(i + 1, e)
            for l in leftSubtrees:
                for r in rightSubtrees:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    res.append(root)

        return res

    def generateTrees(self, n):

        if n == 0:
            return []

        return self.generateSubtrees(1, n)



Sol = Solution()
ans = Sol.generateTrees(3)
for item in ans:
    print item.val