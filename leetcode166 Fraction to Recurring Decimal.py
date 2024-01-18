# bear in mind the test cases like: 1 / 3, 1 / 6, 1 / 2, 2 / 1, etc.
class Solution(object):
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        curr = []
        if numerator * denominator < 0:
            curr.append('-')
        numerator = abs(numerator)
        denominator = abs(denominator)

        n, numerator = numerator / denominator, numerator % denominator
        curr.append(str(n))
        if numerator:
            curr.append('.')
            # numerator *10 here as if it's a new numerator
            numerator *= 10

        i = 1
        # j not None means that we are seeing repeating part
        j = None
        numeratorToIndex = {}

        # notice the order we do each operation
        while numerator:
            # the following if block should be written at last for the while loop
            if numerator in numeratorToIndex:
                j = numeratorToIndex[numerator]
                break

            # 1) add numerator to visited map here because each added digit n should correspond to the numerator;
            # i.e, we wanna check if the same numerator occurs again
            numeratorToIndex[numerator] = i
            # 2) do the division and add the digit to curr result
            n, numerator = numerator / denominator, numerator % denominator
            curr.append(str(n))

            # 3) increment digit index reference, and prepare new numerator
            i += 1
            numerator *= 10

        if j is not None:
            k = curr.index('.') + j
            repeatingPart = curr[k:]
            ans = curr[:k]
            ans.append('(')
            ans += repeatingPart
            ans.append(')')
        else:
            ans = curr

        return ''.join(ans)


print(Solution().fractionToDecimal(-5, 6))
print(Solution().fractionToDecimal(1, 6))
print(Solution().fractionToDecimal(1, 2))
print(Solution().fractionToDecimal(1, 3))
print(Solution().fractionToDecimal(2, 1))
print(Solution().fractionToDecimal(13, 7))
