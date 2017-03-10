# idea from: https://discuss.leetcode.com/topic/58334/a-couple-of-java-solutions-with-explanations
# logic is we divide into three conditions.
class Solution(object):
    def integerReplacement(self, n):

        count = 0
        bits = 1
        while bits < n:
            bits <<= 1
        #print bits

        while n != 1:
            #print n
            if n & 1 == 0:
                n >>= 1
                count += 1
                bits >>= 1
                continue
            countbit1, countbit2 = 0, 0
            originalbits = bits
            while bits > 0:
                if bits & (n - 1) != 0:
                    countbit1 += 1
                if bits & (n + 1) != 0:
                    countbit2 += 1
                bits >>= 1
            bits = originalbits
            #print countbit1, countbit2
            if n == 3 or countbit1 < countbit2:
                n -= 1
            else:
                n += 1
            count += 1

        return count