# this fking stupid question doesn't make any sense at all.
class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []


    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.append(x)



    def pop(self):
        """
        :rtype: nothing
        """
        self.stack.reverse()
        self.stack.pop(0)
        self.stack.reverse()


    def top(self):
        """
        :rtype: int
        """
        self.stack.reverse()
        ans = self.stack[0]
        self.stack.reverse()
        return ans


    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack) == 0