
# this fking stupid question doesn't make any sense at all.

class Stack(object):
    def __init__(self):

        self.stack = []

    def push(self, x):

        self.stack.append(x)

    def pop(self):

        self.stack.reverse()
        self.stack.pop(0)
        self.stack.reverse()

    def top(self):

        self.stack.reverse()
        ans = self.stack[0]
        self.stack.reverse()
        return ans

    def empty(self):

        return len(self.stack) == 0