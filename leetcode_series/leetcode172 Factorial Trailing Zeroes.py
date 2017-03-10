'''class Solution(object):
    def trailingZeroes(self, n):
        return 0 if n < 5 else n/5 + self.trailingZeroes(n/5)
'''
# The above is the perfect recursive solution.
# The algorithm can be found here: http://bookshadow.com/weblog/2014/12/30/leetcode-factorial-trailing-zeroes/

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = 5
        ans = 0
        while n >= x:
            ans += n/x
            x *= 5
        return ans


Sol = Solution()
a = 5
print Sol.trailingZeroes(a)


