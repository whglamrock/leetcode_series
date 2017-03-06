# -*- coding: utf-8 -*-
class Solution(object): # binary manipulation trick
    def reverseBits(self, n):
        
        ans = 0
        for i in xrange(32):
            ans = (ans << 1) + (n & 1) #二进制与操作符"&": http://www.tutorialspoint.com/python/python_basic_operators.htm
            n >>= 1
        return ans
# if n = 234 = 00000000000000000000000011101010, the for loop从右到左将二进制转换成十进制;
# 将"<<1"看成"*2", 那么最右的0乘了31次,右二的1乘了31次,以此类推(只是乘号"*"通过for循环和ans = (ans << 1) + (n & 1)的操作分插
# 在一层层的括号里了: 例如((((0*2)+1)*2+0)*2+1)=5,其实是0*2^3+1*2^2+0*2^1+1*2^0变形,以便放到每一次loop里)

a = 43261596
Sol = Solution()
print Sol.reverseBits(a)


'''
class Solution(object):
    def reverseBits(self, n):
        
        def find(num):
            i = 0
            while 2**i<=num:
                i += 1
            i -= 1
            return i

        lst = []
        while n > 0:
            j = find(n)
            lst.append(j)
            n -= 2**j

        bits = [0 for x in xrange(32)]
        for item in lst:
            bits[item] = 1

        res = 0
        length = len(bits)
        for y in xrange(32):
            if bits[length-1-y] == 1:
                res += 2**y

        return res
'''




