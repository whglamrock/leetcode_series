class Solution(object):
    def plusOne(self, digits):

        if not digits or len(digits) == 0:
            return

        carry = 1
        for i in xrange(len(digits) - 1, -1, -1):
            digits[i], carry = (digits[i] + carry) % 10, (digits[i] + carry) / 10

        if carry == 1:
            digits = [1] + digits

        return digits


a = [1,2,3,4,5,6]
b = Solution()
print b.plusOne(a)



