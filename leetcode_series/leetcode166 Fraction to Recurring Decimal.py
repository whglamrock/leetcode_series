
# we need to consider a lot of tricky edge cases, so when faced with such questions in interview, ask the interviewer
# to give you as many test cases as possible

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):

        if numerator == 0:
            return '0'

        flag = numerator/denominator
        numerator, denominator = abs(numerator), abs(denominator)
        digits = []
        remainder = numerator
        dick = {}

        while remainder > 0:
            if remainder not in dick:
                dick[remainder] = len(digits)
            else:
                # dick[remainder] is the first position that the cycle starts
                break
            if remainder < denominator:
                digits.append('0')
            else:
                if remainder/denominator >= 10:    # for case like 71/3 = 23, new remainder = 2. We need to add '2' and '3' one by one
                    rip = str(remainder/denominator)
                    for i in xrange(len(rip)):
                        digits.append(rip[i])
                else:
                    digits.append(str(remainder/denominator))   # the remainder/denominator is one digit.
                remainder -= (remainder/denominator) * denominator
            remainder *= 10  # when we do the division, the remainder will be added a '0' behind to continue the next round.

        start = len(str(numerator/denominator))
        if remainder == 0:
            if start == len(digits):
                ans = ''.join(digits)
            else:
                ans = ''.join(digits[:start]) + '.' + ''.join(digits[start:])
        else:
            ans = ''.join(digits[:start]) + '.' + ''.join(digits[start:dick[remainder]]) + '(' + ''.join(digits[dick[remainder]:]) + ')'
            # very tricky case could be like 1/6, where the cycle doesn't start at the first decimal point
            # 'interger part' + '.' + 'non-cycle decimal digits' + '(' + 'cycle digits' + ')'
        if flag < 0:
            ans = '-' + ans
        return ans



Sol = Solution()
numerator = -5
denominator = 6
print Sol.fractionToDecimal(numerator, denominator)
