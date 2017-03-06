class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        queue = [root]
        ans = []
        counter = 0
        while queue:
            level = []
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                level.append(node.val)
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            if counter%2 == 0:
                ans.append(level)
            else:
                level.reverse()
                ans.append(level)
            counter += 1
        return ans