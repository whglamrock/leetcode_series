
# basic idea is: the amount of trapped water is decided by the shortest wall around it
#   so put the heights in a min priorityqueue and the newly popped height will be taller than
#   all previously popped ones. Then the height difference cna be directly added the amount of trapped
#   water.

from heapq import *
class Solution(object):
    def trapRainWater(self, heightMap):

        if not heightMap or len(heightMap[0]) == 0:
            return 0

        pq = []
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False for j in xrange(n)] for i in xrange(m)]

        for i in xrange(m):
            visited[i][0], visited[i][-1] = True, True
            heappush(pq, [heightMap[i][0], (i, 0)])
            heappush(pq, [heightMap[i][-1], (i, n - 1)])

        for j in xrange(1, n - 1):
            visited[0][j], visited[-1][j] = True, True
            heappush(pq, [heightMap[0][j], (0, j)])
            heappush(pq, [heightMap[-1][j], (m - 1, j)])

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        res = 0

        while pq:
            cell = heappop(pq)
            for x, y in dirs:
                row, col = cell[1][0] + x, cell[1][1] + y
                if 0 <= row < m and 0 <= col < n and (not visited[row][col]):
                    visited[row][col] = True
                    res += max(0, cell[0] - heightMap[row][col])
                    # re-add the "filled" cell, change the height at (row, col)
                    heappush(pq, [max(cell[0], heightMap[row][col]), (row, col)])

        return res



Sol = Solution()
heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
print Sol.trapRainWater(heightMap)



'''
# java version

import java.util.*;
import java.lang.Math;

public class Solution {

    public class Cell implements Comparable<Cell> {

        int row;
        int col;
        int height;

        public Cell (int row, int col, int height) {
            this.row = row;
            this.col = col;
            this.height = height;
        }

        public int compareTo(Cell o) {
            return this.height - o.height;
        }
    }

    public int trapRainWater(int[][] heightMap) {

        if (heightMap == null || heightMap.length <= 2 || heightMap[0].length <= 2) {
            return 0;
        }

        // the compareTo method has already been pre-defined
        PriorityQueue<Cell> pq = new PriorityQueue<Cell> (1);
        int m = heightMap.length;
        int n = heightMap[0].length;

        boolean[][] visited = new boolean[m][n];
        for (boolean[] visitedrow: visited) {
            Arrays.fill(visitedrow, false);
        }

        for (int i = 0; i < m; i++) {
            visited[i][0] = true;
            visited[i][n - 1] = true;
            pq.offer(new Cell(i, 0, heightMap[i][0]));
            pq.offer(new Cell(i, n - 1, heightMap[i][n - 1]));
        }

        for (int j = 0; j < n; j++) {
            visited[0][j] = true;
            visited[m - 1][j] = true;
            pq.offer(new Cell(0, j, heightMap[0][j]));
            pq.offer(new Cell(m - 1, j, heightMap[m - 1][j]));
        }

        int[][] dirs = new int[][] {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        int res = 0;
        while (!pq.isEmpty()) {
            Cell cell = pq.poll();
            for (int[] dir: dirs) {
                int row = cell.row + dir[0];
                int col = cell.col + dir[1];
                if (row >= 0 && row < m && col >= 0 && col < n && !visited[row][col]) {
                    visited[row][col] = true;
                    res += Math.max(0, cell.height - heightMap[row][col]);
                    pq.offer(new Cell(row, col, Math.max(cell.height, heightMap[row][col])));
                }
            }
        }

        return res;
    }
}
'''