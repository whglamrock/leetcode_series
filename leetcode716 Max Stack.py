from heapq import *


# Remember the below solution (using a decreasingId + "soft delete").
# Using sortedcontainers' SortedList is more error prone.
class MaxStack:
    def __init__(self):
        self.softDeleted = set()
        self.maxHeap = []
        self.stack = []
        self.currId = 0

    def push(self, x: int) -> None:
        heappush(self.maxHeap, [-x, self.currId])
        self.stack.append([x, self.currId])
        self.currId -= 1

    def pop(self) -> int:
        lastVal, lastId = self.stack.pop()
        self.softDeleted.add(lastId)
        self.cleanUp()
        return lastVal

    def top(self) -> int:
        return self.stack[-1][0]

    def peekMax(self) -> int:
        return -self.maxHeap[0][0]

    def popMax(self) -> int:
        maxVal, maxId = heappop(self.maxHeap)
        maxVal = -maxVal
        self.softDeleted.add(maxId)
        self.cleanUp()
        return maxVal

    def cleanUp(self):
        while self.stack and self.stack[-1][1] in self.softDeleted:
            self.softDeleted.discard(self.stack.pop()[1])
        while self.maxHeap and self.maxHeap[0][1] in self.softDeleted:
            self.softDeleted.discard(heappop(self.maxHeap)[1])


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
