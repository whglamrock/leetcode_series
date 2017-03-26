
# divide and conquer solution.

class Solution(object):
    def diffWaysToCompute(self, input):

        if input.isdigit():    # a very powerful python string operator!
            return [int(input)]

        res = []
        for i in xrange(len(input)):
            if input[i] in '+-*':
                res1 = self.diffWaysToCompute(input[:i])
                res2 = self.diffWaysToCompute(input[i+1:])
                for j in res1:
                    for k in res2:
                        res.append(self.helper(j, k, input[i]))

        return res

    def helper(self, l, r, operator):
        if operator == '+':
            return l + r
        elif operator == '-':
            return l - r
        else:
            return l * r



Sol = Solution()
input = '2*3-4*5'
print Sol.diffWaysToCompute(input)
