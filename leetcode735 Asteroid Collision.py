from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            else:
                # pop out the smaller positive asteroids
                while stack and stack[-1] > 0 and abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                # pop out the equal one exactly once
                if stack and stack[-1] == -asteroid:
                    stack.pop()
                else:
                    if not stack or stack[-1] < 0:
                        stack.append(asteroid)

        return stack
