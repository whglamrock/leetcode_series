
# define the isBadVersion(num) as an 'API'...

def isBadVersion(num):

    if num <= 11:  # however, the bound for num could be any number besides 11.
        return False
    else:
        return True


class Solution(object):
    def firstBadVersion(self, n):

        # there is no need to check whether n == 0, because n always >= 1 according to the problem
        l, r = 1, n

        while l < r:
            mid = l + (r - l) / 2
            # all versions after this are bad
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1

        return l



Sol = Solution()
print Sol.firstBadVersion(13)
        

