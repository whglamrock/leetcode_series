
class ListNode(object):
    def __init__(self, x):

        self.val = x
        self.next = None


# leetcode time limit is tight for python...
# idea: build a new sorted list and return the newhead

class Solution(object):
    def insertionSortList(self, head):

        newhead = ListNode(None)
        if (not head):
            return None
        else:
            newhead.val = head.val
            tail = newhead    # tail is set to track down the new final tail
        head = head.next

        while head:
            find = ListNode(None)
            find.next = newhead
            if head.val >= tail.val:    # quick comparison to avoid TLE for sick case like [0,1,2,3,...4998,4999]
                find = tail
            else:    # find the insertion location: after this, we need to implement 'find.next = add'.
                while find.next and find.next.val <= head.val:  # it's '<=' rather than '<'. e.g., for case [4,4,2,5],
                    find = find.next  # when newhead.val == the first 4, we need find == newhead instead of
                                      # find.next = newhead.
            add = ListNode(head.val)
            if add.val < newhead.val:  # it's '<' rather than '<='. Otherwise, for the above case, when add.val ==
                newhead = add  # newhead.val == 4, the newhead will be changed and the newlist will be [4]
                               # after the following operations.
            add.next = find.next
            find.next = add
            head = head.next
            while tail and tail.next:
                tail = tail.next

        return newhead