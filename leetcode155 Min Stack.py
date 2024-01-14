class MinStack:
    def __init__(self):
        self.currMin = None
        self.mins = []
        self.stack = []

    def push(self, val: int) -> None:
        if self.currMin is None:
            self.currMin = val
        else:
            self.currMin = min(self.currMin, val)
        self.stack.append(val)
        self.mins.append(self.currMin)

    def pop(self) -> None:
        if not self.stack:
            return
        self.stack.pop()
        self.mins.pop()
        if self.mins:
            self.currMin = self.mins[-1]
        else:
            self.currMin = None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.currMin


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
