
from collections import deque
from copy import copy

class SnakeGame(object):

    def __init__(self, width, height, food):

        self.width = width
        self.height = height
        self.food = set()
        self.foodorder = deque(copy(food))
        for foodposition in food:
            self.food.add((foodposition[0], foodposition[1]))
        self.snake = deque()
        self.snake.append([0, 0])
        self.body = {(0, 0)}

    def check(self, nextposition):
        y, x = nextposition[0], nextposition[1]
        if (y, x) in self.body:
            return False
        if x < 0 or x >= self.width:
            return False
        if y < 0 or y >= self.height:
            return False
        return True

    def move(self, direction):

        head = self.snake[0]
        if direction == 'L':
            nextposition = [head[0], head[1] - 1]
        elif direction == 'R':
            nextposition = [head[0], head[1] + 1]
        elif direction == 'U':
            nextposition = [head[0] - 1, head[1]]
        else:
            nextposition = [head[0] + 1, head[1]]

        dump = self.snake.pop()
        self.body.remove((dump[0], dump[1]))
        if (not self.check(nextposition)): return -1
        if (nextposition[0], nextposition[1]) in self.food and (self.foodorder and nextposition == self.foodorder[0]):
            self.snake.append(dump)
            self.body.add((dump[0], dump[1]))
            self.food.remove((nextposition[0], nextposition[1]))
            self.foodorder.popleft()
        self.snake.appendleft(nextposition)
        self.body.add((nextposition[0], nextposition[1]))
        return len(self.snake) - 1



# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)