
class Solution(object):
    def convertToBase7(self, num):

        if num == 0: return '0'
        value = abs(num)
        digits = []

        while value:
            bit = value % 7
            digits.append(str(bit))
            value /= 7

        if num < 0:
            digits.append('-')
        digits.reverse()
        ans = ''.join(digits)

        return ans