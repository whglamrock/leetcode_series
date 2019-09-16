
# make it simple for testing purpose

def isBadVersion(num):
    return num > 11



class Solution(object):
    def firstBadVersion(self, n):

        # there is no need to check whether n == 0, because n always >= 1 according to the problem
        l, r = 1, n

        while l < r:
            m = l + (r - l) / 2
            # all versions after this are bad
            if isBadVersion(m):
                r = m
            else:
                l = m + 1

        return l



print Solution().firstBadVersion(13)
        

