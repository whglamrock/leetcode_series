
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = {(0, 0)}
        x, y = 0, 0
        for char in path:
            if char == 'N':
                x -= 1
            elif char == 'S':
                x += 1
            elif char == 'E':
                y += 1
            else:
                y -= 1
            if (x, y) in visited:
                return True
            visited.add((x, y))

        return False
