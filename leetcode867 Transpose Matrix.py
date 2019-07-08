
class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(A), len(A[0])
        ans = [[0 for j in xrange(m)] for i in xrange(n)]

        for i in xrange(m):
            for j in xrange(n):
                ans[j][i] = A[i][j]

        return ans



'''
# practice

class Solution(object):
    def transpose(self, A):
        return [[A[i][j] for i in xrange(len(A))] for j in xrange(len(A[0]))]
'''