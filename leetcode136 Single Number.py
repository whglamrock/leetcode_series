
class Solution(object):
    def singleNumber(self, nums):

        res = 0
        for num in nums:
            res ^= num
        return res



Sol = Solution()
print Sol.singleNumber([2,1,4,5,4,2,1])



'''
Let's assume a = 60, b = 19, so their binary expressions are
a = 00111100, b = 00001101. a^b = 00110001 (for all digits, if corresponding digits of two number are same, the
result is 0; otherwise it is 1. Thus, n^n=0). And the ^ operator is cumulative: 2^2^3^3^5 = 5: (0010)^(0010) = 0000,
(0000)^(0011) = 0011, (0011)^(0011) = 0000, (0000)^(0101) = 0101 = 5
'''