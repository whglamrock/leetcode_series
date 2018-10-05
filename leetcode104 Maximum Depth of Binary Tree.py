
class Solution(object):

    def maxDepth(self, root):

        if not root:
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
        self.length = 0
        def traverse(node, pathLength):
            if not node:
                self.length = max(self.length, pathLength)
                return
            traverse(node.left, pathLength + 1)
            traverse(node.right, pathLength + 1)
        
        traverse(root, 0)
        return self.length
"""

