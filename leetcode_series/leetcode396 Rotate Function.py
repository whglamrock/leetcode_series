# easy question.
class Solution(object):
    def maxRotateFunction(self, A):

        if (not A) or len(A) == 0:
            return 0

        s = sum(A)
        olds = 0
        for i, num in enumerate(A):
            olds += i * num

        if len(A) == 1:
            return olds

        maxsum = olds
        for i in xrange(1, len(A)):
            curs = olds + s - len(A) * A[len(A) - i]    # key step
            maxsum = max(maxsum, curs)
            olds = curs

        return maxsum