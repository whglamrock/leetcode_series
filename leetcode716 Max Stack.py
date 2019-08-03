
# Tradeoff has to be made between O(n) & O(logN) solution.
# The O(logN) solution may be more troublesome because every time you pop stack you have to update the heap as well

class MaxStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        return self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def peekMax(self):
        """
        :rtype: int
        """
        return max(self.stack)

    def popMax(self):
        """
        :rtype: int
        """
        maxNum = max(self.stack)
        maxIndex = len(self.stack) - 1
        while self.stack[maxIndex] != maxNum:
            maxIndex -= 1
        del self.stack[maxIndex]
        return maxNum



        # Your MaxStack object will be instantiated and called as such:
        # obj = MaxStack()
        # obj.push(x)
        # param_2 = obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.peekMax()
        # param_5 = obj.popMax()