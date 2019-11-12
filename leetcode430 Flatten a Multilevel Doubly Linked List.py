
# Definition for a Node.

class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child



class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head

        stack = [head]
        ans = []

        while stack:
            node = stack.pop()
            ans.append(node)
            if node.next:
                stack.append(node.next)
            if node.child:
                stack.append(node.child)

        for i in xrange(len(ans) - 1):
            node = ans[i]
            nextNode = ans[i + 1]
            node.child, nextNode.child = None, None
            node.next = nextNode
            nextNode.prev = node

        return ans[0]
