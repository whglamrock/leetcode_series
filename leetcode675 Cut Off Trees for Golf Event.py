
# a TLE but will definitely pass real interview's solution, simply translating from:
#   https://leetcode.com/problems/cut-off-trees-for-golf-event/discuss/107404/Java-solution-PriorityQueue-+-BFS

from collections import deque

class Solution(object):
    def cutOffTree(self, forest):

        # "impossible" edge case
        if not forest or not forest[0]:
            return -1

        # cut the tree in reverse order of tree's height
        treeList = []
        for i in xrange(len(forest)):
            for j in xrange(len(forest[0])):
                if forest[i][j] > 1:
                    treeList.append([forest[i][j], [i, j]])
        treeList.sort()  # will sort based on the first key

        totalSteps = self.minStep(forest, [0, 0], treeList[0][1])
        k = 0
        while k < len(treeList) - 1:
            step = self.minStep(forest, treeList[k][1], treeList[k + 1][1])
            if step == -1:
                return -1
            totalSteps += step
            k += 1

        return totalSteps

    # do BFS to see if we can find a path from start to end
    def minStep(self, forest, start, end):
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        step = 0
        m, n = len(forest), len(forest[0])
        visited = [[False for x in xrange(n)] for _ in xrange(m)]
        visited[start[0]][start[1]] = True
        queue = deque()
        queue.append(start)

        while queue:
            size = len(queue)
            for i in xrange(size):
                curr = queue.popleft()
                if curr == end:
                    return step
                for direction in directions:
                    nextRow = curr[0] + direction[0]
                    nextCol = curr[1] + direction[1]
                    if nextRow < 0 or nextRow >= m or nextCol < 0 or nextCol >= n or visited[nextRow][nextCol] or \
                                    forest[nextRow][nextCol] == 0:
                        continue
                    queue.append([nextRow, nextCol])
                    visited[nextRow][nextCol] = True
            step += 1

        # here, it means we can never find the destination
        return -1



Sol = Solution()
forest = [
 [1,2,3],
 [0,0,4],
 [7,6,5]
]
print Sol.cutOffTree(forest)


