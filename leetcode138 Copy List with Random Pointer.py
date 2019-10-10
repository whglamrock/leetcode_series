
# Definition for a Node.

class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random



# See O(1) space solution: https://leetcode.com/problems/copy-list-with-random-pointer/discuss/43689/Python-solution-without-using-dictionary.
    # The idea is modify the original list to make node.copy.next = node.next & node.next = node_copy, so the oldToNew
    # mapping is represented in a different way
# In real interview, we just need to mention the idea of O(1) space solution to qualify the strong hire

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        oldToNew = {}
        pOld = head
        dummy = Node(None, None, None)
        pNew = dummy

        while pOld:
            node = Node(pOld.val, None, None)
            oldToNew[pOld] = node

            pNew.next = node
            pNew = pNew.next
            pOld = pOld.next

        pNew = dummy.next
        pOld = head
        while pOld:
            if pOld.random:
                pNew.random = oldToNew[pOld.random]
            pOld = pOld.next
            pNew = pNew.next

        return dummy.next



