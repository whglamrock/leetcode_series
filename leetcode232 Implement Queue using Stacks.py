
# The description asks for using 2 stacks, although there are plenty of other ways to solve it (e.g., doubly linked list).
class MyQueue:
    def __init__(self):
        self.inStack, self.outStack = [], []

    def push(self, x: int) -> None:
        self.inStack.append(x)

    def pop(self) -> int:
        self.move()
        return self.outStack.pop()

    def peek(self) -> int:
        self.move()
        return self.outStack[-1]

    def empty(self) -> bool:
        return len(self.outStack) == 0 and len(self.inStack) == 0

    def move(self):
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
