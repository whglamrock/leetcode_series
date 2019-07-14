
# the proof should be able to be thought of at any time so it's easy level

class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        # if N is even number, Alice just picks N/2 and she wins
        # else if N is a prime number (> 2), Alice can only pick 1, the remaining N
        # becomes a even number so Bob wins
        # else then we can let N = a * b (both a & b are not even number), no matter
        # Alice picks a or b, the remaining N becomes (a - 1) * b or a * (b - 1)
        # and both them are even number so Bob wins again

        return N % 2 == 0