# if it doesn't go back to original position, the final direction cannot be north
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        angle = 0
        direction = 'N'
        nextDirectionWithLeftTurn = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}
        nextDirectionWithRightTurn = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
        deltaX, deltaY = 0, 0
        for char in instructions:
            if char == 'G':
                if direction == 'N':
                    deltaY += 1
                elif direction == 'S':
                    deltaY -= 1
                elif direction == 'E':
                    deltaX += 1
                else:
                    deltaX -= 1
            elif char == 'L':
                angle -= 90
                direction = nextDirectionWithLeftTurn[direction]
            else:
                angle += 90
                direction = nextDirectionWithRightTurn[direction]
        angle = abs(angle) % 360

        return deltaX == deltaY == 0 or angle != 0


print(Solution().isRobotBounded("GLRLLGLL"))
print(Solution().isRobotBounded("GL"))
print(Solution().isRobotBounded("GG"))
print(Solution().isRobotBounded("GGLLGG"))
