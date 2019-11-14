
# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

# O(n) calls of knows API

class Solution(object):
    def findCelebrity(self, n):

        # IMPORTANT! it is very easy to forget to check the corner case
        if n <= 1:
            return n - 1

        x = 0
        for i in xrange(n):
            if i == x:
                continue
            # means the current x can't be the celebrity
            if knows(x, i):
                x = i

        # after the above for loop, x don't know all people from x + 1 to n - 1 (x + 1 to n - 1 ruled out)
        #   and all people from 0 to x - 1 were also ruled out because if they are possible celebrity,
        #   then they won't be removed by "x = i".
        # so we only need to check people from 0 to x - 1
        for j in xrange(x):
            if knows(x, j):
                return -1

        # then at this point, x don't know anyone in the party
        #   at last we need to make sure everybody else knows him
        #   P.S.: try test case --"0 doesn't know 1, 1 doesn't know 0"
        for j in xrange(n):
            if not knows(j, x):
                return -1

        return x