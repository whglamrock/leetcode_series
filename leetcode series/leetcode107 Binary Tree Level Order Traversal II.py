class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        ans = []
        queue = [root]
        while queue:
            level = []
            nextlevel = []
            size = len(queue)
            for i in range(size):
                if queue[i].left != None:
                    nextlevel.append(queue[i].left)
                if queue[i].right != None:
                    nextlevel.append(queue[i].right)
                level.append(queue[i].val)
            ans.append(level)
            queue = nextlevel

        ans.reverse()
        return ans

