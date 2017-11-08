
class Solution(object):
    def nthUglyNumber(self, n):
        
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        while n > 1:
            u2, u3, u5 = 2 * ugly[i2], 3 * ugly[i3], 5 * ugly[i5] # This is where amazing happens! "*ugly[i]", not i
            # so the above line ensures that every ugly[i] is also an ugly number too (i.e. it can't be 7, 14, etc.)
            umin = min(u2, u3, u5)
            if umin == u2:
                i2 += 1
            if umin == u3:  # it's not elif XXX because when u2 == u3 == 6, we need to update both i2, i3
                i3 += 1    # to avoid duplicates
            if umin == u5:
                i5 += 1
            ugly.append(umin)
            n -= 1
        return ugly[-1]



Sol = Solution()
print Sol.nthUglyNumber(17)
