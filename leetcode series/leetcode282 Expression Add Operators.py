# two things that you should notice:
# 1): the multi-digit numbers in the expression should not start with zero
# 2): we need to keep record of last added clause in case the next operator is '*'

# It is inconvenient to use memoization in this question:
#   considering the length of current num and leftresult as the key of memo, then different
#   path with the same key could yield different final results because of the variation the last claus
# Plus, there is no solution with memoization brought up in discuss

class Solution(object):
    def addOperators(self, num, target):

        if not num: return []

        self.ans = []
        self.target = target
        for i in xrange(1, len(num) + 1):
            if i == 1 or (i > 1 and num[0] != '0'):
                self.dfs(num[i:], num[:i], int(num[:i]), int(num[:i]))

        return self.ans

    # the last means the last claus, which is very import if the next operator is '*'
    def dfs(self, num, leftexpression, leftresult, last):

        if not num:
            if leftresult == self.target:
                self.ans.append(leftexpression)
            return

        for i in xrange(1, len(num) + 1):
            # we need to avoid the situation when the val is '0XXX...'
            if i == 1 or (i > 1 and num[0] != '0'):
                val = num[:i]
                self.dfs(num[i:], leftexpression + '+' + val, leftresult + int(val), int(val))
                # make the parameter last '-int(val)' in '-' case, so the parameter last in '*' can consistent
                self.dfs(num[i:], leftexpression + '-' + val, leftresult - int(val), -int(val))
                self.dfs(num[i:], leftexpression + '*' + val, leftresult - last + last * int(val), last * int(val))
