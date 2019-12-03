
# two things that you should notice:
# 1): the multi-digit numbers in the expression should not start with zero
# 2): we need to keep record of last added clause in case the next operator is '*'

# It is inconvenient to use memoization in this question:
#   considering the length of current num and leftResult as the key of memo, then different
#   path with the same key could yield different final results because of the variation the last claus
# There is no solution with memoization brought up in discuss

class Solution(object):
    def addOperators(self, num, target):

        self.ans = []
        for i in xrange(1, len(num) + 1):
            # it is legal when num[:i] == '0', and the "i == 1" condition is for this
            if i == 1 or (i > 1 and num[0] != '0'):
                self.dfs(num[i:], int(num[:i]), num[:i], int(num[:i]), target)

        return self.ans

    # lastClause is set for operator '*';
    # also, there is no way to save the leftExpression to prune all afterward DFSes, because we always
        # need to try out three operators
    def dfs(self, num, leftResult, leftExpression, lastClause, target):

        if not num:
            if leftResult == target:
                self.ans.append(leftExpression)
            return

        # because the nextNum is num[:i], i starts from 1
        for i in xrange(1, len(num) + 1):
            val = int(num[:i])
            nextNum = num[i:]
            # we need to put the "whether starts with 0" check here instead of arbitrarily using
            #   "if num[0] == '0': return " to end the recursion
            if i == 1 or (i > 1 and num[0] != '0'):
                self.dfs(nextNum, leftResult + val, leftExpression + '+' + str(val), val, target)
                self.dfs(nextNum, leftResult - val, leftExpression + '-' + str(val), -val, target)
                self.dfs(nextNum, leftResult - lastClause + lastClause * val, leftExpression + '*' + str(val), lastClause * val, target)



print Solution().addOperators('105', 5)
