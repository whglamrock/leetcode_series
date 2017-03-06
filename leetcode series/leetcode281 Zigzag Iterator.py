# in fact, pop(0) is very time consuming.
class ZigzagIterator(object):

    def __init__(self, v1, v2):

        v1.reverse()
        v2.reverse()
        self.queue = []
        while v1 and v2:
            self.queue.append(v1.pop())
            self.queue.append(v2.pop())
        if v1:
            while v1:
                self.queue.append(v1.pop())
        else:
            while v2:
                self.queue.append(v2.pop())
        self.queue.reverse()

    def next(self):

        return self.queue.pop()

    def hasNext(self):

        return len(self.queue) != 0

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())