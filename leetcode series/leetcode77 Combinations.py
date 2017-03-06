# inefficient solution o(n^2) time complexity. In this question there is no way to do
# with better time complexity. Better backtracking solution can be found
# on: https://leetcode.com/discuss/61607/ac-python-backtracking-iterative-solution-60-ms
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []
        for i in xrange(k):
            new = []
            if (not ans):
                for j in xrange(1,n+2-k):
                    new.append([j])
            else:
                for item in ans:
                    for l in xrange(item[-1]+1,n-k+i+2):
                        new.append(item+[l])
            ans = new

        return ans