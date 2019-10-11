
# The idea is also appending the currMin along with the new value. This way we can achieve O(1) with getMin().
# Because the minStack can only "pop" not remove a specific value,
    # when we pop the last element the previous min becomes the current min

class MinStack(object):

    def __init__(self):

        self.q = []

    def push(self, x):

        if (not self.q):
            self.q.append([x, x])
        else:
            if x < self.getMin():
                self.q.append([x, x])
            else:
                self.q.append([x, self.q[-1][1]])

    def pop(self):

        self.q.pop()

    def top(self):

        return self.q[-1][0]


    def getMin(self):

        return self.q[-1][1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()