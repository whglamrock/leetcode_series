class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = 0
        for i in range(n/2+1):
            increase = 1
            if i != 0:
                for j in range(i):
                    increase = increase * (n-j-i)/(j+1)
            total += increase

        return total


a = Solution()
b = a.climbStairs(6)
print b