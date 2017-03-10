class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# O(1) space solution.
class Solution(object):
    def reorderList(self, head):

        if not head:
            return

        # find the mid point
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half in-place
        pre, node = None, slow
        while node:
            pre, node.next, node = node, pre, node.next

        # Merge in-place; Note : the last node of "first" and "second" are the same
        first, second = head, pre
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next

        # the lc asks for returning nothing


'''
# my original inefficient solution with O(n) running time/space.
class Solution(object):
    def reorderList(self, head):

        if (not head) or (not head.next):
            return

        travel = head
        counter = 0
        while travel:
            counter += 1
            travel = travel.next

        find = head
        for i in xrange(counter/2):
            find = find.next

        store = find.next
        save = []
        while store:
            save.append(store)
            store = store.next

        ans = head
        while save:
            new = save.pop()
            new.next = head.next
            head.next = new
            head = new.next
        find.next = None

        head = ans
'''

