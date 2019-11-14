
# This is not really an easy level question

# see Sieve of Eratosthenes: https://www.youtube.com/watch?v=eKp56OLhoQs
# time complexity O(n/2 + n/3 + n/5 + n/7 + n/11 + ...) = O(N * log(logN)).

class Solution(object):
    def countPrimes(self, n):

        if n < 3: return 0

        primes = [True] * n
        primes[0] = primes[1] = False

        # Because we only needa check up to sqrt(m) to see if m is prime,
        # then if we want to put some index m False, then we only need to check up to sqrt(m).
        # And in this case, m is from 2 to n, so the sqrt(m) <= sqrt(n).
        # So i from 2 to sqrt(n), we can then assure every non-prime number within n will be
        # put False (e.g., if n - 1 non-prime, it will be put False at some point
        # from i = 2 to sqrt(n - 1), same for n - 2, n - 3..., 4)
        for i in xrange(2, int(n ** 0.5) + 1):
            # is i is a prime number, then all numbers that can be
            # divided by i are not prime.
            if primes[i]:
                for j in xrange(2 * i, n, i):
                    primes[j] = False

        return sum(primes)



Sol = Solution()
print Sol.countPrimes(12)

