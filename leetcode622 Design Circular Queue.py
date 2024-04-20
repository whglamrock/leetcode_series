class MyCircularQueue:
    def __init__(self, k: int):
        self.size = 0
        self.firstIndex, self.currIndex = 0, 0
        self.nums = [-1] * k

    def enQueue(self, value: int) -> bool:
        if self.size == len(self.nums):
            return False

        self.nums[self.currIndex] = value
        self.currIndex += 1
        self.currIndex %= len(self.nums)
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False

        self.nums[self.firstIndex] = - 1
        self.firstIndex += 1
        self.firstIndex %= len(self.nums)
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.size == 0:
            return -1
        return self.nums[self.firstIndex]

    def Rear(self) -> int:
        if self.size == 0:
            return -1
        return self.nums[self.currIndex - 1]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == len(self.nums)


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
