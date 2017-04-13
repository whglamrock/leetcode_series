
# two things that you should notice:
# 1): the multi-digit numbers in the expression should not start with zero
# 2): we need to keep record of last added clause in case the next operator is '*'

# It is inconvenient to use memoization in this question:
#   considering the length of current num and leftresult as the key of memo, then different
#   path with the same key could yield different final results because of the variation the last claus
# Plus, there is no solution with memoization brought up in discuss


class Solution(object):
    def addOperators(self, num, target):

        self.ans = []
        for i in xrange(1, len(num) + 1):
            # it is legal when num[:i] == '0', and the "i == 1" condition is for this
            if i == 1 or (i > 1 and num[0] != '0'):
                self.helper(num[i:], int(num[:i]), num[:i], int(num[:i]), target)

        return self.ans

    # lastclause is set for operator '*'
    def helper(self, num, leftresult, leftexpression, lastclause, target):

        if not num:
            if leftresult == target:
                self.ans.append(leftexpression)
            return

        # because the nextnum is num[:i], i starts from 1
        for i in xrange(1, len(num) + 1):
            val = num[:i]
            nextnum = num[i:]
            # we need to put the "whether starts with 0" check here instead of arbitrarily using
            #   "if num[0] == '0': return " to end the recursion
            if i == 1 or (i > 1 and num[0] != '0'):
                self.helper(nextnum, leftresult + int(val), leftexpression + '+' + val, int(val), target)
                self.helper(nextnum, leftresult - int(val), leftexpression + '-' + val, -int(val), target)
                self.helper(nextnum, leftresult - lastclause + lastclause * int(val), leftexpression + '*' + val, lastclause * int(val), target)