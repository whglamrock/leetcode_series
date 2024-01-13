
# A realistic BFS approach that you can think of in real interview.
# For crazy O(1) solution: https://leetcode.com/problems/minimum-knight-moves/solutions/392053/here-is-how-i-get-the-formula-with-graphs/
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)
        todo = {(0, 0)}
        visited = {(0, 0)}
        step = 0
        directions = [[-1, 2], [-2, 1], [-1, -2], [-2, -1], [1, 2], [2, 1], [2, -1], [1, -2]]

        while todo:
            nextTodo = set()
            for i, j in todo:
                if i == x and j == y:
                    return step

                for deltaI, deltaJ in directions:
                    ii, jj = i + deltaI, j + deltaJ
                    # x, y are already positive so we don't need to go left/down farther than -1
                    if (ii, jj) not in visited and ii >= -1 and jj >= -1:
                        visited.add((ii, jj))
                        nextTodo.add((ii, jj))
            todo = nextTodo
            step += 1

        return step


'''
from functools import lru_cache

# same time complexity but faster "dp" approach with memoization
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        
        @lru_cache(None) 
        def dp(x,y):
            if x + y == 0:
                return 0
            elif x + y == 2:
                return 2
            return min(dp(abs(x - 1), abs(y - 2)), dp(abs(x - 2), abs(y - 1))) + 1
        
        return dp(abs(x), abs(y))
'''