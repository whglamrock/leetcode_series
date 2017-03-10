
# clean DFS solution
#   the BFS version is nothing different but using "pop(0)"
# P.S., it's very important to know that the

class Solution(object):
    def hasPath(self, maze, start, destination):

        queue = [start]
        m, n = len(maze), len(maze[0])
        # remember this trick
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:

            # using "pop(0)" becomes a BFS!
            i, j = queue.pop()
            maze[i][j] = 2

            if [i, j] == destination:
                return True

            for x, y in dirs:
                row, col = i, j

                # the condition is "!= 1" not "== 0" because
                #   when it "== 2", we can still go through the stop point that we've been to
                while 0 <= row < m and 0 <= col < n and maze[row][col] != 1:
                    row += x
                    col += y

                # P.S. it is possible that the above while loop didn't even execute
                row -= x
                col -= y
                # so we need this check:
                if maze[row][col] == 0:
                    queue.append([row, col])

        return False
