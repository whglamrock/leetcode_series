
# O(R * C) BFS solution. We will have to use visited to avoid duplicate

class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        # first we need to find out the max distance
        maxDist = max(R - r0 - 1, r0 - 0) + max(C - c0 - 1, c0 - 0)

        ans = [[r0, c0]]
        visited = set()
        for dist in xrange(1, maxDist + 1):
            for i in xrange(dist + 1):
                j = dist - i
                if r0 - i >= 0 and c0 - j >= 0:
                    if (r0 - i, c0 - j) not in visited:
                        ans.append([r0 - i, c0 - j])
                        visited.add((r0 - i, c0 - j))
                if r0 + i < R and c0 - j >= 0:
                    if (r0 + i, c0 - j) not in visited:
                        ans.append([r0 + i, c0 - j])
                        visited.add((r0 + i, c0 - j))
                if r0 - i >= 0 and c0 + j < C:
                    if (r0 - i, c0 + j) not in visited:
                        ans.append([r0 - i, c0 + j])
                        visited.add((r0 - i, c0 + j))
                if r0 + i < R and c0 + j < C:
                    if (r0 + i, c0 + j) not in visited:
                        ans.append([r0 + i, c0 + j])
                        visited.add((r0 + i, c0 + j))

        return ans


