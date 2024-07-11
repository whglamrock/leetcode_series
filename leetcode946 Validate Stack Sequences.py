from collections import deque
from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        pushed, popped = deque(pushed), deque(popped)
        stack = []
        while pushed:
            while not stack or stack[-1] != popped[0]:
                if not pushed:
                    break
                stack.append(pushed.popleft())

            while stack and popped and stack[-1] == popped[0]:
                stack.pop()
                popped.popleft()

        return len(stack) == 0
