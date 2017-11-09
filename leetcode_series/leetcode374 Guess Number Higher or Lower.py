
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

# the goal is to track down 'my' number

class Solution(object):
    def guessNumber(self, n):

        l, r = 1, n
        while l <= r:
            mid = (l+r)/2
            if guess(mid) == -1:  # 'my' number is lower, means the goal should be on the left side
                r = mid-1
            elif guess(mid) == 1:  # 'my' number is higher, means the goal should be on the right side
                l = mid+1
            else:
                return mid

        return l

