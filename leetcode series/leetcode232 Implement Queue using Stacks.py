# this fking stupid question doesn't make any sense at all.
class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue = []


    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.queue.append(x)


    def pop(self):
        """
        :rtype: nothing
        """
        self.queue.reverse()
        self.queue.pop()
        self.queue.reverse()


    def peek(self):
        """
        :rtype: int
        """
        self.queue.reverse()
        ans = self.queue[-1]
        self.queue.reverse()
        return ans


    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue) == 0