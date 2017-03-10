'''A very straightforward solution that converts the 10-ary number into 26-ary ones: the tricky part is the lack
of equivalent number '0'. Because in the Excel sheet column, when in the input n == 1, it means the first column A.
The last digit of every column is at least 'A' (not start from 0).
   However, the conversion is still done by the same way: "n%26" to get the value for every digit. It is just "every
number is added by 1 "(like in 10-ary numbers, 0 to 9 became 1 to 10; in 26-ary numbers, 0-25 became 1-26)
'''
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        r = ''
        while(n>0):
            n -= 1
            r = chr(n%26+65) + r
            n /= 26
        return r

Sol = Solution()
print Sol.convertToTitle(702)

# Let's take n = 525 as an example (525 = TE). In the function: n = n-1 = 525-1 = 524; n%26 = 524%26 = 4; n = n/26
# = 524/26 (same as 525/26) = 20; n = n-1 = 20-1 = 19 [Attention: because of the existence of first 26 letters A to Z,
# the first digit of 26-ary "525" should be 20-1 = 19. chr(19+65) = T. Let's consider every 26 numbers as a cycle.
# We use "n -= 1" because the number "20" (acquired by 525/26) only means there are 20 complete cycles preceding the
# 525, and the first one can not be used for computing the "'shi'weishu". "'shi'weishu" starts and changes from the
# second cycle.]

# P.S. : 26^3+26^2+26 = 26(26(26+1)+1) => so every time n = n/26, it needs to - 1 to start computing the next n

# Another explanation for the above is that the ASCII code of capital letters starts from 65 (A). In our case, if we
# don't use n -= 1, 525%26=5, 5+65=70(F, not E!). At this time, you might be thinking about using chr(n%26+64) and
# dump the 'n -= 1'. Unfortunately, this doesn't work when the input n is the multiple of 26 (i.e. n = k*26, k is
# integer).


#class Solution(object):     # A more troublesome solution that will pass...
#    def convertToTitle(self, n):
#        """
#        :type n: int
#        :rtype: str
#        """
#        r = ''
#        while(n>0):
#            if n%26 != 0:
#                r = chr(n%26+64) + r
#                n /= 26
#            else:
#                n -= 1
#                r = chr(n%26+65) + r
#                n /= 26
#
#        return r