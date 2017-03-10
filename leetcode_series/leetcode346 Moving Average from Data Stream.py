class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.inside = 0
        self.sum = []


    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if self.inside < self.size:
            self.sum.append(val)
            self.inside += 1
        else:
            self.sum.pop(0)
            self.sum.append(val)

        return float(sum(self.sum))/self.inside


movavg = MovingAverage(3)
print movavg.next(4)
print movavg.next(100)
print movavg.next(-10)
print movavg.next(-300)




# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)