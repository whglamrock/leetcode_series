class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Solution without knowing the length
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        ptA, ptB, jumpA = headA, headB, False
        while True:
            if ptA == ptB:
                return ptA
            ptA, ptB = ptA.next, ptB.next
            if not ptA:
                if not jumpA:
                    jumpA = True
                    ptA = headB
                else:
                    return None
            if not ptB:
                ptB = headA


a = ListNode(1)
b = ListNode(3)
c = ListNode(5)
d = ListNode(7)
e = ListNode(9)
f = ListNode(11)

g = ListNode(2)
h = ListNode(4)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

g.next = h
h.next = e


i = ListNode(10)
i.next = f

Sol = Solution()
final = Sol.getIntersectionNode(g,a)
print final.val


'''
# Another simple solution with length
class Solution(object):
    def getIntersectionNode(self, headA, headB):

        tmpA, tmpB = headA, headB
        lenA, lenB = 0, 0
        while tmpA:
            tmpA = tmpA.next
            lenA += 1
        while tmpB:
            tmpB = tmpB.next
            lenB += 1

        while lenA > lenB:
            lenA -= 1
            headA = headA.next

        while lenB > lenA:
            lenB -= 1
            headB = headB.next

        if headA == headB: return headA

        while (headA != None and headB != None) and headA != headB:
            headA = headA.next
            headB = headB.next

        return headA
'''








