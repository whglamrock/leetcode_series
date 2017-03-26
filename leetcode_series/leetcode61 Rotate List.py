
# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):

        self.val = x
        self.next = None


# understand the definition of 'Rotate' is very important: e.g., original linked list
# is 1->2->3->4->5, k=2; It means operating 'take the last one off and put it before the head' k times.
# i.e., it goes through: 1)5->1->2->3->4; 2)4->5->1->2->3.

class Solution(object):
    def rotateRight(self, head, k):

        if (not head):
            return

        count, findend = 0, head
        while findend and findend.next:
            count += 1
            findend = findend.next

        count += 1
        k %= count  # k could be bigger than the list length.
        if k == 0:
            return head

        connect, newhead = head, head
        for i in xrange(count-k-1): # connect will be the new tail
            connect = connect.next
            newhead = newhead.next
        newhead = newhead.next    # new tail's 'old next' is new head, which we need to return

        findend.next = head    # old tail's next becomes old head
        connect.next = None

        return newhead