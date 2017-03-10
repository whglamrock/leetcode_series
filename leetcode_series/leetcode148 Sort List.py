# normally use merge sort. Get familiar with 'merge sort'!
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# iterative solution with O(1) space.
class Solution(object):
    def split(self, head, n):

        for i in xrange(1,n):
            if head:
                head = head.next

        if (not head):
            return None
        second = head.next
        head.next = None    # very import, this step splits the original list
        return second

    def merge(self, l1, l2, head):

        cur = head
        while l1 and l2:
            if l1.val > l2.val:
                cur.next = l2
                cur = cur.next
                l2 = l2.next
            else:
                cur.next = l1
                cur = cur.next
                l1 = l1.next

        cur.next = l1 or l2
        while cur and cur.next:
            cur = cur.next

        return cur

    def sortList(self, head):

        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next

        dummy = ListNode(0)
        dummy.next = head
        step = 1

        while step < length:
            cur = dummy.next
            tail = dummy
            while cur:  # while step == 1, sort every pair in list (e.g., for [5,4,2,1,3], it
                # will become [4,5, 1,2, 3]). while step == 2, it will sort every block (contains
                # 4 elements, in our case, [1,2,4,5, 3]... so on and so forth)
                left = cur
                right = self.split(left, step)
                cur = self.split(right, step)
                tail = self.merge(left, right, tail)
            step <<= 1

        return dummy.next


a = ListNode(5)
b = ListNode(4)
c = ListNode(2)
d = ListNode(1)
e = ListNode(3)
a.next = b
b.next = c
c.next = d
d.next = e
Sol = Solution()
ans = Sol.sortList(a)
while ans:
    print ans.val
    ans = ans.next


'''
# recursive solution
class Solution(object):
    def sortList(self, head):

        if (not head) or (not head.next):
            return head

        prev, slow, fast = ListNode(None), head, head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None

        l1 = self.sortList(head)    # recursive so in next loop the new 'head/slow' will split
        l2 = self.sortList(slow)    # into 2. It goes on and on.

        return self.merge(l1, l2)

    def merge(self, l1, l2):

        l = ListNode(0)
        p = l

        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next

        if l1:
            p.next = l1
        else:
            p.next = l2

        return l.next
'''


