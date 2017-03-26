
'''
idea came from: https://leetcode.com/discuss/24282/dp-solution-in-6-lines-with-explanation-f-i-n-g-i-1-g-n-i
dynamic programming
'''

class Solution(object):
    def numTrees(self, n):

        if n == 1:
            return 1
        if n == 2:
            return 2

        g = [0 for i in xrange(n+1)]
        g[0],g[1] = 1,1

        for i in xrange(2,n+1):
            for j in xrange(1,i+1):
                g[i] += g[j-1]*g[i-j]

        return g[n]