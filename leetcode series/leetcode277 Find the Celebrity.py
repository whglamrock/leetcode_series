# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

# O(n) calls of knows API
class Solution(object):
    def findCelebrity(self, n):

        if n <= 1:
            return n - 1

        # avoiding using two pointers i, j, the following approach find the candidate much faster
        x = 0
        for i in xrange(n):
            # the old x will no longer be candidate, but i will be
            if knows(x, i):
                x = i
        # when the x is the final x,
        #   all knows(x, i) are False where i from x + 1 to n - 1, which means
        #   all x + 1 to n - 1 can't be candidate

        # the above for loop is to select out the only possible candidate:
        #   if there is another one candidate y (y < x), then knows(y, i) will remain False
        #   ans x will be occur. Thus the hypothesis doesn't apply.

        for j in xrange(x):
            if knows(x, j):
                return -1

        # it is necessary (P.S., try '0 doesn't know 1, 1 doesn't know 0').
        for j in xrange(n):
            if not knows(j, x):
                return -1

        return x