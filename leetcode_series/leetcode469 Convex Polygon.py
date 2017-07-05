
# no need to worry about the order of points
#   because the description said join them sequentially
# remember the mathematical meaning of crossproduct

class Solution(object):
    def isConvex(self, points):

        if not points:
            return False

        n = len(points)
        positive = False
        negative = False

        # notice the order of Ax/Ay, Bx/By, Cx/Cy
        def getcrossproduct(Ax, Ay, Bx, By, Cx, Cy):
            ABx, ABy = Bx - Ax, By - Ay
            BCx, BCy = Cx - Bx, Cy - By
            return ABx * BCy - ABy * BCx

        for i in xrange(n):
            j, k = (i + 1) % n, (i + 2) % n
            A, B, C = points[i], points[j], points[k]
            Ax, Ay, Bx, By, Cx, Cy = A[0], A[1], B[0], B[1], C[0], C[1]
            thecrossproduct = getcrossproduct(Ax, Ay, Bx, By, Cx, Cy)
            if thecrossproduct == 0:
                continue
            elif thecrossproduct > 0:
                positive = True
            else:
                negative = True
            if positive and negative:
                return False

        return True



points = [[0, 0], [0, 1], [1, 1], [1, 0]]
Sol = Solution()
print Sol.isConvex(points)
