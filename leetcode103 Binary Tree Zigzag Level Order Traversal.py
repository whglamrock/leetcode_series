
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        ans = []
        level = 0
        curr = [root]

        while curr:
            next = []
            levelTraversal = []
            for node in curr:
                levelTraversal.append(node.val)
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            if level % 2 == 0:
                ans.append(levelTraversal)
            else:
                ans.append(levelTraversal[::-1])
            level += 1
            curr = next

        return ans