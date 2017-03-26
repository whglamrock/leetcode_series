
# bitwise manipulation, idea came from: https://discuss.leetcode.com/topic/12133/bit-operation-solution-java/2
# the last digit of (odd number & even number) == 0. So compare all digits of m,n from right to left.
# If m!=n exits for new m and n, there is at least an odd number and an even number between [m,n]

class Solution(object):
    def rangeBitwiseAnd(self, m, n):

        if m == 0:
            return 0

        movefactor = 1
        while m != n:   # move the comparing digit from right to left.
            # e.g., m = 1110, n = 1111, once cut their digits from right to left, the left part of n is always
            # >= the left part of m: 111 >= 111, 11 >= 11, 1 >= 1. Same goes for n = 1000, m = 0111, etc.
            # (from left to right it doesn't work, e.g. m = 0111, n = 1000).
            m >>= 1    # after every while loop, all old numbers within old [m,n] will be within new [m,n]
            n >>= 1    # with themselves modified.
            movefactor <<= 1    # 10.....0 (x zeroes, x = how many times the while loop executed)
                                # once movefactor << once, it means there is at least one odd number and one even
                                # number within [m,n]: the last digit of (odd number & even number) == 0,
                                # so the last digit of this (m&....&n) == 0

        return m*movefactor # same with n*movefactor cuz m==n at this moment
                            # m and n can be 0.