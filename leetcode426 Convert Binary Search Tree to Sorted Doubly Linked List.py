
# Definition for a Node.

class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right



class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return

        # find the smallest node as the return value
        head, tail = self.dfs(root)
        tail.right = head
        head.left = tail

        return head

    def dfs(self, node):
        head, tail = node, node
        if node.left:
            prevHead, prevTail = self.dfs(node.left)
            head = prevHead
            prevTail.right = node
            node.left = prevTail
        if node.right:
            nextHead, nextTail = self.dfs(node.right)
            tail = nextTail
            nextHead.left = node
            node.right = nextHead

        return head, tail