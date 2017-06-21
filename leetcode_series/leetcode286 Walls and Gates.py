
# classic recursive BFS solution

class Solution(object):
    def wallsAndGates(self, a):

        for i in xrange(len(a)):
            for j in xrange(len(a[0])):
                if a[i][j] == 0:
                    stack = [
                        (i + 1, j, 1),
                        (i - 1, j, 1),
                        (i, j + 1, 1),
                        (i, j - 1, 1)
                    ]
                    while stack:
                        ii, jj, dist = stack.pop()
                        if ii < 0 or jj < 0 or ii >= len(a) or jj >= len(a[0]) or a[ii][jj] < dist:
                            continue
                        a[ii][jj] = dist
                        stack.append((ii + 1, jj, dist + 1))
                        stack.append((ii - 1, jj, dist + 1))
                        stack.append((ii, jj + 1, dist + 1))
                        stack.append((ii, jj - 1, dist + 1))

        #return a   # the stupid leetcode asks to return nothing



'''
# recursive BFS solution
# it's really interesting that this solution will get TLE if the bfs is not written
#   as a global method

class Solution(object):
    def wallsAndGates(self, rooms):

        if not rooms or not rooms[0]:
            return

        for i in xrange(len(rooms)):
            for j in xrange(len(rooms[0])):
                if rooms[i][j] == 0:
                    self.bfs(rooms, i, j, 0)

    def bfs(self, rooms, i, j, currdist):

        if i < 0 or i >= len(rooms) or j < 0 or j >= len(rooms[0]) or rooms[i][j] < currdist:
            return
        else:
            rooms[i][j] = currdist
            self.bfs(rooms, i - 1, j, currdist + 1)
            self.bfs(rooms, i + 1, j, currdist + 1)
            self.bfs(rooms, i, j - 1, currdist + 1)
            self.bfs(rooms, i, j + 1, currdist + 1)
'''

