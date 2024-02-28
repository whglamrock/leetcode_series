from collections import deque
from math import sqrt

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        firstHalf, secondHalf = [], deque()
        for i in range(1, int(sqrt(n)) + 1):
            if n % i == 0:
                firstHalf.append(i)
                if i != n // i:
                    secondHalf.appendleft(n // i)

        if len(firstHalf) >= k:
            return firstHalf[k - 1]
        else:
            k -= len(firstHalf)
            if k > len(secondHalf):
                return -1
            return secondHalf[k - 1]
