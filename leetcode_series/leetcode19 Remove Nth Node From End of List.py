#!/usr/bin/python
# -*- coding: utf-8 -*-

class ListNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def setData(self, newData):
        self.data = newData

    def getNext(self):
        return self.next

    def setNext(self, nextNode):
        self.next = nextNode


class Solution(object):
    def removeNthFromEnd(self, head, n):
        counter = 0
        current = head
        while current.getNext() is not None:
            current = current.getNext()
            counter += 1
        counter += 1
        counterdown = 0
        current = head
        previous = None
        while counterdown < counter-n:
            previous = current
            current = current.getNext()
            counterdown += 1
        fku = current.next
        previous.setNext(fku)
        return head

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
a.setNext(b)
b.setNext(c)
c.setNext(d)

fk = Solution()
show = fk.removeNthFromEnd(a,2)

print show.next.next.getData()
