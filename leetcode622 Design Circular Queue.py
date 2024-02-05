
class MyCircularQueue:
    def __init__(self, k: int):
        self.k = k
        self.queue = [-1] * k
        self.firstIndex, self.currIndex = 0, 0
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.size == self.k:
            return False

        self.queue[self.currIndex] = value
        self.currIndex += 1
        self.currIndex %= self.k
        self.size += 1

        return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False

        self.queue[self.firstIndex] = -1
        self.size -= 1
        self.firstIndex += 1
        self.firstIndex %= self.k
        return True

    def Front(self) -> int:
        return self.queue[self.firstIndex]

    def Rear(self) -> int:
        return self.queue[self.currIndex - 1]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
