# -*- coding: utf-8 -*-

'''
bit manipulation, idea came from: https://discuss.leetcode.com/topic/49900/python-solution
熟悉负数的二进制表达,32位反码和补码的概念. 比如-1在二进制中表示成为32个1.
二进制中负数取余操作见:http://www.cnblogs.com/zhangziqiu/archive/2011/03/30/computercode.html
所以(-6) % 4294967296 = (-6) - 4294967296 * [(-6)/4294967296] = (-6) - 4294967296 * (-1) = 4294967290;
类似的, (-4294967294) % 4294967296 = 2.
而乘除操作只是加减操作的累积,见:http://www.cnblogs.com/dandingyy/archive/2012/10/29/2745570.html.
'''

# P.S.: 注意十六进制的表示方法; python中储存的整数有64位 (at least more than 32 bits)
# see idea and explanation from: https://discuss.leetcode.com/topic/51999/python-solution-with-no-completely-bit-manipulation-guaranteed/2

class Solution(object):
    def getSum(self, a, b):

        # 32 bits integer max
        MAX = 0x7FFFFFFF

        # 32 bits interger min
        MIN = 0x80000000

        # the "^mask" step gets the last 32 bits
        mask = 0xFFFFFFFF

        while b != 0:
            # ^ get different bits and & gets double 1s, << moves carry
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        # if a is negative, get its last 32 bits first,
        #   then use '~' to reverse to its negative value
        return a if a <= MAX else ~(a ^ mask)


Sol = Solution()
print Sol.getSum(-1,3)






