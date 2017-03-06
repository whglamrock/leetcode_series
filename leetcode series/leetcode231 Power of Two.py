# for all number n that is power of 2: only one of its binary bits is 1 (8 = 1000(2)). So if n is
# power of 2, n = 1000..0(2)(in this case we assume the binary number has y-1 0s).  So n-1 must be:
# n-1 = 0XXXX...X (y-1 numbers, 1 or 0). Because the first yth digit of n-1 is 0, n&(n-1)=0
# for all numbers that are not power of 2, they don't have this feature.

class Solution(object):
    def isPowerOfTwo(self, n):

        if n <= 0:
            return False
        else:
            return n&(n-1) == 0 # "&" is yu yunsuan (e.g. 5&3=1).


Sol = Solution()
print Sol.isPowerOfTwo(8)

'''
class Solution(object):
    def isPowerOfTwo(self, n):

        if n <= 0:
            return False
        while n>1:
            temp = n
            n = n>>1
            if n*2 != temp:
                return False

        return True
'''