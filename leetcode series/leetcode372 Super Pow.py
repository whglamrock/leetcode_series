'''
a very complicated math question. Should be marked hard.
idea from: https://discuss.leetcode.com/topic/50586/math-solusion-based-on-euler-s-theorem-power-called-only-once-c-java-1-line-python/2
'''
class Solution(object):
    def superPow(self, a, b):

        #return 0 if a % 1337 == 0 else pow(a, reduce(lambda x, y: (x * 10 + y) % 1140, b) + 1140, 1337)
        # please remember the reduce built-int function

        if a % 1337 == 0:
            return 0

        for i in xrange(len(b)):
            b[i] = str(b[i])
        num = int(''.join(b))
        num %= 1140
        if num == 0:
            b = 1140
        else:
            b = num

        return pow(a, b, 1337)


Sol = Solution()
print Sol.superPow(2, [1, 0, 0, 0])