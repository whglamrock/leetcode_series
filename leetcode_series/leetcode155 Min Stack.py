'''
Every element in the stack stores a tuple(in "list" structure) that contains the newly pushed x and current min.
If newly pushed x is still more that current min, the newly added tuple will store the new "x" and old min;
Otherwise, it will store "[x,x]". Thus, the last tuple[1] will always be the current min.
'''
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if (not self.q):
            self.q.append([x,x])
        else:
            if x < self.getMin():
                self.q.append([x,x])
            else:
                self.q.append([x,self.q[-1][1]])

    def pop(self):
        """
        :rtype: void
        """
        self.q.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.q[-1][0]


    def getMin(self):
        """
        :rtype: int
        """
        return self.q[-1][1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()