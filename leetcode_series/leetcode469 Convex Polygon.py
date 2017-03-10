
# no need to worry about the order of points
#   because the description said join them sequentially

class Solution(object):
    def isConvex(self, points):

        n = len(points)
        go_positive = False
        go_negative = False

        # assume the point B is one in the middle
        def getcrossproduct(Ax, Ay, Bx, By, Cx, Cy):

            ABx = Ax - Bx
            ABy = Ay - By
            BCx = Bx - Cx
            BCy = By - Cy

            return BCx * ABy - BCy * ABx

        for i in xrange(n):

            j, k = (i + 1) % n, (i + 2) % n
            A, B, C = points[i], points[j], points[k]
            Ax, Ay, Bx, By, Cx, Cy = A[0], A[1], B[0], B[1], C[0], C[1]
            crossproduct = getcrossproduct(Ax, Ay, Bx, By, Cx, Cy)

            # crossproduct == 0 should be treated as a neutral senario
            #   which can be "both" positve and nagative
            if crossproduct > 0:
                go_positive = True
            elif crossproduct < 0:
                go_negative = True
            if go_positive and go_negative:
                return False

        return True



points = [[0,0],[0,1],[1,1],[1,0]]
Sol = Solution()
print Sol.isConvex(points)
