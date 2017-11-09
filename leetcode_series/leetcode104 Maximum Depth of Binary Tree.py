
class Solution(object):
    def maxDepth(self, root):

        if root is None:
            return 0
        queue = [root]
        ans = 0
        while queue:
            ans += 1
            level = []
            size = len(queue)
            for i in range(size):
                if queue[i].left != None:
                    level.append(queue[i].left)
                if queue[i].right != None:
                    level.append(queue[i].right)
            queue = level
        return ans



"""
# recursive solution

class Solution(object):
    def maxDepth(self, root):
        def dfs(level, root, res):
            if root:
                if level > res[0]:
                    res[0] = level
                dfs(level+1, root.left, res)
                dfs(level+1, root.right,res)
        res = [0]
        dfs(1, root, res)
        return res[0]
"""

