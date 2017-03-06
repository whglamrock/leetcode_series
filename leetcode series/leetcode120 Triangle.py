'''
modify the triangle, from top to bottom:
'''
class Solution(object):
    def minimumTotal(self, triangle):
        if not triangle:
            return

        for i in xrange(1, len(triangle)):
            for j in xrange(len(triangle[i])):
                if j == 0:
                    triangle[i][0] = triangle[i-1][0] + triangle[i][0]
                elif j == len(triangle[i])-1:
                    triangle[i][j] = triangle[i-1][j-1] + triangle[i][j]
                else:
                    triangle[i][j] = min(triangle[i-1][j-1], triangle[i-1][j]) + triangle[i][j]

        return min(triangle[-1])

triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
Sol = Solution()
print Sol.minimumTotal(triangle)


# if the interviewer don't allow to modify the triangle, o(n) space solution is:
# use the above triangle as an example and write down the 'res' in each for loop.
class Solution(object):
    def minimumTotal(self, triangle):

        if not triangle:
            return
        res = triangle[-1]
        for i in xrange(len(triangle)-2, -1, -1):  # new res[j] is the min that sums from bottom to current triangle[i][j]
            for j in xrange(len(triangle[i])):
                res[j] = min(res[j], res[j+1]) + triangle[i][j]   # only the 1st i+1 res[j] elements are modified
                # thus, in the last loop, only 1 element -- res[0] is modified.

        return res[0]