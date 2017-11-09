
# simple solution

class Solution(object):
    def findComplement(self, num):

        i = 1
        # notice the condition here: "<=" instead of "<"
        while i <= num:
            i <<= 1

        return (i - 1) ^ num



Sol = Solution()
print Sol.findComplement(17)



'''
# solution with extra spaced used
class Solution(object):
    def findComplement(self, num):

        bits = []
        while num:
            bit = num & 1
            if bit == 1:
                bits.append(0)
            else:
                bits.append(1)
            num >>= 1

        #print bits
        ans = 0
        while bits:
            ans <<= 1
            ans |= bits.pop()

        return ans
'''