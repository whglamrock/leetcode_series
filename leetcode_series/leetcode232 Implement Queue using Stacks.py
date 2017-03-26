
# this fking stupid question doesn't make any sense at all.

class Queue(object):
    def __init__(self):

        self.queue = []

    def push(self, x):

        self.queue.append(x)

    def pop(self):

        self.queue.reverse()
        self.queue.pop()
        self.queue.reverse()

    def peek(self):

        self.queue.reverse()
        ans = self.queue[-1]
        self.queue.reverse()
        return ans

    def empty(self):

        return len(self.queue) == 0